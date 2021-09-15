# Internship Portal Web App
# __init__.py for API


"""
Clients: Dr. Joseph Anderson, Dr. Giulia Franchi
Team: Blaine Mason, Jacob Duncan, Justin Ventura, Margaret Finnegan

For now just store API in the __init__.py file, this will change later.
"""


# Flask Imports:
from flask import Flask
from flask_cors import CORS


# Creates app:
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = 'jenna sleeps on the floor'

    return app


# ------------------------------------------------------------------------
#                                 ROUTES
# ------------------------------------------------------------------------


# Root page route:
@views.route('/')
def home():
    """Root page view route.
    This function runs whenever the root page (url below) is requested.
        ex) -> localhost:5000/
    Returns the root page:
    """
    return '<h1>Internship Portal</h1>'
