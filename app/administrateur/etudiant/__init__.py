# app/home/__init__.py

from flask import Blueprint

etudiants = Blueprint('etudiants', __name__)

from app.administrateur.etudiant import views
