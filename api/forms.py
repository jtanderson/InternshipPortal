# Internship Portal Web App
# forms.py for API


"""
Clients: Dr. Joseph Anderson, Dr. Giulia Franchi
Team: Blaine Mason, Jacob Duncan, Justin Ventura, Margaret Finnegan

For now just store API in the forms.py file, this will change later.
"""

from flask import Blueprint, request

from .models import ClientsModel, ListingsModel

# Create auth blueprint:
forms = Blueprint('forms', __name__)


# Route for submitting forms:
@forms.route('/contact-submit', methods=['POST'])
def contact_submit():
    """Contact submission route.
    This function handles the contact submissions.
    """
    data = request.json
    name = data['name']
    email = data['email']
    message = data['message']
    print(f'Name: {name}, Email: {email}, Message: {message}')

    return 200  # Status code success

# Route for submitting forms:
@forms.route('/listing-submit', methods=['POST'])
def listing_submit():
    """Listing submission route.
    This function handles the listing submissions.
    """
    data = request.json
    client_name = data["client_name"],
    client_address = data["client_address"],
    client_city = data["client_city"],
    client_state = data["client_state"],
    client_zip = data["client_zip"],
    position_title = data['position_title']
    pos_responsibility = data['pos_responsibility']
    min_qualifications = data['min_qualifications']
    pref_qualifications = data['pref_qualifications']
    additional_info = data['additional_info']
    # print(f'client Name: {client_name}, client Address: {client_address}, client City: {client_city}, client State: {client_state}, client Zip: {client_zip}, Position Title: {position_title}, Position Responsibility: {pos_responsibility}, Minimum Qualifications: {min_qualifications}, Preffered Qualifications: {pref_qualifications}, Additional Info: {additional_info}')

    client = ClientsModel()

    response = {"status": 200}
    return response  # Status code success
