# Justin Ventura
import json
import requests


def login(client, username, password):
    data = {
        'username': username,
        'password': password
    }
    print(data)
    return client.post('/login-submit', json=data, follow_redirects=True)


def logout(client):
    return client.get('/logout', follow_redirects=True)


def test_login_submit(client):
    from global_testing_seeder import UsersSeeder
    seeder = UsersSeeder()
    seeder.run()
    rv = login(client, 'jventura3', 'justinventura426')
    # data = json.loads(json.dumps({
    #     'username': 'jventura3',
    #     'password': 'justinventura426'
    # }))
    # req = requests.post('http://localhost:5000/login-submit', json={
    #     'username': 'jventura3',
    #     'password': 'justinventura426'
    # })
    assert b'admin.html' in rv.data
