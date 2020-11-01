# app/annonce/__init__.py

from flask import Blueprint

annonces = Blueprint('annonces', __name__)

from app.administrateur.annonce import views
