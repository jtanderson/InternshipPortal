from flask_seeder import Seeder
from api.models import db, ContactFormMessage


class ContactFormMessagesSeeder(Seeder):
    """
    This is the seeder for contact form messages.
    No other models will be affected by this.
    """

    # run() will be called by Flask-Seeder
    def run(self):
        messages = [
            {
                'name': 'Meg Finnegan',
                'email': 'mfinnegan1@gulls.salisbury.edu',
                'message': 'This should work.',
                'was_seen': False,

            }
        ]
        for message in messages:
            db.session.add(ContactFormMessage(**message))
        db.session.commit()
