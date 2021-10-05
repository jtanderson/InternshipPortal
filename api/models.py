# Justin Ventura

"""
This module is for the database models.
"""

# Imports for database ORM:
from flask_sqlalchemy import SQLAlchemy

# Import constants:
from .constants import MAX_CREDENTIAL_LEN

# Prepare for wrapping:
db = SQLAlchemy()


# Users Models Class:
class UsersModel(db.Model):
    __tablename__ = 'users'

    # Table attributes:
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(MAX_CREDENTIAL_LEN))
    email = db.Column(db.String(MAX_CREDENTIAL_LEN))
    password = db.Column(db.String(MAX_CREDENTIAL_LEN))

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<User {self.username}>'


# Clients Models Class:
class ClientsModel(db.Model):
    __tablename__ = 'clients'

    # Table attributes:
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(MAX_CREDENTIAL_LEN))
    client_info = db.Column(db.Text)
    num_listings = db.Column(db.Integer)

    def __init__(self, client_info: str, c_name: str, num_listings: int):
        self.c_name = c_name
        self.client_info = client_info
        self.num_listings = num_listings

    def __repr__(self):
        return f'<Client {self.c_name}>'


# Listings Models Class:
class ListingsModel(db.Model):
    __tablename__ = 'listings'

    # Table attributes:
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    position = db.Column(db.String(MAX_CREDENTIAL_LEN))
    pos_responsibility = db.Column(db.Text)
    min_qualifications = db.Column(db.Text)
    pref_qualifications = db.Column(db.Text)
    additional_info = db.Column(db.Text)
    
    def __init__(self, client_id: int, position: str, pos_responsibility: str,
                min_qualifications: str, pref_qualifications: str, 
                additional_info: str):
        self.client_id = client_id
        self.position = position
        self.pos_responsibility = pos_responsibility
        self.min_qualifications = min_qualifications
        self.pref_qualifications = pref_qualifications
        self.additional_info = additional_info
    
    def __repr__(self):
        return f'<Listing {self.id}: {self.position}>'
