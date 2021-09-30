# Internship Portal Web App
# auth.py for API


"""
Clients: Dr. Joseph Anderson, Dr. Giulia Franchi
Team: Blaine Mason, Jacob Duncan, Justin Ventura, Margaret Finnegan
"""


# Flask Imports:
from flask import Blueprint, request

# Helper imports:
from .helpers import correct_login
import hashlib  # Using for password hashing (SHA-256)


# Create auth blueprint:
auth = Blueprint('auth', __name__)

# ------------------------------------------------------------------------
#          AUTH ROUTES: these routes are all for authorization
# ------------------------------------------------------------------------


# Handles the login form post requests:
# TODO: handle login correctly.
@auth.route('/login-submit', methods=['POST'])
def login_submit():
    """Login submission route.
    This function handles the login submission attempts.

    Expects json from post request with the form:
    { 
        "username": <username>,
        "password": <password>
    }

    If login success, returns 'admin.html' and 200 status.
    Else, returns error message.
    """
    response = dict()
    login_data = request.json
    username, password = login_data.values()

    # Hash password with SHA-256.
    pass_hash = hashlib.sha256(password.encode()).hexdigest()

    # For logging:
    print(f'username: {username}, password: {pass_hash}')

    # Check against the database for correct/incorrect login info:
    if correct_login(username=username, password=pass_hash):
        response['redirect'] = 'admin.html'
    else:
        response['err_msg'] = 'Invalid username or password.'

    # Status code 200.
    return response, 200
