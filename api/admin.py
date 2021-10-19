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


# STATUSES: inactive, active, pending, rejected.
@admin.route('/get-listings/<status>', methods=['GET'])
def get_listings(status: str):
    """Route returns json payload of all <status> listings:

    NOTE: must be in admin session.

    JSON payload format:
    {
        'i': {
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
    print(session)
    # If in an admin session:
    if 'username' in session:

        # Gather all pending listings from database:
        listings = ListingsModel.query.filter_by(status=status).all()

        # For all pending listings, create a payload for each one:
        for i, listing in enumerate(listings):

            # Use foreign key to get client name via client_id:
            temp = ClientsModel.query.filter_by(id=listing.client_id).first()
            client_name = temp.client_name

            # Create the payload:
            response[i] = {
                # TODO: serializer for listings: 'full_listing': listing,
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
        response['err_msg'] = 'ACCESS DENIED.'

    return response


@admin.route('/<status>-listing/<id>', methods=['GET'])
def action_on_listings(id: int, status: str):
    """Route accepts a listing:

    NOTE: must be in admin session.
    """
    response = dict()
    # If in an admin session:
    if 'username' in session:
        if status in ['accept, reject']:
            listing = ListingsModel.query.filter_by(id=id)
            setattr(listing, 'status', status)
            session.commit()
        else:
            response['err_msg'] = 'Incorrect Status'
    # If NOT in admin session, deny access:
    else:
        response['err_msg'] = 'Access Denied.'

    return response