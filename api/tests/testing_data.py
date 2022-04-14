# Justin Ventura

'''
This module contains testing data for all tests
'''

# Python imports:
import hashlib


# For hashing passwords:
def hash(password): return hashlib.sha256(password.encode()).hexdigest()


# User information:
usersInfo = [
    {
        'username': 'jventura3',
        'email': 'jventura3@gulls.salisbury.edu',
        'password': hash('justinventura426'),
        'is_admin': True
    },
    {
        'username': 'joemomma4',
        'email': 'joemomma4@gulls.salisbury.edu',
        'password': hash('password2'),
        'is_admin': False
    },
    {
        'username': 'joejoejoe',
        'email': None,
        'password': hash('password3'),
        'is_admin': False
    }
]
