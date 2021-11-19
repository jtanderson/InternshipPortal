# Justin Ventura

"""
Routes module for general routes in api.
"""

from flask import Blueprint

from .models import ListingsModel, ClientsModel
from .constants import LISTING_STATUSES

routes = Blueprint('routes', __name__)

# ------------------------------------------------------------------------
#          ADMIN ROUTES: these routes are all for the admin
# ------------------------------------------------------------------------

# Route to get all listings with the given status.


@routes.route('get-listings/<status>')
def get_listings(status: str = 'all'):
    """Route returns json payload of all <status> listings:

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


# Route to get a singular listing with given id.
@routes.route('/get-listing/<id>', methods=['GET'])
def get_listing(id: int):
    """Get a singular listing with the given id"""
    response = dict()

    if listing := ListingsModel.query.filter_by(id=id).first():
        response['listing'] = listing.to_dict()
        code = 200
    else:
        response['err_msg'] = f'Listing with id: {id} not found.'
        code = 404  # Error 404 so we can add a page for this.

    return response, code


# Route to get client information
