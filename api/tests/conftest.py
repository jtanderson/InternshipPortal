# Justin Ventura


'''
This module is for configuring the testing client.

May need some trimming.
'''


# Python imports:
import os
import pytest

# Flask Imports:
from flask import Flask
from flask_cors import CORS

# Imports for database and migrations:
from api.models import db
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder

# Import for env file:
from os.path import join, dirname
from dotenv import load_dotenv

# DO we need this?
from api import create_app

# Database imports:
from api.models import db

# Load in the env file with variables:
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


# This is to create the test app as client:
@pytest.fixture
def client():
    '''Create the test client'''
    # app = create_app()
    # # db_fd, app.config['DATABASE'] = tempfile.mkstemp()

    # app = create_test_app()

    # with app.test_client() as client:
    #     with app.app_context():
    #         db.init_app(app)
    #     yield client
    app = create_test_app()
    app.app_context().push()
    return app.test_client()

    # # os.close(db_fd)
    # # os.unlink(app.config['DATABASE'])


# Create the test app client:
def create_test_app():
    '''Create the test app'''
    # Creates Flask app  with some configurations:
    app = Flask(__name__,
                static_folder='../static',
                template_folder='../templates')

    CORS(app)
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
    app.config['TESTING'] = True

    # Check if we need this:
    # app.config.from_pyfile(config_filename)
    initialize_extensions(app)
    register_blueprints(app)
    return app


# This is basically for the db:
def initialize_extensions(app):
    '''Initialize Flask extensions.'''
    # TODO: This is for the database:
    # myusername = os.environ.get("DB_USERNAME")
    # mypassword = os.environ.get("DB_PASSWORD")
    # myaddress = os.environ.get("DB_ADDRESS")
    # myport = os.environ.get("DB_PORT")
    # mydbname = os.environ.get("DB_DBNAME")
    myusername = "justinventura"
    mypassword = "justinventura"
    myaddress = "localhost"
    myport = 5432
    mydbname = "internship_portal"
    app.config['SECRET_KEY'] = "secret"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{myusername}:' +\
        f'{mypassword}@{myaddress}:{myport}/{mydbname}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    Migrate(app, db)
    seeder = FlaskSeeder()
    seeder.init_app(app, db)


# This is to make sure the blueprints are registered to app:
def register_blueprints(app):
    '''Register all blueprints from all modules in api'''
    # Blueprint for views routes in the app:
    from api.views import views as views_blueprint
    app.register_blueprint(views_blueprint)

    # Blueprint for auth routes in the app:
    from api.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Blueprint for routes routes in the app:
    from api.routes import routes as routes_blueprint
    app.register_blueprint(routes_blueprint)

    # Blueprint for form routes in the app:
    from api.forms import forms as forms_blueprint
    app.register_blueprint(forms_blueprint)

    # Blueprint for form routes in the app:
    from api.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)


@pytest.fixture()
def runner(app):
    '''A test runner for the app's Click commands.'''
    return app.test_cli_runner()
