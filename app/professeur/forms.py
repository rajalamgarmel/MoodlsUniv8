# app/professeur/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, SelectField, FileField, TextAreaField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    """
    Form for professeur to login
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

class CoursForm(FlaskForm):
    """
    Form to edit a profile
    """
    type = SelectField('Type', choices=[("COURS","COURS"),("TD","TD"),("TP","TP"),("NOTES","NOTES")])
    titre = StringField('Titre',  validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    fichier = FileField('Fichier')

    submit = SubmitField('Register')

class AnnonceForm(FlaskForm):
    """
    Form for Professeur to create new Annonce
    """
    titre = StringField('titre', validators=[DataRequired()])
    contenu = TextAreaField('contenu')
    submit = SubmitField('Register')

