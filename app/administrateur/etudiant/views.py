# app/etudiant/views.py

from flask import flash, redirect, render_template, url_for, abort
from flask_login import login_required, current_user
from app.administrateur.etudiant import etudiants
from app import db
from ..forms import EtudForm
from ...models import Etudiant


@etudiants.route('/etudiants/<int:id>', methods=['GET', 'POST'])
@login_required
def list_etudiants(id):
    """
    List all etudiants
    """

    etudiants = Etudiant.query.filter_by(formation_id=id)

    return render_template('administrateur/etudiant/etudiants.html', idFormation=id,
                           etudiants=etudiants, title="etudiants")


@etudiants.route('/etudiants/add/<int:id>', methods=['GET', 'POST'])
@login_required
def add_etudiants(id):
    add_etudiants = True

    form = EtudForm()
    if form.validate_on_submit():
        etudiants = Etudiant(nom_etud=form.nom.data,
                                 prenom_etud=form.prenom.data,
                                 num_etud=form.numero_etud.data,
                                 sexe_etud=form.sexe.data,
                                 email=form.email.data,
                                 date_naissance=form.dateNaissance.data,
                                 password_hash=form.dateNaissance.data,
                                 formation_id=id)

        try:
            # add etudiant to the database
            db.session.add(etudiants)
            db.session.commit()
            flash('You have successfully added a new etudiants .')
        except:
            # in case etudiant name already exists
            flash('Error: etudiants name already exists.')

        # redirect to etudiant page
        return redirect(url_for('etudiants.list_etudiants', id=etudiants.formation_id))

    # load etudiant template
    return render_template('administrateur/etudiant/etudiant.html', action="Add",
                           add_etudiants=add_etudiants, form=form,
                           title="Add Etudiants")


@etudiants.route('/etudiants/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_etudiants(id):
    """
    Edit a etudiants
    """

    add_etudiants = False

    etudiants = Etudiant.query.get_or_404(id)
    form = EtudForm(obj=etudiants)
    if form.validate_on_submit():
        etudiants.nom_etud = form.nom.data
        etudiants.prenom_etud = form.prenom.data
        etudiants.num_etud = form.numero_etud.data
        etudiants.date_naissance = form.dateNaissance.data
        etudiants.email = form.email.data
        etudiants.sexe_etud = form.sexe.data
        db.session.commit()
        flash('You have successfully edited the etudiants.')

        # redirect to the etudiant page
        return redirect(url_for('etudiants.list_etudiants', id=etudiants.formation_id))

    form.nom.data = etudiants.nom_etud
    form.prenom.data = etudiants.prenom_etud
    form.dateNaissance.data = etudiants.date_naissance
    form.email.data = etudiants.email
    form.numero_etud.data = etudiants.num_etud
    form.sexe.data = etudiants.sexe_etud
    return render_template('administrateur/etudiant/etudiant.html', action="Edit",
                           add_etudiants=add_etudiants, form=form,
                           etudiants=etudiants, title="Edit Etudiants")


@etudiants.route('/etudiants/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_etudiants(id):
    """
    Delete a etudiants from the database
    """

    etudiants = Etudiant.query.get_or_404(id)
    db.session.delete(etudiants)
    db.session.commit()
    flash('You have successfully deleted the etudiants.')

    # redirect to the departments page
    return redirect(url_for('etudiants.list_etudiants', id=etudiants.formation_id))

    return render_template(title="Delete etudiants")
