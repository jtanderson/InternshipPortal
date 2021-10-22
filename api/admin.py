# Justin Ventura

"""
This module contains routes specifically for the admin.
"""

# Flask imports:
from flask import Blueprint

from .models import db, ListingsModel, ClientsModel
from .constants import LISTING_STATUSES
from api import session


admin = Blueprint('admin', __name__, url_prefix='/admin')


# ------------------------------------------------------------------------
#          ADMIN ROUTES: these routes are all for the admin
# ------------------------------------------------------------------------


# STATUSES: inactive, active, pending, rejected.
@admin.route('/get-listings/<status>', methods=['GET'])
def get_listings(status: str = 'all'):
    """Route returns json payload of all <status> listings:

    NOTE: must be in admin session.

    JSON payload format:
    {
        'i': {
            # METADATA:
            'client': client_name,
            'client_id': listing.client_id,
            'listing_id': listing.id,
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

        # Handle possible listing statuses:
        listings = []

        # All statuses:
        if status == 'all':
            listings = ListingsModel.query.all()

        # Query for one of the four statuses:
        elif status in LISTING_STATUSES:
            listings = ListingsModel.query.filter_by(status=status).all()

        # Invalid listings request:
        else:
            response['err_msg'] = 'Invalid listings request.'
            return response, 400

        # Valid listing request:
        if listings is not None:
            code = 200
            # For all pending listings, create a payload for each one:
            for i, listing in enumerate(listings):

                # Use foreign key to get client name via client_id:
                temp = ClientsModel.query.filter_by(id=listing.client_id)\
                    .first()
                client_name = temp.client_name

                # Create the payload:
                response[i] = {
                    # TODO: serializer for listings: 'full_listing': listing,
                    # METADATA:
                    'client': client_name,
                    'client_id': listing.client_id,
                    'listing_id': listing.id,
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

        # No listings found.
        else:
            response['err_msg'] = 'No listings found.'
            code = 200

    # If NOT in admin session, deny access:
    else:
        response['err_msg'] = 'Access Denied.'
        code = 403

    return response, code


# Route for (un)starring listings.
@admin.route('star-listing/<listing_id>', methods=['GET'])
def star_listing(listing_id: int):
    """Star a listing

    If a listing is unstarred, star it.
    If a listing is starred, unstar it.
    """
    response = {}
    if 'username' in session:
        if listing := ListingsModel.query.filter_by(id=listing_id).first():
            listing.starred = True if listing.starred is False else False
            response['listing'] = listing.to_dict()
            code = 200
            db.session.commit()
        else:
            response['err_msg'] = f'Listing with id {listing_id}\
                                    not found in database'
            code = 400
    else:
        response['err_msg'] = 'Access Denied.'
        code = 403

    return response, code
