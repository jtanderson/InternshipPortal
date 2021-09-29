# Justin Ventura

"""
This module is for the database models.
"""

# Grab the database object from api.
from api import db


# Users Models Class:
class UserModel(db.Model):
    __tablename__ = 'user'

    # Table attributes:
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<User {self.username}>'
