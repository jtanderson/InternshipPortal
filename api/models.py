# Justin Ventura

"""
This module is for the database models.
"""

# Imports for database ORM:
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# Import constants:
from .constants import MAX_CREDENTIAL_LEN, DEFAULT_LISTING_STATUS as DEFAULT

# Prepare for wrapping:
db = SQLAlchemy()


# Users Models Class:
class UsersModel(db.Model, SerializerMixin):
    """This is the model for users in the database.

    For now, this only contains admin information.
    """
    __tablename__ = 'users'

    # Serialization rules:
    serialize_only = ('id', 'username', 'email', 'is_admin')
    serialize_rules = ('-password')

    # Table attributes:
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(MAX_CREDENTIAL_LEN))
    email = db.Column(db.String(MAX_CREDENTIAL_LEN))
    password = db.Column(db.String(MAX_CREDENTIAL_LEN))
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, username: str, email: str, password: str,
                 is_admin: bool = False):
        self.username = username
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return f'<User {self.username}>'


# Clients Models Class:
class ClientsModel(db.Model):
    __tablename__ = 'clients'

    # Serialization rules:
    serialize_only = ('id', 'client_name', 'client_addr', 'client_email')

    # Table attributes:
    id = db.Column(db.Integer, primary_key=True)

    # General Client information:
    client_name = db.Column(db.String(MAX_CREDENTIAL_LEN))
    client_addr = db.Column(db.String(MAX_CREDENTIAL_LEN))
    client_email = db.Column(db.String(MAX_CREDENTIAL_LEN))

    def __init__(self, client_name: str, client_addr: str,
                 client_email: str = None):
        self.client_name = client_name
        self.client_addr = client_addr
        self.client_email = client_email

    def __repr__(self):
        return f'<Client ({self.id}) {self.client_name}>'


# Listings Models Class:
class ListingsModel(db.Model, SerializerMixin):
    __tablename__ = 'listings'

    # Serialization rules:
    serialize_only = ('id', 'client_id', 'position', 'pos_responsibility',
                      'min_qualifications', 'pref_qualifications',
                      'additional_info', 'status', 'starred')

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

    # Starred: True or False
    starred = db.Column(db.Boolean, default=False)

    def __init__(self, client_id: int, position: str, pos_responsibility: str,
                 min_qualifications: str, pref_qualifications: str,
                 additional_info: str = None, status: str = DEFAULT,
                 starred: bool = False):
        self.client_id = client_id
        self.position = position
        self.pos_responsibility = pos_responsibility
        self.min_qualifications = min_qualifications
        self.pref_qualifications = pref_qualifications
        self.additional_info = additional_info
        self.status = status
        self.starred = starred

    def __repr__(self):
        return f'<Listing {self.id}: {self.position}>'
