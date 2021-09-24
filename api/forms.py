# Internship Portal Web App
# forms.py for API


"""
Clients: Dr. Joseph Anderson, Dr. Giulia Franchi
Team: Blaine Mason, Jacob Duncan, Justin Ventura, Margaret Finnegan

For now just store API in the forms.py file, this will change later.
"""

from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField
from flask import Blueprint, request, redirect, url_for

# Create auth blueprint:
forms = Blueprint('forms', __name__)


# Contact Form Class:
class ContactForm(Form):
    name = TextField('Name')
    email = TextField('Email')
    message = TextField('Message')
    submit = SubmitField('Send')


# Route for submitting forms:
@forms.route('\contact-submit', methods=['POST'])
def contact_submit():
    pass
