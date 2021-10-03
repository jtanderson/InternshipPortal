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
