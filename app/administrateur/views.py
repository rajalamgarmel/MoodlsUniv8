# app/administrateur/views.py

from flask import flash, redirect, render_template, url_for, abort
from flask_login import login_required, login_user, logout_user, current_user
from app.administrateur import administrateur
from .. import db
from .forms import LoginForm
from ..models import Administrateur


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
    return render_template('administrateur/LoginAdmin.html', form=form, title='Login')


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

    return render_template('administrateur/AccueilSuperAdm.html', title="Accueil Super Administrateur")


@administrateur.route('/AccueilAdmin')
@login_required
def AccueilAdmin():
    """
    Render the dashboard template on the /AccueilAdmin route
    """
    return render_template('administrateur/AccueilAdmin.html', title="Accueil Administrateur")

@administrateur.route('/Profil')
@login_required
def profil():
    """
    Render the dashboard template on the /Profil route
    """
    """
     Profil
     """

    administrateur = Administrateur.query.filter_by(id=current_user.id)

    return render_template('administrateur/profil.html',
                           administrateur=administrateur, title="Profil")
