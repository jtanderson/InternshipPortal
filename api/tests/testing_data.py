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


# Client information:
clientInfo = [
    {
        'client_name': 'Amazon',
        'client_addr': '601 New Jersey Ave NW Suite 420,' +
        'Washington, DC 20001',
        'client_email': 'hr@amazon.com'
    },
    {
        'client_name': 'Google Inc.',
        'client_addr': '1600 Amphitheatre Pkwy, Mountain' +
        'View, CA 94043',
        'client_email': 'sundar_pichai@google.com'
    },
    {
        'client_name': 'Facebook Inc.',
        'client_addr': '1 Hacker Way, Menlo Park, CA 94025',
        'client_email': 'zuck@facebook.com'
    },
    {
        'client_name': 'SU Department of Computer Science',
        'client_addr': '1101 Camden Ave, Salisbury, MD 21801',
        'client_email': 'giulia_franchi@salisbury.edu'
    }
]
