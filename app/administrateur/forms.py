# app/etudiant/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, RadioField, TextAreaField,BooleanField,SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import Administrateur, Departement, Professeur


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class DepartementForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    label = StringField('Label Departement', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AdminForm(FlaskForm):
    """
    Form for users to create new account
    """
    nom = StringField('Nom', validators=[DataRequired()])
    prenom = StringField('Prenom', validators=[DataRequired()])
    sexe = RadioField('Sexe', choices=[('M', 'M'), ('F', 'F')])
    dateNaissance = StringField('Date Naissance', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    departement = QuerySelectField(query_factory=lambda: Departement.query.all(),
                                   get_label="label_departement")
    submit = SubmitField('Register')


class FormationForm(FlaskForm):
    """
    Form for formation to create new formation
    """
    label_formation = StringField('Label Formation', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    departement = QuerySelectField(query_factory=lambda: Departement.query.all(),
                                   get_label="label_departement")
    submit = SubmitField('Register')


class ProfForm(FlaskForm):
    """
    Form for users to create new account
    """
    nom = StringField('Nom', validators=[DataRequired()])
    prenom = StringField('Prenom', validators=[DataRequired()])
    sexe = RadioField('Sexe', choices=[('M', 'M'), ('F', 'F')])
    dateNaissance = StringField('Date Naissance', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')


class EtudForm(FlaskForm):
    """
    Form for users to create new account
    """
    nom = StringField('Nom', validators=[DataRequired()])
    prenom = StringField('Prenom', validators=[DataRequired()])
    numero_etud = StringField('Numéro Etudiant', validators=[DataRequired()])
    sexe = RadioField('Sexe', choices=[('M', 'M'), ('F', 'F')])
    dateNaissance = StringField('Date Naissance', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')

class MatiereForm(FlaskForm):
    """
    Form for matiere to create new formation
    """
    label_matiere = StringField('Label Formation', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    professeur = QuerySelectField(query_factory=lambda: Professeur.query.all(),
                                   get_label="nom_prof")
    submit = SubmitField('Register')

class AnnonceForm(FlaskForm):
    """
    Form for Annonce to create new Annonce
    """
    titre = StringField('titre', validators=[DataRequired()])
    contenu = TextAreaField('contenu')
    submit = SubmitField('Register')
