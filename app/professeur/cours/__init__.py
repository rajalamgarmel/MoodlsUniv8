# app/annonce/__init__.py

from flask import Blueprint

cours = Blueprint('cours', __name__)

from . import views

