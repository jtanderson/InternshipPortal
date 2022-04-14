# Justin Ventura


'''
This module contains the tests for the auth routes.

How to test: `python3 -m pytest -s api/tests/test_auth.py`
OR
`python3 -m pytest -s api/tests/`
'''

# Python imports
import hashlib


# Import for the test app:
from conftest import create_test_app
from testing_data import usersInfo


# We will need literally everything from models:
from api.models import *


# -----------------------------------------------------------------
#                        UsersModel Tests
# -----------------------------------------------------------------

# For hashing passwords:
def hash(password): return hashlib.sha256(password.encode()).hexdigest()


# Add a user to the database:
def add_user_to_database(userInfo):
    '''
    This helper function adds a user to the database.

    userInfo is a dictionary with the following keys:
    'username', 'email', 'password'
    '''
    db.session.add(UsersModel(**userInfo))
    db.session.commit()


# Test that users can be added to the database correctly:
def test_users_model_create(client):
    '''
    This test checks that the UsersModel can be created.
    '''
    with create_test_app().app_context():
        for userInfo in usersInfo:
            add_user_to_database(userInfo)

        for userInfo in usersInfo:
            user = UsersModel.query.filter_by(
                username=userInfo['username']).first()

            # Check that the user was created correctly:
            username_fail_msg = f'{userInfo["username"]} not found in db'
            email_fail_msg = f'{userInfo["email"]} doesn\'t match in db'
            password_fail_msg = f'{userInfo["password"]} doesn\'t match in db'
            admin_fail_msg = f'{userInfo["is_admin"]} doesn\'t match in db'

            # Tests:
            assert user.username == userInfo['username'], username_fail_msg
            assert user.email == userInfo['email'], email_fail_msg
            assert user.password == hash(
                userInfo['password']), password_fail_msg
            assert user.is_admin == userInfo['is_admin'], admin_fail_msg
