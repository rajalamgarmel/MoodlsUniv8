# app/professeur/views.py

from flask import flash, redirect, render_template, url_for, abort
from flask_login import login_required, current_user
from app.administrateur.professeur import professeurs
from app import db
from ..forms import ProfForm
from ...models import Professeur


@professeurs.route('/professeurs', methods=['GET', 'POST'])
@login_required
def list_professeurs():
    """
    List all professeurs
    """

    professeurs = Professeur.query.all()

    return render_template('administrateur/professeurs/professeurs.html',
                           professeurs=professeurs, title="Professeurs")


@professeurs.route('/professeurs/add', methods=['GET', 'POST'])
@login_required
def add_professeurs():
    add_professeurs = True

    form = ProfForm()
    if form.validate_on_submit():
        professeurs = Professeur(type='prof',
                                 nom_prof=form.nom.data,
                                 prenom_prof=form.prenom.data,
                                 sexe_prof=form.sexe.data,
                                 email=form.email.data,
                                 date_naissance=form.dateNaissance.data,
                                 password_hash=form.dateNaissance.data)

        try:
            # add professeurs to the database
            db.session.add(professeurs)
            db.session.commit()
            flash('You have successfully added a new professeurs .')
        except:
            # in case professeurs name already exists
            flash('Error: professeurs name already exists.')

        # redirect to professeurs page
        return redirect(url_for('professeurs.list_professeurs'))

    # load professeurs template
    return render_template('administrateur/professeurs/professeur.html', action="Add",
                           add_professeurs=add_professeurs, form=form,
                           title="Add Professeurs")


@professeurs.route('/professeurs/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_professeurs(id):
    """
    Edit a professeurs
    """

    add_professeurs = False

    professeurs = Professeur.query.get_or_404(id)
    form = ProfForm(obj=professeurs)
    if form.validate_on_submit():
        professeurs.nom_prof = form.nom.data
        professeurs.prenom_prof = form.prenom.data
        professeurs.date_naissance = form.dateNaissance.data
        professeurs.email = form.email.data
        professeurs.sexe_prof = form.sexe.data
        professeurs.adresse = form.adresse.data
        professeurs.code_postal = form.code_postal.data
        professeurs.ville = form.ville.data
        professeurs.pays = form.pays.data
        db.session.commit()
        flash('You have successfully edited the professeurs.')

        # redirect to the professeurs page
        return redirect(url_for('professeurs.list_professeurs'))

    form.nom.data = professeurs.nom_prof
    form.prenom.data = professeurs.prenom_prof
    form.dateNaissance.data = professeurs.date_naissance
    form.email.data = professeurs.email
    form.sexe.data = professeurs.sexe_prof
    form.code_postal.data = professeurs.code_postal
    form.adresse.data = professeurs.adresse
    form.ville.data = professeurs.ville
    form.pays.data = professeurs.pays
    return render_template('administrateur/professeurs/professeur.html', action="Edit",
                           add_professeurs=add_professeurs, form=form,
                           professeurs=professeurs, title="Edit professeurs")


@professeurs.route('/professeurs/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_professeurs(id):
    """
    Delete a professeurs from the database
    """

    professeurs = Professeur.query.get_or_404(id)
    db.session.delete(professeurs)
    db.session.commit()
    flash('You have successfully deleted the professeurs.')

    # redirect to the professeurs page
    return redirect(url_for('professeurs.list_professeurs'))

    return render_template(title="Delete professeurs")
