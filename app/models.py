# app/models.py
from flask import sessions
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    temp = user_id.split('.')
    try:
        uid = temp[1]
        if temp[0] == 'administrateur':
            return Administrateur.query.get(uid)
        elif temp[0] == 'etudiant':
            return Etudiant.query.get(uid)
        elif temp[0] == 'professeur':
            return Professeur.query.get(uid)
        else:
            return None
    except IndexError:
        return None


class Administrateur(UserMixin, db.Model):
    """
    Create an Employee table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'administrateur'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(60))
    nom_admin = db.Column(db.String(60), index=True)
    prenom_admin = db.Column(db.String(60), index=True)
    sexe_admin = db.Column(db.String(60), index=True)
    date_naissance = db.Column(db.Date(), index=True)
    email = db.Column(db.String(60), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    adresse = db.Column(db.String(60))
    code_postal = db.Column(db.Integer)
    ville = db.Column(db.String(60))
    pays = db.Column(db.String(60))
    departement_id = db.Column(db.Integer, db.ForeignKey('departement.id'))
    is_superadmin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return 'administrateur.' + str(self.id)

    def __repr__(self):
        return '[Administrateur: {}]'.format(self.nom_admin)


class Etudiant(UserMixin, db.Model):
    """
    Create an Employee table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'etudiant'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(60))
    nom_etud = db.Column(db.String(60), index=True)
    prenom_etud = db.Column(db.String(60), index=True)
    num_etud = db.Column(db.String(60), index=True)
    sexe_etud = db.Column(db.String(60), index=True)
    date_naissance = db.Column(db.Date(), index=True)
    email = db.Column(db.String(60), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    adresse = db.Column(db.String(60))
    code_postal = db.Column(db.Integer)
    ville = db.Column(db.String(60))
    pays = db.Column(db.String(60))
    formation_id = db.Column(db.Integer, db.ForeignKey('formation.id'))

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Etudiant: {}>'.format(self.nom_etud)

    def get_id(self):
        return 'etudiant.' + str(self.id)


class Professeur(UserMixin, db.Model):
    """
    Create an Employee table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'professeur'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(60))
    nom_prof = db.Column(db.String(60), index=True)
    prenom_prof = db.Column(db.String(60), index=True)
    sexe_prof = db.Column(db.String(60), index=True)
    date_naissance = db.Column(db.Date(), index=True)
    email = db.Column(db.String(60), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    adresse = db.Column(db.String(60))
    code_postal = db.Column(db.Integer)
    ville = db.Column(db.String(60))
    pays = db.Column(db.String(60))
    matiere = db.relationship('Matiere', backref='professeur',
                              lazy='dynamic')

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return 'professeur.' + str(self.id)

    def __repr__(self):
        return '[Professeur : {}]'.format(self.nom_prof + ' ' + self.prenom_prof)


class Announce(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'annonce'

    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(200))
    contenu = db.Column(db.String(1000))
    date = db.Column(db.Date())
    matiere_id = db.Column(db.Integer, db.ForeignKey('matiere.id'))
    formation_id = db.Column(db.Integer, db.ForeignKey('formation.id'))

    def __repr__(self):
        return '[Announce: {}]'.format(self.titre)


class Cours(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'cours'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(200))
    titre = db.Column(db.String(500))
    description = db.Column(db.String(200))
    fichier = db.Column(db.String(200))
    date = db.Column(db.Date())
    matiere_id = db.Column(db.Integer, db.ForeignKey('matiere.id'))

    def __repr__(self):
        return '[Cours: {}]'.format(self.titre)


class Matiere(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'matiere'

    id = db.Column(db.Integer, primary_key=True)
    label_matiere = db.Column(db.String(200), unique=True)
    description = db.Column(db.String(200))
    formation_id = db.Column(db.Integer, db.ForeignKey('formation.id'))
    professeur_id = db.Column(db.Integer, db.ForeignKey('professeur.id'))
    cours = db.relationship('Cours', backref='matiere',
                            lazy='dynamic')
    announce = db.relationship('Announce', backref='matiere',
                               lazy='dynamic')

    def __repr__(self):
        return '<Matiere: {}>'.format(self.label_matiere)


class Formation(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'formation'

    id = db.Column(db.Integer, primary_key=True)
    label_formation = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    departement_id = db.Column(db.Integer, db.ForeignKey('departement.id'))
    etudiant = db.relationship('Etudiant', backref='formation',
                               lazy='dynamic')
    matiere = db.relationship('Matiere', backref='formation',
                              lazy='dynamic')
    announce = db.relationship('Announce', backref='formation',
                               lazy='dynamic')

    def __repr__(self):
        return '[Formation: {}]'.format(self.label_formation)


class Departement(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'departement'

    id = db.Column(db.Integer, primary_key=True)
    label_departement = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    administrateur = db.relationship('Administrateur', backref='departement',
                                     lazy='dynamic')
    formation = db.relationship('Formation', backref='departement',
                                lazy='dynamic')

    def __repr__(self):
        return '[Departement: {}]'.format(self.label_departement)
