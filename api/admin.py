# Justin Ventura

"""
This module contains routes specifically for the admin.
"""

# Flask imports:
from flask import Blueprint, request

from .models import ListingsModel, ClientsModel, db
from api import session


admin = Blueprint('admin', __name__, url_prefix='/admin')


# ------------------------------------------------------------------------
#          ADMIN ROUTES: these routes are all for the admin
# ------------------------------------------------------------------------


@admin.route('/pending-listings', methods=['GET'])
def pending_listings():
    response = {}
    
    google = ClientsModel('Google', 'Address', 'Email', 'Phone', 1)
    amazon = ClientsModel('Amazon', 'Address', 'Email', 'Phone', 1)

    db.session.add(google)
    db.session.add(amazon)
    db.session.commit()

    listing1 = ListingsModel(1, 'SE', 'Stuff', 'Things', 'Experience', 'NA', 'pending')
    listing2 = ListingsModel(2, 'SDE', 'Stuff', 'Things', 'Experience', 'NA', 'pending')

    db.session.add(listing1)
    db.session.add(listing2)
    db.session.commit()

    all_pending = ListingsModel.query.filter_by(status='pending').all()

    response = dict()

    for i, listing in enumerate(all_pending):
        response[f'listing {i}'] = [listing.client_id, listing.position]
    
    return response, 200

    # if 'username' in session:
    #     all_pending = ListingsModel.query.filter_by(status='pending').all()

    #     for listing in all_pending:
    #         print(listing)

    # else:
    #     response['err_msg'] = 'Access Denied.'

    # return response


@admin.route('/active-listings', methods=['GET'])
def active_listings():
    pass


@admin.route('/rejected-listings', methods=['GET'])
def rejected_listings():
    pass