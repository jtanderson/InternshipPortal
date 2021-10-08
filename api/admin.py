# Justin Ventura

"""
This module contains routes specifically for the admin.
"""

from flask import Blueprint, request


admin = Blueprint('admin', __name__, url_prefix='admin')


# ------------------------------------------------------------------------
#          ADMIN ROUTES: these routes are all for the admin
# ------------------------------------------------------------------------
