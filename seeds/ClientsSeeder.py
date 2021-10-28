from flask_seeder import Seeder
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
        clients = [
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
        for client in clients:
            db.session.add(ClientsModel(**client))
        db.session.commit()
