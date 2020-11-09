# app/matiere/__init__.py

from flask import Blueprint

profmatieres = Blueprint('profmatieres', __name__)

from . import views


