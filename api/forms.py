# Internship Portal Web App
# forms.py for API


"""
Clients: Dr. Joseph Anderson, Dr. Giulia Franchi
Team: Blaine Mason, Jacob Duncan, Justin Ventura, Margaret Finnegan

For now just store API in the forms.py file, this will change later.
"""

from flask import Blueprint, request

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
    company_name = data["company_name"],
    company_address = data["company_address"],
    company_city = data["company_city"],
    company_state = data["company_state"],
    company_zip = data["company_zip"],
    position_title = data['position_title']
    pos_responsibility = data['pos_responsibility']
    min_qualifications = data['min_qualifications']
    pref_qualifications = data['pref_qualifications']
    additional_info = data['additional_info']
    print(f'Company Name: {company_name}, Company Address: {company_address}, Company City: {company_city}, Company State: {company_state}, Company Zip: {company_zip}, Position Title: {position_title}, Position Responsibility: {pos_responsibility}, Minimum Qualifications: {min_qualifications}, Preffered Qualifications: {pref_qualifications}, Additional Info: {additional_info}')

    response = {"status": 200}
    return response  # Status code success
