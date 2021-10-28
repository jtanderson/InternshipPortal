from flask_seeder import Seeder, generator, Faker
from api.models import db, UsersModel
import hashlib  # Using for password hashing (SHA-256)


# All seeders inherit from Seeder
class UsersSeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create User objects
        faker = Faker(
            cls=UsersModel,
            init={
                "username": generator.Name(),
                "email": generator.Email(),
                "password": hashlib.sha256("password".encode()).hexdigest(),
            }
        )

        # Create 5 users
        for user in faker.create(5):
            print("Adding user: %s" % user)
            db.session.add(user)
        db.session.commit()

        admins = [
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
             'is_admin': True
            }
        ]
        for admin in admins():
            db.session.add(UsersModel(**admin))
        db.session.commit()

    @staticmethod
    def password_hash(password: str):
        """Returns the hashed password"""
        return hashlib.sha256(password.encode()).hexdigest()
