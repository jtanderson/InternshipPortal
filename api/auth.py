# Internship Portal Web App
# __init__.py for API


"""
Clients: Dr. Joseph Anderson, Dr. Giulia Franchi
Team: Blaine Mason, Jacob Duncan, Justin Ventura, Margaret Finnegan

For now just store API in the __init__.py file, this will change later.
"""


# Flask Imports:
from flask import render_template, Blueprint, request, redirect, url_for


# Create auth blueprint:
auth = Blueprint('auth', __name__)

# ------------------------------------------------------------------------
#       ADMIN PAGE ROUTES: these routes are all for admin page.
# ------------------------------------------------------------------------

@auth.route('/login', methods=['GET'])
def login():
    """Admin login page.
    """
    return render_template("login.html", page_title="Admin Login", jinja_data="Hello from Jinja")


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.POST.get('email')
    name = request.POST.get('name')
    password = request.POST.get('password')

    # IMPLEMENT THE FOLLOWING ONCE WE HAVE DB MODEL:

    # user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    # if user: # if a user is found, we want to redirect back to signup page so user can try again
    #     return redirect(url_for('auth.signup'))

    # # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    # new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # # add the new user to the database
    # db.session.add(new_user)
    # db.session.commit()

    return redirect(url_for('auth.login'))
