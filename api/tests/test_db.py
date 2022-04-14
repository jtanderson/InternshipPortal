# Justin Ventura


'''
This module contains the tests for the auth routes.

How to test: `python3 -m pytest -s api/tests/test_auth.py`
OR
`python3 -m pytest -s api/tests/`
'''


# Import for the test app:
from testing_data import hash, usersInfo, clientsInfo


# We will need literally everything from models:
from api.models import *


# -----------------------------------------------------------------
#                        UsersModel Tests
# -----------------------------------------------------------------


# Add a user to the database:
def add_user_to_database(userInfo):
    '''
    This helper function adds a user to the database.

    userInfo is a dictionary with the following keys:
    'username', 'email', 'password'
    '''
    user = UsersModel(**userInfo)
    db.session.add(user)
    db.session.commit()


# Test that users can be added to the database correctly:
def test_users_model_create(client):
    '''
    This test checks that the UsersModel can be created.
    '''
    # with create_test_app().app_context():
    for userInfo in usersInfo[1:]:
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
        assert user.password == userInfo['password'], password_fail_msg
        assert user.is_admin == userInfo['is_admin'], admin_fail_msg


# Test that users can be updated from the database correctly:
def test_users_model_update(client):
    '''
    This test checks that the UsersModel can be updated.

    Assumes that the database is already populated.
    Relies on 'joejoejoe' being in the database.
    '''

    # Grab the user to be updated
    user = UsersModel.query.filter_by(username='joejoejoe').first()
    assert user is not None, 'joejoejoe not found in db'

    # Update the password:
    user.password = hash('new_password')
    db.session.commit()

    # Check that the password was updated:
    user = UsersModel.query.filter_by(username='joejoejoe').first()
    assert user.password == hash('new_password'), 'Password not updated'


# -----------------------------------------------------------------
#                        ClientsModel Tests
# -----------------------------------------------------------------


# Add a client to the database:
def add_client_to_database(clientInfo):
    '''
    This helper function adds a client to the database.

    clientInfo is a dictionary with the following keys:
    'name', 'address', 'email'
    '''
    client = ClientsModel(**clientInfo)
    db.session.add(client)
    db.session.commit()


# Test that clients can be added to the database correctly:
def test_clients_model_create(client):
    '''
    This test checks that the ClientsModel can be created.
    '''
    # with create_test_app().app_context():
    for clientInfo in clientsInfo:
        add_client_to_database(clientInfo)

    for clientInfo in clientsInfo:
        client = ClientsModel.query.filter_by(
            name=clientInfo['name']).first()

        # Check that the client was created correctly:
        name_fail_msg = f'{clientInfo["name"]} not found in db'
        address_fail_msg = f'{clientInfo["address"]} doesn\'t match in db'
        email_fail_msg = f'{clientInfo["email"]} doesn\'t match in db'

        # Tests:
        assert client.name == clientInfo['name'], name_fail_msg
        assert client.address == clientInfo['address'], address_fail_msg
        assert client.email == clientInfo['email'], email_fail_msg
