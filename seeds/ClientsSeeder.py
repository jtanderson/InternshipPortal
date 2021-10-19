from flask_seeder import Seeder, generator, Faker
from api.models import db, ClientsModel


class ClientsSeeder(Seeder):
    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create User objects
        client1 = ClientsModel(**({
            "client_name": "Amazon",
            "client_info": "Jeff Bezos CEO Nerd's Kingdom",
            "num_listings": 1
        }))
        client2 = ClientsModel(**({
            "client_name": "Google",
            "client_info": "Steals users data.",
            "num_listings": 1
        }))
        client3 = ClientsModel(**({
            "client_name": "Facebook",
            "client_info": "Absolutely selling all of your data.",
            "num_listings": 2
        }))
        print("Adding Client: %s" % client1)
        print("Adding Client: %s" % client2)
        print("Adding Client: %s" % client3)
        db.session.add(client1)
        db.session.add(client2)
        db.session.add(client3)
        db.session.commit()
