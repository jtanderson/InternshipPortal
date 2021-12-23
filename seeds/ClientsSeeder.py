from flask_seeder import Seeder
from api.models import db, ClientsModel


class ClientsSeeder(Seeder):
    """
    This is the seeder for clients.
    No other models will be affected by this.
    """

    # run() will be called by Flask-Seeder
    def run(self):
        clients = [
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
        for client in clients:
            db.session.add(ClientsModel(**client))
        db.session.commit()
