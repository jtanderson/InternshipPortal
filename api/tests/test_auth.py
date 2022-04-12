# Justin Ventura
import json
import requests
import hashlib

# Imports for the database:
from api.models import db, UsersModel

# Imports for the test app:
from conftest import create_test_app


# Helper to login
def login(client, username, password):
    data = {
        'username': username,
        'password': password
    }
    return client.post('/login-submit',
                       json=data,
                       follow_redirects=True)


# Helper to logout:
def logout(client):
    return client.get('/logout',
                      follow_redirects=True)


# Unit test for login/logout functionality:
def test_login_logout(client):
    '''
    This test checks that the login form works correctly.

    Routes:
        /login-submit
        /logout
    '''
    with create_test_app().app_context():
        user = UsersModel(username='jventura3',
                          email='jventura3@gulls.salisbury.edu',
                          password=hashlib.sha256(
                              'justinventura426'.encode()).hexdigest(),
                          is_admin=True)
        db.session.add(user)
        db.session.commit()

    # Test that the login form works correctly:
    # ------------------------------ TEST 1 ------------------------------
    valid_login = login(client, 'jventura3', 'justinventura426')
    assert valid_login.status_code == 200, 'Correct login failed.'

    valid_logout = logout(client)
    assert valid_logout.status_code == 200, 'Valid Logout failed.'

    # ------------------------------ TEST 2 -------------------------------
    invalid_login1 = login(client, 'jventura3', 'justinventura')
    invalid_login2 = login(client, 'joemomma', 'justinventura')
    invalid_login3 = login(client, None, 'justinventura')
    invalid_login4 = login(client, 'jventura3', None)

    assert invalid_login1.status_code == 403, 'Invalid password test succeeded.'
    assert invalid_login2.status_code == 403, 'Invalid username test succeeded.'
    assert invalid_login3.status_code == 403, 'Missing username test succeeded.'
    assert invalid_login4.status_code == 403, 'Missing password test succeeded.'

    # ------------------------------ TEST 3 -------------------------------
    invalid_logout = logout(client)
    assert invalid_logout.status_code == 400, 'Invalid logout succeeded.'
