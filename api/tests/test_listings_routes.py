# Justin Ventura

'''
This module contains the tests for the listings routes.

How to test: `python3 -m pytest -s api/tests/test_db.py`
OR
`python3 -m pytest -s api/tests/`
'''

# Imports for database:
# from api.models import db, ClientsModel, ListingsModel
from api.constants import OK, BAD_REQUEST, NOT_FOUND

from testing_data import listingsToSubmit


# Test route to insert a listing:
def test_listing_submit(client):
    '''
    This test checks that the listing submission route works correctly.

    Route:
        /listing-submit
    '''
    # Test that this route works correctly:
    # ------------------------------ TEST 1 ------------------------------
    for listingToSubmit in listingsToSubmit:
        valid_post = client.post('/listing-submit', json=listingToSubmit)
        assert valid_post.status_code == OK, 'Valid listing failed.'


# Test route to get listings by status:
def test_get_listings_bystatus(client):
    '''
    This test checks that the listings by status route works correctly.

    Route:
        /get-listings/<status>
    '''
    # Test that this route works correctly:
    # ------------------------------ TEST 1 ------------------------------
    invalid_get1 = client.get('/get-listings/joe')
    assert invalid_get1.status_code == BAD_REQUEST, 'Invalid status failed.'

    invalid_get2 = client.get('/get-listings/lsaddfj')
    assert invalid_get2.status_code == BAD_REQUEST, 'Invalid status failed.'

    invalid_get3 = client.get('/get-listings/')
    assert invalid_get3.status_code == NOT_FOUND, 'Missing status failed.'

    # ------------------------------ TEST 2 ------------------------------
    # TODO:
    valid_get = client.get('/get-listings/inactive')
    print(valid_get)
