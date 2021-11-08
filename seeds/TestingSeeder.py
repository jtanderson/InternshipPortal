# Justin Ventura

from flask_seeder import Seeder
from api.models import db, ClientsModel, UsersModel, ListingsModel
import hashlib

"""
This is a temporary seeding file for my local test.
"""


class TestSeeder(Seeder):

    def run(self):
        for admin in self.create_admins():
            db.session.add(UsersModel(**admin))

        for client in self.create_clients():
            db.session.add(ClientsModel(**client))

        for listing in self.create_listings():
            db.session.add(ListingsModel(**listing))

        db.session.commit()

    def create_admins(self):
        return [
            {
             'username': 'jventura3',
             'email': 'jventura3@gulls.salisbury.edu',
             'password': self.password_hash('joe momma'),
             'is_admin': True
            },
            {
             'username': 'jduncan5',
             'email': 'jduncan5@gulls.salisbury.edu',
             'password': self.password_hash('valorant'),
             'is_admin': True
            },
            {
             'username': 'bmason3',
             'email': 'bmason3@gulls.salisbury.edu',
             'password': self.password_hash('lapras'),
             'is_admin': True
            },
            {
             'username': 'jtanderson',
             'email': 'jtanderson@gulls.salisbury.edu',
             'password': self.password_hash('noob'),
             'is_admin': False
            }
        ]

    def create_clients(self):
        return [
            {
                'client_name': 'Amazon',
                'client_addr': '601 New Jersey Ave NW Suite 420,\
                                Washington, DC 20001',
                'client_email': 'hr@amazon.com'
            },
            {
                'client_name': 'Google Inc.',
                'client_addr': '1600 Amphitheatre Pkwy, Mountain\
                                View, CA 94043',
                'client_email': 'sundar_pichai@google.com'
            },
            {
                'client_name': 'Joe Nanderson Inc.',
                'client_addr': '169 Joe Ave, Salisbury, MD 21801',
                'client_email': 'joe_nand@salisbury.edu'
            },
            {
                'client_name': 'SU Department of Computer Science',
                'client_addr': '1101 Camden Ave, Salisbury, MD 21801',
                'client_email': 'giulia_franchi@salisbury.edu'
            }
        ]

    def create_listings(self):
        return [
            {
                'client_id': 1,
                'position': 'Summer 2022 SDE Intern',
                'pos_responsibility': '12-week 40hr internship.',
                'min_qualifications': 'Be good at coding',
                'pref_qualifications': 'Be a strong leader',
                'additional_info': None,
                'status': 'active'
                
            },
            {
                'client_id': 2,
                'position': 'Google Summer 2022 Intern',
                'pos_responsibility': 'Summer internship.',
                'min_qualifications': 'Be good at coding',
                'pref_qualifications': 'Must love stealing data',
                'additional_info': 'Google epic',
                'status': 'active'
            },
            {
                'client_id': 3,
                'position': 'Joe\'s Research Slave',
                'pos_responsibility': 'Do what joe doesnt wanna do',
                'min_qualifications': 'Statistics and Probability',
                'pref_qualifications': 'Machine Learning',
                'additional_info': 'Roll 4-sided die often.',
                'status': 'active'
            },
            {
                'client_id': 4,
                'position': 'Robotics Research',
                'pos_responsibility': 'Build robots of mass destruction',
                'min_qualifications': 'Like destruction',
                'pref_qualifications': 'Experience with weapon building',
                'additional_info': 'Totally NOT illegal',
                'status': 'rejected'
            },
            {
                'client_id': 1,
                'position': 'Summer 2021 SDE Intern',
                'pos_responsibility': '12-week 40hr internship.',
                'min_qualifications': 'Be good at coding',
                'pref_qualifications': 'Be a strong leader',
                'additional_info': None,
                'status': 'inactive'
            },
            {
                'client_id': 4,
                'position': 'Dummy positions',
                'pos_responsibility': 'Stuff',
                'min_qualifications': 'Nothing',
                'pref_qualifications': 'Code',
                'additional_info': 'Nothing',
                'status': 'inactive'
            },
            {
                'client_id': 3,
                'position': 'Dummy positions',
                'pos_responsibility': 'Stuff',
                'min_qualifications': 'Nothing',
                'pref_qualifications': 'Code',
                'additional_info': 'Nothing',
                'status': 'pending'
            },
            {
                'client_id': 2,
                'position': 'Dummy positions',
                'pos_responsibility': 'Stuff',
                'min_qualifications': 'Nothing',
                'pref_qualifications': 'Code',
                'additional_info': 'Nothing',
                'status': 'active'
            },
        ]

    @staticmethod
    def password_hash(password: str):
        """Returns the hashed password"""
        return hashlib.sha256(password.encode()).hexdigest()
