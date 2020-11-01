# app/home/__init__.py

from flask import Blueprint

matieres = Blueprint('matieres', __name__)

from app.administrateur.matiere import views
