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
from .models import db
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder

# Import for env file:
from os.path import join, dirname
from dotenv import load_dotenv

# To timeout sessions
from datetime import timedelta

# Load in the env file with variables:
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Creates Flask app  with some configurations:
app = Flask(__name__,
            static_folder='../static',
            template_folder='../templates')


# Creates app:
def create_app():
    """
    This is the function for creating the flask app along with
    all of the configurations and blueprints.
    """
    # Initial configurations:
    CORS(app)
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

    # How long do we want sessions to last, 30min? 1hr?
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

    myusername = os.environ.get("DB_USERNAME")
    mypassword = os.environ.get("DB_PASSWORD")
    myaddress = os.environ.get("DB_ADDRESS")
    myport = os.environ.get("DB_PORT")
    mydbname = os.environ.get("DB_DBNAME")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{myusername}:' +\
        f'{mypassword}@{myaddress}:{myport}/{mydbname}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # Init app with database from models.
    db.init_app(app)
    print("[PostgreSQL]: Connection successful")

    # Wrap SQLAlchemy ORM to the app for database.
    Migrate(app, db)

    seeder = FlaskSeeder()
    seeder.init_app(app, db)

    # Blueprint for views routes in the app:
    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint)

    # Blueprint for auth routes in the app:
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Blueprint for routes routes in the app:
    from .routes import routes as routes_blueprint
    app.register_blueprint(routes_blueprint)

    # Blueprint for form routes in the app:
    from .forms import forms as forms_blueprint
    app.register_blueprint(forms_blueprint)

    # Blueprint for form routes in the app:
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    # Return the app to be run in main.py:
    return app
