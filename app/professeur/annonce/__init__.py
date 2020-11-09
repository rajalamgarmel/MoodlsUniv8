# app/annonce/__init__.py

from flask import Blueprint

profannonces = Blueprint('profannonces', __name__)

from . import views