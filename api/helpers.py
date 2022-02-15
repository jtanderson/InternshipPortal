# Justin Ventura

"""
This module contains functions used to help out with the app.
"""

# Database functinality imports
from .models import UsersModel
from flask import session


# Check credentials against the database:
def correct_login(username: str, password: str) -> bool:
    """
    This function checks if the username and password pair
    are correct, and are admins.
    """

    # Grab the admin from the database:
    admin = UsersModel.query.filter_by(username=username).first()

    # Must be in database, be admin, and match password.
    if admin is None or admin.is_admin is False or admin.password != password:
        return False
    else:
        return True


# Method to check if in admin session:
def admin_session() -> bool:
    return 'username' in session
