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
class UserModel(db.Model):
    __tablename__ = 'user'

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


# Companies Models Class:
class CompaniesModel(db.Model):
    __tablename__ = 'companies'

    # Table attributes:
    company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(MAX_CREDENTIAL_LEN))
    company_info = db.Column(db.Text)
    num_listings = db.Column(db.Integer)

    def __init__(self, c_id: int, c_name: str, num_listings: int):
        self.c_id = c_id
        self.c_name = c_name
        self.num_listings = num_listings

    def __init__(self):
        return f'<Company {self.c_name}>'


# Listings Models Class:
class ListingsModel(db.Model):
    __tablename__ = 'listings'

    # Table attributes:
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.company_id'))
    position = db.Column(db.String(MAX_CREDENTIAL_LEN))
    pos_responsibility = db.Column(db.Text)
    min_qualifictions = db.Column(db.Text)
    pref_qualifictions = db.Column(db.Text)
    additional_info = db.Column(db.Text)
    
    def __init__(self, company_id: int, position: str, pos_responsibility: str,
                min_qualifictions: str, pref_qualifictions: str, 
                additional_info: str):
        self.company_id = company_id
        self.position = position
        self.pos_responsibility = pos_responsibility
        self.min_qualifictions = min_qualifictions
        self.pref_qualifictions = pref_qualifictions
        self.additional_info = additional_info
    
    def __init__(self):
        return f'<Listing {self.id}: {self.position}>'
