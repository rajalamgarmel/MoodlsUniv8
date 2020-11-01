# app/admin/views.py

from flask import flash, redirect, render_template, url_for, abort
from flask_login import login_required, current_user
from app.administrateur.annonce import annonces
from app import db
from ..forms import AnnonceForm
from ...models import Announce
import datetime


@annonces.route('/annonces/<int:id>', methods=['GET', 'POST'])
@login_required
def list_annonces(id):
    """
    List all annonces
    """
    annonces = Announce.query.filter_by(formation_id=id)

    return render_template('administrateur/annonce/annonces.html', idFormation=id,
                           annonces=annonces, title="Annonces")


@annonces.route('/annonces/add/<int:id>', methods=['GET', 'POST'])
@login_required
def add_annonces(id):
    """
    Add a annonces to the database
    """

    add_annonces = True

    form = AnnonceForm()
    if form.validate_on_submit():
        annonces = Announce(titre=form.titre.data,
                            contenu=form.contenu.data,
                            date=datetime.datetime.now(),
                            formation_id=id)
        try:
            # add department to the database
            db.session.add(annonces)
            db.session.commit()
            flash('You have successfully added a new annonces.')
        except:
            # in case annonces name already exists
            flash('Error: annonces name already exists.')

        # redirect to annonces page
        return redirect(url_for('annonces.list_annonces', id=annonces.formation_id))

    # load department template
    return render_template('administrateur/annonce/annonce.html', action="Add",
                           add_annonces=add_annonces, form=form,
                           title="Add Annonces")


@annonces.route('/annonces/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_annonces(id):
    """
    Edit a annonces
    """

    add_annonces = False

    annonces = Announce.query.get_or_404(id)
    form = AnnonceForm(obj=annonces)
    if form.validate_on_submit():
        annonces.type = form.type.data
        annonces.titre = form.titre.data
        annonces.contenu = form.contenu.data
        annonces.date = form.date.data
        db.session.commit()
        flash('You have successfully edited the annonces.')

        # redirect to the annonces page
        return redirect(url_for('annonces.list_annonces', id=annonces.formation_id))

    form.type.data = annonces.type
    form.titre.data = annonces.titre
    form.contenu.data = annonces.contenu
    form.date.data = annonces.date
    return render_template('administrateur/annonce/annonce.html', action="Edit",
                           add_annonces=add_annonces, form=form,
                           annonces=annonces, title="Edit Annonces")


@annonces.route('/annonces/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_annonces(id):
    """
    Delete a annonces from the database
    """

    annonces = Announce.query.get_or_404(id)
    db.session.delete(annonces)
    db.session.commit()
    flash('You have successfully deleted the annonces.')

    # redirect to the annonces page
    return redirect(url_for('annonces.list_annonces', id=annonces.formation_id))

    return render_template(title="Delete Annonces")