# Justin Ventura

"""
This module contains routes specifically for the admin.
"""

# Flask imports:
from flask import Blueprint, request

from .models import db, ListingsModel, ClientsModel
from .constants import LISTING_STATUSES
from .helpers import admin_session


admin = Blueprint('admin', __name__, url_prefix='/admin')


# ------------------------------------------------------------------------
#          ADMIN ROUTES: these routes are all for the admin
# ------------------------------------------------------------------------

# Ensure that client is in admin session:
@admin.before_request
def _admin_session():
    """Runs before all admin routes to check session."""
    if admin_session() is False:
        return {'err_msg': 'ACCESS DENIED.'}, 403


# STATUSES: inactive, active, pending.
@admin.route('/get-listings/<status>', methods=['GET'])
def get_listings(status: str = 'all'):
    """Route returns json payload of all <status> listings:

    NOTE: must be in admin session.

    JSON payload format:
    {
        'i': {
            'client': client_name,
            'listing': {
                'id': listing.id,
                'client_id': client_id,
                'position': position,
                'pos_responsibility': pos_responsibility,
                'min_qualifications': min_qualifications,
                'pref_qualifications': pref_qualifications,
                'additional_info': additional_info,
                'status': status,
                'starred': starred,
            }
        }
    }
    """
    response = dict()

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
                'client': client_name,
                'listing': listing.to_dict()
            }

    # No listings found.
    else:
        response['err_msg'] = 'No listings found.'
        code = 200

    return response, code


# Get a singular listing:
@admin.route('/get-listing/<id>', methods=['GET'])
def get_listing(id: int):
    """Get a singular listing with the given id"""
    response = dict()

    if listing := ListingsModel.query.filter_by(id=id).first():
        response['listing'] = listing.to_dict()
        code = 200
    else:
        response['err_msg'] = f'Listing with id: {id} not found.'
        code = 401

    return response, code


# Route for changing a listings status.
@admin.route('/set-status/<id>/<status>', methods=['PUT'])
def action_on_listing(id: int, status: str):
    """Route accepts a listing:

    NOTE: must be in admin session.
    """
    response = dict()

    # Valid status:
    if status in LISTING_STATUSES:
        listing = ListingsModel.query.get(id)
        listing.status = status
        db.session.commit()

        response['listing'] = listing.to_dict()
        code = 200

    # Invalid status:
    else:
        response['err_msg'] = 'Invalid status'
        code = 400

    return response, code


# Route for (un)starring listings.
@admin.route('star-listing/<listing_id>', methods=['PUT'])
def star_listing(listing_id: int):
    """Star a listing

    If a listing is unstarred, star it.
    If a listing is starred, unstar it.
    """
    response = dict()

    # Check if listing is in database, then update and return to Jake:
    if listing := ListingsModel.query.filter_by(id=listing_id).first():
        listing.starred = True if listing.starred is False else False
        db.session.commit()
        response['listing'] = listing.to_dict()
        code = 200

    # Otherwise, return an error message:
    else:
        response['err_msg'] = f'Listing with id {listing_id}\
                                not found in database'
        code = 400

    return response, code


# Route for editing listings.
@admin.route('edit-listing/<id>', methods=['PUT'])
def edit_listing(id: int) -> None:
    """Edit a listing.

    Replace the existing listing data with the data
    passed in with the request."""
    response = dict()
    data = request.json

    assert data is not None, 'No listing information in PUT request.'

    # If the listing is already in the database:
    if listing := ListingsModel.query.filter_by(id=id).first():

        # Listing information:
        listing.position = data['position_title']
        listing.pos_responsibility = data['pos_responsibility']
        listing.min_qualifications = data['min_qualifications']
        listing.pref_qualifications = data['pref_qualifications']
        listing.additional_info = data['additional_info']
        listing.duration = data['duration']
        listing.app_open = data['app_open']
        listing.app_close = data['app_close']

        # Update the database.
        db.session.commit()
        response['listing'] = listing.to_dict()
        code = 200

    # Invalid listing id:
    else:
        response['err_msg'] = f'Listing with id {id}\
                                not found in database'
        code = 400

    return response, code
