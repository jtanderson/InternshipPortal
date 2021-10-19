from flask_seeder import Seeder, generator, Faker
from api.models import db, ClientsModel


class ClientsSeeder(Seeder):
    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create User objects
        client1 = ClientsModel(**({
            "client_name": "Amazon",
            "client_addr": "123 amazon ln",
            "client_email": "jbezos1234@amazon.com"
        }))
        client2 = ClientsModel(**({
            "client_name": "Google",
            "client_addr": "123 google ln",
            "client_email": "google@google.com"
        }))
        client3 = ClientsModel(**({
            "client_name": "Facebook",
            "client_addr": "123 facebook ln",
            "client_email": "dazuck@facebook.com"
        }))
        print("Adding Client: %s" % client1)
        print("Adding Client: %s" % client2)
        print("Adding Client: %s" % client3)
        db.session.add(client1)
        db.session.add(client2)
        db.session.add(client3)
        db.session.commit()
