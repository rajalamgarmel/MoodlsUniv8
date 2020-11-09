# app/admin/views.py

from flask import flash, redirect, render_template, url_for, abort, request, send_from_directory
from flask_login import login_required, current_user
from app.professeur.cours import cours
from app import db, app
from ..forms import CoursForm
from ...models import Cours,Matiere
import datetime
import os.path
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@cours.route('/cours/<int:id>', methods=['GET', 'POST'])
@login_required
def list_cours(id):
    """
    List all cours
    """
    cours = Cours.query.filter_by(matiere_id=id)

    return render_template('professeur/cours/cours.html', matiere_id=id,
                           cours=cours, title="Cours")


@cours.route('/cours/add/<int:id>', methods=['GET', 'POST'])
@login_required
def add_cours(id):
    """
    Add a cours to the database
    """

    add_cours = True

    form = CoursForm()
    if form.validate_on_submit():
        # check if the post request has the file part
        if 'fichier' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['fichier']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            os.makedirs(os.path.join(app.instance_path, 'cours'), exist_ok=True)
            file.save(os.path.join(app.instance_path, 'cours', filename))
            cours = Cours(type=form.type.data,
                          titre=form.titre.data,
                          description=form.description.data,
                          date=datetime.datetime.now(),
                          fichier=filename,
                          matiere_id=id)

        try:
            # add cours to the database
            db.session.add(cours)
            db.session.commit()
            flash('You have successfully added a new cours.')
        except:
            # in case cours name already exists
            flash('Error: cours name already exists.')

        # redirect to cours page
        return redirect(url_for('cours.list_cours', id=cours.matiere_id))

    # load cours template
    return render_template('professeur/cours/cour.html', action="Add",
                           add_cours=add_cours, form=form,
                           title="Add Cours")


@cours.route('/cours/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_cours(id):
    """
    Edit a cours
    """

    add_cours = False

    cours = Cours.query.get_or_404(id)
    form = CoursForm(obj=cours)
    if form.validate_on_submit():
        if form.validate_on_submit():
            # check if the post request has the file part
            if 'fichier' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['fichier']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                os.makedirs(os.path.join(app.instance_path, 'cours'), exist_ok=True)
                file.save(os.path.join(app.instance_path, 'cours', filename))
                cours.type = form.type.data
                cours.titre = form.titre.data
                cours.description = form.description.data
                cours.fichier = filename
                cours.date = datetime.datetime.now()
        db.session.commit()
        flash('You have successfully edited the cours.')

        # redirect to the annonces page
        return redirect(url_for('cours.list_cours', id=cours.matiere_id))

    form.type.data = cours.type
    form.titre.data = cours.titre
    form.description.data = cours.description
    form.fichier.data = cours.fichier

    return render_template('professeur/cours/cour.html', action="Edit",
                           add_cours=add_cours, form=form,
                           cours=cours, title="Edit Cours")


@cours.route('/cours/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_cours(id):
    """
    Delete a cours from the database
    """

    cours = Cours.query.get_or_404(id)
    db.session.delete(cours)
    db.session.commit()
    flash('You have successfully deleted the cours.')

    # redirect to the cours page
    return redirect(url_for('cours.list_cours', id=cours.matiere_id))

    return render_template(title="Delete Cours")


@cours.route('/uploads/<path:filename>', methods=['GET', 'POST'])
@login_required
def download(filename):
    uploads = os.path.join(app.instance_path, 'cours')
    return send_from_directory(directory=uploads, filename=filename)