from flask_seeder import Seeder
from api.models import db, UsersModel
import hashlib  # Using for password hashing (SHA-256)


# All seeders inherit from Seeder
class UsersSeeder(Seeder):
    """
    This is the seeder for the users.  This basically just generates
    data for admins at this point.
    """

    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create User objects

        admins = [
            {
                'username': 'jventura3',
                'email': 'jventura3@gulls.salisbury.edu',
                'password': self.password_hash('justinventura425'),
                'is_admin': True
            },
            {
                'username': 'jduncan5',
                'email': 'jduncan5@gulls.salisbury.edu',
                'password': self.password_hash('jacobduncan425'),
                'is_admin': True
            },
            {
                'username': 'bmason3',
                'email': 'bmason3@gulls.salisbury.edu',
                'password': self.password_hash('blainemason425'),
                'is_admin': True
            },
            {
                'username': 'jtanderson',
                'email': 'jtanderson@gulls.salisbury.edu',
                'password': self.password_hash('joeanderson425'),
                'is_admin': True
            }
        ]
        for admin in admins:
            db.session.add(UsersModel(**admin))
        db.session.commit()

    @staticmethod
    def password_hash(password: str):
        """Returns the hashed password"""
        return hashlib.sha256(password.encode()).hexdigest()
