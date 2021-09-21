# Internship Portal Web App
# __init__.py for API


"""
Clients: Dr. Joseph Anderson, Dr. Giulia Franchi
Team: Blaine Mason, Jacob Duncan, Justin Ventura, Margaret Finnegan

For now just store API in the __init__.py file, this will change later.
"""


# Flask Imports:
from flask import Flask, render_template, request
from flask_cors import CORS


# Creates Flask app  with some configurations:
app = Flask(__name__,
            static_folder='../web/static',
            template_folder='../web/templates')


# Creates app:
def create_app():
    # Initial configurations:
    CORS(app)
    app.config['SECRET_KEY'] = ''

    # Blueprint for auth routes in the app:
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Return the app to be run in main.py:
    return app


# ------------------------------------------------------------------------
#                                 ROUTES
# ------------------------------------------------------------------------

# Root page route: 
@app.route('/')
def root():
    """Root page view route.
    This function runs whenever the root page (url below) is requested.
        ex) -> localhost:5000/
    Returns the root page: which renders index.html (landing page)
    """
    return render_template("index.html", page_title="Internship Web Portal Homepage")


# Admin view route:
@app.route('/admin')
def admin():
    """Admin page view route.
    This function runs whenver the admin page ('/admin') is requested.
        ex) -> localhost:5000/admin
    Returns the admin page: which renders admin.html (admin dashboard)
    """
    return render_template("admin.html")
