# Justin Ventura

"""
This module contains functions used to help out with the app.
"""

# Database functinality imports
from .models import UsersModel


# TODO: check database here.
# Check credentials against the database:
def correct_login(username: str, password: str) -> bool:

    # Grab the admin from the database:
    admin = UsersModel.query.filter_by(username=username).first()

    # Must be in database, be admin, and match password.
    if admin is False or admin.is_admin is False or admin.password != password:
        return False
    else:
        return True
