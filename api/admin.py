# Justin Ventura

"""
This module contains routes specifically for the admin.
"""

# Flask imports:
from flask import Blueprint

from .models import ListingsModel, ClientsModel
from api import session


admin = Blueprint('admin', __name__, url_prefix='/admin')


# ------------------------------------------------------------------------
#          ADMIN ROUTES: these routes are all for the admin
# ------------------------------------------------------------------------


@admin.route('/pending-listings', methods=['GET'])
def pending_listings():
    """Route returns json payload of all pending listings:

    NOTE: must be in admin session.

    JSON payload format:
    {
        'Pending listing i': {
            # METADATA:
            'client': client_name,
            'client_id': listing.client_id,
            'status': listing.status,

            # PAYLOAD:
            'position_info': {
                'title': listing.position,
                'responsibility': listing.pos_responsibility,
                'min_qualifications': listing.min_qualifications,
                'pref_qualifications': listing.pref_qualifications,
                'additional_info': listing.additional_info,
            }
        }
    }
    """
    response = dict()

    # If in an admin session:
    if 'username' in session:

        # Gather all pending listings from database:
        all_pending = ListingsModel.query.filter_by(status='pending').all()

        # For all pending listings, create a payload for each one:
        for i, listing in enumerate(all_pending):

            # Use foreign key to get client name via client_id:
            temp = ClientsModel.query.filter_by(id=listing.client_id).first()
            client_name = temp.client_name

            # Create the payload:
            response[i] = {
                # 'full_listing': listing,
                # METADATA:
                'client': client_name,
                'client_id': listing.client_id,
                'status': listing.status,

                # PAYLOAD:
                'position_info': {
                    'title': listing.position,
                    'responsibility': listing.pos_responsibility,
                    'min_qualifications': listing.min_qualifications,
                    'pref_qualifications': listing.pref_qualifications,
                    'additional_info': listing.additional_info,
                }
            }

    # If NOT in admin session, deny access:
    else:
        response['err_msg'] = 'Access Denied.'

    return response


@admin.route('/active-listings', methods=['GET'])
def active_listings():
    pass


@admin.route('/rejected-listings', methods=['GET'])
def rejected_listings():
    pass
