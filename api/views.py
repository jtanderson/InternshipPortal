# Internship Portal Web App
# views.py for API


"""
Clients: Dr. Joseph Anderson, Dr. Giulia Franchi
Team: Blaine Mason, Jacob Duncan, Justin Ventura, Margaret Finnegan
"""


# Flask Imports:
from flask import render_template, Blueprint, request, redirect, url_for

# Create views blueprint:
views = Blueprint('views', __name__)

# ------------------------------------------------------------------------
#                                 ROUTES
# ------------------------------------------------------------------------

# Root page route: 
@views.route('/')
def root():
    """Root page view route.
    This function runs whenever the root page (url below) is requested.
        ex) -> localhost:5000/
    Returns the root page: which renders index.html (landing page)
    """
    return render_template("index.html", page_title="Internship Web Portal Homepage")


# Admin view route:
@views.route('/admin')
def admin():
    """Admin page view route.
    This function runs whenver the admin page ('/admin') is requested.
        ex) -> localhost:5000/admin
    Returns the admin page: which renders admin.html (admin dashboard)
    """
    return render_template("admin.html", page_title="Admin Dashboard")


# Renders login page for admin:
@views.route('/login', methods=['GET'])
def login():
    """Login page for admin.
    This function runs whenver the login page ('/login') is requested.
        ex) -> localhost:5000/admin
    Returns the login page: which renders login.html (login form)
    """
    return render_template('login.html', page_title='Admin Login')

# Renders contact page for admin:
@views.route('/contact', methods=['GET'])
def contact():
    """Contact page for users.
    This function runs whenver the contact page ('/contact') is requested.
        ex) -> localhost:5000/contact
    Returns the login page: which renders contact.html (contact page)
    """
    return render_template('contact.html', page_title='Contact Us')