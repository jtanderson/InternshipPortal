# Justin Ventura


'''
This module is for configuring the testing client.
'''


# Python imports:
import pytest

# Import for env file:
from os.path import join, dirname
from dotenv import load_dotenv

# Import the app creation method:
from api import create_app

# Load in the env file with variables:
dotenv_path = join(dirname(__file__), '../../.env')
load_dotenv(dotenv_path)


# This is to create the test app as client:
@pytest.fixture
def client():
    '''Create the test client'''
    app = create_app()
    # app.config['TESTING'] = True
    app.app_context().push()
    return app.test_client()
