from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user, login_manager
from .. import db
from app.professeur import professeur
from .forms import LoginForm, ProfilForm
from ..models import Professeur, Matiere


@professeur.route('/loginProf', methods=['GET', 'POST'])
def loginProf():
    """
    Handle requests to the /login route
    Log an professeur in through the login form
    """
    formprof = LoginForm()
    if formprof.validate_on_submit():

        # check whether professeur exists in the database and whether
        # the password entered matches the password in the database
        professeur = Professeur.query.filter_by(email=formprof.email.data).first()
        if professeur is not None and Professeur.query.filter_by(password_hash=formprof.password.data).first():
            login_user(professeur)

            return redirect(url_for('professeur.AcceuilProfesseur'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('professeur/LoginProf.html', form=formprof, title='Login')


@professeur.route('/logoutProf')
@login_required
def logoutProf():
    """
    Handle requests to the /logout route
    Log an professeur out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('professeur.loginProf'))


@professeur.route('/AcceuilProfesseur')
@login_required
def AcceuilProfesseur():
    """
    Render the dashboard template on the /AcceuilProfesseur route
    """
    matieres = Matiere.query.filter_by(professeur_id=current_user.id)
    return render_template('professeur/AccueilProf.html', title="Accueil Professeur",
                           matieres=matieres)

@professeur.route('/profile')
@login_required
def profil():
    """
    Render the dashboard template on the /Profile route
    """
    """
     Profil
     """

    professeur = Professeur.query.filter_by(id=current_user.id)
    matieres = Matiere.query.filter_by(professeur_id=current_user.id)
    return render_template('professeur/profile/profile.html',
                           professeur=professeur, matieres=matieres ,title="profile")


@professeur.route('/profile/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_profile(id):
    """
    Render the edit template on the /Profile route
    """
    """
     Profil
     """

    professeur = Professeur.query.get_or_404(id)
    form = ProfilForm(obj=professeur)
    if form.validate_on_submit():
        professeur.adresse = form.adresse.data
        professeur.code_postal = form.code_postal.data
        professeur.ville = form.ville.data
        professeur.pays = form.pays.data
        db.session.commit()
        flash('You have successfully edited your profile.')

        # redirect to the profile page
        return redirect(url_for('professeur.profil'))

    form.nom.data = professeur.nom_prof
    form.prenom.data = professeur.prenom_prof
    form.dateNaissance.data = professeur.date_naissance
    form.adresse.data = professeur.adresse
    form.code_postal.data = professeur.code_postal
    form.ville.data = professeur.ville
    form.pays.data = professeur.pays
    return render_template('professeur/profile/edit_profile.html', action="Edit", form=form,
                           professeur=professeur, title="Edit Profile")