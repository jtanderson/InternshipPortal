# Justin Ventura

"""
This module contains functions used to help out with the app.
"""

# Database functinality imports
from .models import UserModel


# TODO: check database here.
# Check credentials against the database:
def correct_login(username: str, password: str) -> bool:

    # Grab the admin from the database:
    admin = UserModel.query.filter_by(username=username).first()

    # Pythonic ternary babyyyyy
    return False if not admin or password != admin.password else True
