from flask_seeder import Seeder, generator, Faker
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
            "additional_info": "Must be smart"
        }))
        listing2 = ListingsModel(**({
            "client_id": 2,
            "position": "Junior Software Engineer",
            "pos_responsibility": "Do some Software Engineering",
            "min_qualifications": "Bachelor in Computer Science",
            "pref_qualifications": "Be Jacob Duncan and 10 years of experience",
            "additional_info": "Must be smart and know Kelsey"
        }))
        listing3 = ListingsModel(**({
            "client_id": 3,
            "position": "The Zuck's Foot Rest",
            "pos_responsibility": "Reside on all fours and hold up the Zuck's feet.",
            "min_qualifications": "PhD in Computer Science",
            "pref_qualifications": "Have a ton of data with Facebook",
            "additional_info": "Must be smart and know Kelsey"
        }))
        listing4 = ListingsModel(**({
            "client_id": 3,
            "position": "The Zuck's Personal Asssisant",
            "pos_responsibility": "Do everything for the Zuck.",
            "min_qualifications": "PhD in Computer Science",
            "pref_qualifications": "Have a ton of data with Facebook and Instagram",
            "additional_info": "Must be smart and know Kelsey Queso"
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

