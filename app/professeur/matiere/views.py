# app/formation/views.py

from flask import flash, redirect, render_template, url_for, abort
from flask_login import login_required, current_user
from app.professeur.matiere import profmatieres
from app import db
#from ..forms import FormationForm
from ...models import Formation, Etudiant, Matiere, Announce, Cours


@profmatieres.route('/matiere/accueilMatiere/<int:id>', methods=['GET', 'POST'])
@login_required
def accueilMatiere(id):

    matieres = Matiere.query.get_or_404(id)
    etudiants = Etudiant.query.join(Formation).join(Matiere).filter_by(id=id)
    nb_etudiant = etudiants.count()
    cours = Cours.query.filter_by(matiere_id=id)
    nb_cours = cours.count()
    announces = Announce.query.filter_by(matiere_id=id)
    nb_annonce = announces.count()
    return render_template('professeur/matiere/AccueilMatiere.html',
                           matieres=matieres,
                           nb_etudiant=nb_etudiant, nb_annonce=nb_annonce,
                           etudiants=etudiants, cours=cours, nb_cours=nb_cours,
                           announces = announces,
                           title="Accueil Matière")

@profmatieres.route('/matieres')
@login_required
def list_matieres():

    matieres = Matiere.query.filter_by(professeur_id=current_user.id)
    return render_template('professeur/matiere/liste_matieres.html',
                           matieres=matieres,
                           title="Liste Matières")
