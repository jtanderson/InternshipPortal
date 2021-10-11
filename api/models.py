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
    """This is the model for users in the database.

    For now, this only contains admin information.
    """
    __tablename__ = 'users'

    # Table attributes:
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(MAX_CREDENTIAL_LEN))
    email = db.Column(db.String(MAX_CREDENTIAL_LEN))
    password = db.Column(db.String(MAX_CREDENTIAL_LEN))
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, username: str, email: str, password: str,
                is_admin: bool=False):
        self.username = username
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return f'<User {self.username}>'


# Clients Models Class:
class ClientsModel(db.Model):
    __tablename__ = 'clients'

    # Table attributes:
    id = db.Column(db.Integer, primary_key=True)

    # General Client information:
    client_name = db.Column(db.String(MAX_CREDENTIAL_LEN))
    client_addr = db.Column(db.String(MAX_CREDENTIAL_LEN))
    client_email = db.Column(db.String(MAX_CREDENTIAL_LEN))
    client_phone = db.Column(db.String(MAX_CREDENTIAL_LEN))

    def __init__(self, client_name: str, client_addr: str, client_email: str,
                client_phone: str):
        self.client_name = client_name
        self.client_addr = client_addr
        self.client_email = client_email
        self.client_phone = client_phone

    def __repr__(self):
        return f'<Client ({self.id}) {self.client_name}>'


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

    # Status: Pending, Active, Rejected
    status = db.Column(db.String(MAX_CREDENTIAL_LEN))
    
    def __init__(self, client_id: int, position: str, pos_responsibility: str,
                min_qualifications: str, pref_qualifications: str, 
                additional_info: str, status: str):
        self.client_id = client_id
        self.position = position
        self.pos_responsibility = pos_responsibility
        self.min_qualifications = min_qualifications
        self.pref_qualifications = pref_qualifications
        self.additional_info = additional_info
        self.status = status

    def __repr__(self):
        return f'<Listing {self.id}: {self.position}>'
