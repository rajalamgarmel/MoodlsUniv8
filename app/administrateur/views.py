# app/administrateur/views.py

from flask import flash, redirect, render_template, url_for, abort
from flask_login import login_required, login_user, logout_user, current_user
from app.administrateur import administrateur
from .. import db
from .forms import LoginForm, ProfilForm
from ..models import Administrateur, Formation, Etudiant, Departement, Professeur,Matiere


@administrateur.route('/loginAdmin', methods=['GET', 'POST'])
def loginAdmin():
    """
    Handle requests to the /login route
    Log an Admin in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():

        # check whether admin exists in the database and whether
        # the password entered matches the password in the database
        administrateur = Administrateur.query.filter_by(email=form.email.data, password_hash=form.password.data).first()
        if administrateur is not None:
            # log admin in
            login_user(administrateur)
            db.session.commit()

            # redirect to the dashboard page after login
            # superadmin can add a simple admin
            if administrateur.is_superadmin:
                return redirect(url_for('administrateur.AccueilSuperAdm'))
            else:
                return redirect(url_for('administrateur.AccueilAdmin'))


        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('administrateur/LoginAdmin.html', form=form,
                           title='Login')


@administrateur.route('/logoutAdmin')
@login_required
def logoutAdmin():
    """
    Handle requests to the /logout route
    Log an admin out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('administrateur.loginAdmin'))


@administrateur.route('/AccueilSuperAdm')
@login_required
def AccueilSuperAdm():
    """
    Render the dashboard template on the /AccueilSuperAdm route
    """
    # prevent non-admins from accessing the page
    if not current_user.is_superadmin:
        abort(403)

    professeur = len(Professeur.query.all())
    etudiant = len(Etudiant.query.all())
    departement = len(Departement.query.all())
    administrateur = len(Administrateur.query.all())

    return render_template('administrateur/AccueilSuperAdm.html', title="Accueil Super Administrateur"
                           ,nb_administrateur=administrateur,nb_etudiant=etudiant
                           ,nb_professeur=professeur,nb_departement=departement)


@administrateur.route('/AccueilAdmin')
@login_required
def AccueilAdmin():
    """
    Render the dashboard template on the /AccueilAdmin route
    """
    formation = Formation.query.filter_by(departement_id=current_user.departement_id).count()
    etudiant = Etudiant.query.join(Formation).join(Departement)\
        .filter_by(id=current_user.departement_id)\
        .count()
    professeur = Professeur.query.all()
    professeur = len(professeur)

    return render_template('administrateur/AccueilAdmin.html', title="Accueil Administrateur"
                           , nb_formation=formation, nb_etudiant=etudiant, nb_professeur=professeur)


@administrateur.route('/profile')
@login_required
def profil():
    """
    Render the dashboard template on the /Profile route
    """
    """
     Profil
     """

    administrateur = Administrateur.query.filter_by(id=current_user.id)

    return render_template('administrateur/profile/profile.html',
                           administrateur=administrateur, title="profile")


@administrateur.route('/profile/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_profile(id):
    """
    Render the edit template on the /Profile route
    """
    """
     Profil
     """

    administrateur = Administrateur.query.get_or_404(id)
    form = ProfilForm(obj=administrateur)
    if form.validate_on_submit():
        administrateur.adresse = form.adresse.data
        administrateur.code_postal = form.code_postal.data
        administrateur.ville = form.ville.data
        administrateur.pays = form.pays.data
        db.session.commit()
        flash('You have successfully edited your profile.')

        # redirect to the profile page
        return redirect(url_for('administrateur.profil'))

    form.nom.data = administrateur.nom_admin
    form.prenom.data = administrateur.prenom_admin
    form.dateNaissance.data = administrateur.date_naissance
    form.adresse.data = administrateur.adresse
    form.code_postal.data = administrateur.code_postal
    form.ville.data = administrateur.ville
    form.pays.data = administrateur.pays
    return render_template('administrateur/profile/edit_profile.html', action="Edit", form=form,
                           administrateur=administrateur, title="Edit Profile")
