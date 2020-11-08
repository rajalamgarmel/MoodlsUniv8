# app/etudiant/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    """
    Form for etudiant to login
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ProfilForm(FlaskForm):
    """
    Form to edit a profile
    """
    nom = StringField('Nom',  render_kw={'readonly': True})
    prenom = StringField('Prenom', render_kw={'readonly': True})
    dateNaissance = StringField('Date Naissance', render_kw={'readonly': True})
    email = StringField('email', render_kw={'readonly': True})
    adresse = StringField('adresse', validators=[DataRequired()])
    code_postal = StringField('Code Postal', validators=[DataRequired()])
    ville = StringField('Ville', validators=[DataRequired()])
    pays = StringField('Pays', validators=[DataRequired()])

    submit = SubmitField('Register')