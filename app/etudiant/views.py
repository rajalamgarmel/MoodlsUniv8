# app/etudiant/views.py
from pathlib import Path

from flask import flash, redirect, render_template, url_for, request, send_file, current_app
from flask_login import login_required, login_user, logout_user, current_user
from .. import db
from app.etudiant import etudiant
from .forms import LoginForm, ProfilForm
from ..models import Etudiant, Matiere, Cours, Announce


@etudiant.route('/loginEtud', methods=['GET', 'POST'])
def loginEtud():
    """
    Handle requests to the /login route
    Log an etudiant in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():

        # check whether etudiant exists in the database and whether
        # the password entered matches the password in the database
        etudiant = Etudiant.query.filter_by(email=form.email.data).first()
        if etudiant is not None and Etudiant.query.filter_by(password_hash=form.password.data).first():
            # log etudiant in
            login_user(etudiant)

            return redirect(url_for('etudiant.AccueilEtud'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('etudiant/LoginEtud.html', form=form, title='Login')


@etudiant.route('/logoutEtud')
@login_required
def logoutEtud():
    """
    Handle requests to the /logout route
    Log an etudiant out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('etudiant.loginEtud'))


@etudiant.route('/AccueilEtud')
@login_required
def AccueilEtud():
    """
    Render the dashboard template on the /AccueilEtud route
    """
    nombre_matieres = Matiere.query.filter_by(formation_id=current_user.formation_id).count()
    return render_template('etudiant/AccueilEtud.html',nb_matieres =nombre_matieres, title="Accueil Etudiant")

@etudiant.route('/profile')
@login_required
def profil():
    """
    Render the dashboard template on the /Profile route
    """
    """
     Profil
     """

    etudiant = Etudiant.query.filter_by(id=current_user.id)

    return render_template('etudiant/profile/profile.html',
                           etudiant=etudiant, title="profile")


@etudiant.route('/profile/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_profile(id):
    """
    Render the edit template on the /Profile route
    """
    """
     Profil
     """

    etudiant = Etudiant.query.get_or_404(id)
    form = ProfilForm(obj=etudiant)
    if form.validate_on_submit():
        etudiant.adresse = form.adresse.data
        etudiant.code_postal = form.code_postal.data
        etudiant.ville = form.ville.data
        etudiant.pays = form.pays.data
        db.session.commit()
        flash('You have successfully edited your profile.')

        # redirect to the profile page
        return redirect(url_for('etudiant.profil'))

    form.nom.data = etudiant.nom_etud
    form.prenom.data = etudiant.prenom_etud
    form.dateNaissance.data = etudiant.date_naissance
    form.adresse.data = etudiant.adresse
    form.code_postal.data = etudiant.code_postal
    form.ville.data = etudiant.ville
    form.pays.data = etudiant.pays
    return render_template('etudiant/profile/edit_profile.html', action="Edit", form=form,
                           etudiant=etudiant, title="Edit Profile")

@etudiant.route('/matieres', methods=['GET'])
@login_required
def list_matieres():
    """
    List all matieres
    """
    matieres = Matiere.query.filter_by(formation_id=current_user.formation_id)

    return render_template('etudiant/matieres/matieres.html', idFormation=id,
                           matieres=matieres, title="Matieres")

@etudiant.route('matieres/<int:mat_id>/cours', methods=['GET'])
@login_required
def list_cours(mat_id):
    """
    List all courses
    """

    crs = Cours.query.filter_by(matiere_id=mat_id);

    return render_template('etudiant/matieres/cours/cours.html', cours=crs, title="Cours")


@etudiant.route('anonnces', methods=['GET'])
@login_required
def list_annonces():
    """
    List all courses
    """

    annonces = Announce.query.filter_by(formation_id=current_user.formation_id);

    return render_template('etudiant/annonces/annonces.html', annonces=annonces, title="Annonces")

@etudiant.route('matieres/<int:matiere_id>/cours/<string:file_path>', methods=['GET', 'POST'])
def download_file(file_path, matiere_id):
    try:
        file_to_send = Path(file_path)
        return send_file(str(file_to_send))
    except OSError as e:
        current_app.logger.error(e)
        flash("Le fichier " + file_path + " n'existe pas", "error")
    return list_cours(matiere_id)