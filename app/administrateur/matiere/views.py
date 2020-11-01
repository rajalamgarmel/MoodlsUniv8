# app/admin/views.py

from flask import flash, redirect, render_template, url_for, abort
from flask_login import login_required, current_user
from app.administrateur.matiere import matieres
from app import db
from ..forms import MatiereForm
from ...models import Matiere


# Matiere Views


@matieres.route('/matiere/<int:id>', methods=['GET', 'POST'])
@login_required
def list_matieres(id):
    """
    List all matieres
    """
    matieres = Matiere.query.filter_by(formation_id=id)

    return render_template('administrateur/matiere/matieres.html', idFormation=id,
                           matieres=matieres, title="Matieres")


@matieres.route('/matieres/add/<int:id>', methods=['GET', 'POST'])
@login_required
def add_matieres(id):
    """
    Add a matieres to the database
    """

    add_matieres = True

    form = MatiereForm()
    if form.validate_on_submit():
        matieres = Matiere(label_matiere=form.label_matiere.data,
                           description=form.description.data,
                           professeur=form.professeur.data,
                           formation_id=id)
        try:
            # add matieres to the database
            db.session.add(matieres)
            db.session.commit()
            flash('You have successfully added a new matiere.')
        except:
            # in case matieres name already exists
            flash('Error: matieres name already exists.')

        # redirect to matieres page
        return redirect(url_for('matieres.list_matieres', id=matieres.formation_id))

    # load matieres template
    return render_template('administrateur/matiere/matiere.html', action="Add",
                           add_matieres=add_matieres, form=form,
                           title="Add Matieres")


@matieres.route('/matieres/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_matieres(id):
    """
    Edit a matieres
    """

    add_matieres = False

    matieres = Matiere.query.get_or_404(id)
    form = MatiereForm(obj=matieres)
    if form.validate_on_submit():
        matieres.label_matiere = form.label_matiere.data
        matieres.description = form.description.data
        matieres.professeur = form.professeur.data
        db.session.commit()
        flash('You have successfully edited the matieres.')

        # redirect to the departments page
        return redirect(url_for('matieres.list_matieres', id=matieres.formation_id))

    form.description.data = matieres.description
    form.label_matiere.data = matieres.label_matiere
    form.professeur.data = matieres.professeur
    return render_template('administrateur/matiere/matiere.html', action="Edit",
                           add_matieres=add_matieres, form=form,
                           matieres=matieres, title="Edit Matieres")


@matieres.route('/matieres/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_matieres(id):
    """
    Delete a matieres from the database
    """

    matieres = Matiere.query.get_or_404(id)
    db.session.delete(matieres)
    db.session.commit()
    flash('You have successfully deleted the matiere.')

    # redirect to the matieres page
    return redirect(url_for('matieres.list_matieres', id=matieres.formation_id))

    return render_template(title="Delete Matieres")
