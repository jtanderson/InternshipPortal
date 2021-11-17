from flask_seeder import Seeder
from api.models import db, ListingsModel


class ListingsSeeder(Seeder):
    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create User objects
        listing1 = ListingsModel(**({
            "client_id": 1,
            "position": "Senior Software Engineer",
            "pos_responsibility": "Do Software Engineering",
            "min_qualifications": "PhD in Computer Science",
            "pref_qualifications": "PhD in Computer Science and 10 years of experience",
            "additional_info": "Must be smart",
            "duration": "12",
            "app_open": "11/09/2021",
            "app_close": "03/21/2022",
        }))
        listing2 = ListingsModel(**({
            "client_id": 2,
            "position": "Junior Software Engineer",
            "pos_responsibility": "Do some Software Engineering",
            "min_qualifications": "Bachelor in Computer Science",
            "pref_qualifications": "Be Jacob Duncan and 10 years of experience",
            "additional_info": "Must be smart and know Kelsey",
            "duration": "6",
            "app_open": "01/01/2022",
            "app_close": "03/14/2022",
        }))
        listing3 = ListingsModel(**({
            "client_id": 3,
            "position": "The Zuck's Foot Rest",
            "pos_responsibility": "Reside on all fours and hold up the Zuck's feet.",
            "min_qualifications": "PhD in Computer Science",
            "pref_qualifications": "Have a ton of data with Facebook",
            "additional_info": "Must be smart and know Kelsey",
            "duration": "8",
            "app_open": "01/01/2022",
            "app_close": "05/14/2022",
        }))
        listing4 = ListingsModel(**({
            "client_id": 3,
            "position": "The Zuck's Personal Asssisant",
            "pos_responsibility": "Do everything for the Zuck.",
            "min_qualifications": "PhD in Computer Science",
            "pref_qualifications": "Have a ton of data with Facebook and Instagram",
            "additional_info": "Must be smart and know Kelsey Queso",
            "duration": "4",
            "app_open": "12/10/2021",
            "app_close": "06/13/2022",
        }))
        print("Adding listing: %s" % listing1)
        print("Adding listing: %s" % listing2)
        print("Adding listing: %s" % listing3)
        print("Adding listing: %s" % listing4)
        db.session.add(listing1)
        db.session.add(listing2)
        db.session.add(listing3)
        db.session.add(listing4)
        db.session.commit()

        listings = [
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
                'additional_info': 'Google epic'
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
        for listing in listings:
            db.session.add(ListingsModel(**listing))
        db.session.commit()
