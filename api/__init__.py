# Internship Portal Web App
# __init__.py for API


"""
Clients: Dr. Joseph Anderson, Dr. Giulia Franchi
Team: Blaine Mason, Jacob Duncan, Justin Ventura, Margaret Finnegan

For now just store API in the __init__.py file, this will change later.
"""


# General imports:
import os

# Flask Imports:
from flask import Flask
from flask_cors import CORS

# Imports for database and migrations:
from .models import db, UserModel
from flask_migrate import Migrate

# Import for env file:
from os.path import join, dirname
from dotenv import load_dotenv

# Load in the env file with variables:
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Creates Flask app  with some configurations:
app = Flask(__name__,
            static_folder='../static',
            template_folder='../templates')


# Creates app:
def create_app():
    # Initial configurations:
    CORS(app)
    app.config['SECRET_KEY'] = ''
    
    myusername = os.environ.get("DB_USERNAME")
    mypassword = os.environ.get("DB_PASSWORD")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{myusername}:{mypassword}@localhost:5432/internship_portal'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Init app with database from models.
    db.init_app(app)

    # Wrap SQLAlchemy ORM to the app for database.
    migrate = Migrate(app, db)

    # Blueprint for views routes in the app:
    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint)

    # Blueprint for auth routes in the app:
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Blueprint for form routes in the app:
    from .forms import forms as forms_blueprint
    app.register_blueprint(forms_blueprint)

    # Return the app to be run in main.py:
    return app
