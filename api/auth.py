# Internship Portal Web App
# auth.py for API


"""
Clients: Dr. Joseph Anderson, Dr. Giulia Franchi
Team: Blaine Mason, Jacob Duncan, Justin Ventura, Margaret Finnegan
"""


# Flask Imports:
from flask import render_template, Blueprint, request, redirect, url_for


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
    """
    data = request.json
    username = data['username']
    password = data['password']
    print(f'Username: {username}, Password: {password}')

    return redirect(url_for('views.root'))
