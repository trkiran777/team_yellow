import json
import os

from flask import render_template, request
from contact_web_app import app
from contact_web_app.contacts import Contact, ContactDetails, Contacts

contact_list = {}
contacts = Contacts(contact_list)


@app.route('/')
def load_contacts_from_file():
    if os.path.isfile('contacts_data.json') and os.path.getsize('contacts_data.json') > 0:
        with open('contacts_data.json') as data_file:
            json_data = json.load(data_file)
        for key, value in json_data.items():
            ct = Contact(value[ContactDetails.NAME], value[ContactDetails.PHONE_NO], value[ContactDetails.EMAIL],
                         value[ContactDetails.ADDRESS][ContactDetails.STREET],
                         value[ContactDetails.ADDRESS][ContactDetails.CITY],
                         value[ContactDetails.ADDRESS][ContactDetails.STATE],
                         value[ContactDetails.ADDRESS][ContactDetails.PIN_CODE])
            contact_list[key] = ct
    return render_template('contacts_home.html')


@app.route('/contacts_home')
def contacts_home():
    return render_template('contacts_home.html')


@app.route('/add_contact_form')
def add_contact_form():
    message = ''
    return render_template('add_contact.html', message=message)


@app.route('/add_contact', methods=['POST', 'GET'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone_no = request.form['phone_no']
        email = request.form['email']
        street = request.form['street']
        city = request.form['city']
        state = request.form['state']
        pin_code = request.form['pin_code']
        is_contact_exist = contacts.is_contact_exist(phone_no)
        is_valid_phone_no = contacts.is_valid_phone_no(phone_no)
        if (not is_contact_exist) and is_valid_phone_no:
            contact = Contact(name, phone_no, email, street, city, state, pin_code)
            contacts.add_contact(contact)
            contacts.save_contacts_to_file()
            message = 'Contact successfully added!'
            return render_template('add_contact.html', message=message)
        elif is_contact_exist:
            message = 'Contact already exists!'
            return render_template('add_contact.html', message=message)
        else:
            message = 'Invalid phone number!'
            return render_template('add_contact.html', message=message)


@app.route('/modify_contact_form')
def modify_contact_form():
    message = ''
    return render_template('modify_contact.html', message=message)


@app.route('/modify_contact', methods=['POST', 'GET'])
def modify_contact():
    if request.method == 'POST':
        phone_no = request.form['phone_no']
        is_contact_exist = contacts.is_contact_exist(phone_no)
        if is_contact_exist:
            fields = request.form
            contacts.modify_contact(phone_no, fields)
            contacts.save_contacts_to_file()
            message = 'Contact successfully modified!'
            return render_template('modify_contact.html', message=message)
        else:
            message = 'There is no contact with this phone number!'
            return render_template('modify_contact.html', message=message)


@app.route('/delete_contact_form')
def delete_contact_form():
    message = ''
    return render_template('delete_contact.html', message=message)


@app.route('/delete_contact', methods=['POST', 'GET'])
def delete_contact():
    if request.method == 'POST':
        phone_no = request.form['phone_no']
        is_contact_exist = contacts.is_contact_exist(phone_no)
        if is_contact_exist:
            contacts.delete_contact(phone_no)
            contacts.save_contacts_to_file()
            message = 'Contact deleted successfully!'
            return render_template('delete_contact.html', message=message)
        else:
            message = 'There is no contact with this phone number!'
            return render_template('delete_contact.html', message=message)


@app.route('/get_contact_form')
def get_contact_form():
    message = ''
    return render_template('get_contact.html', message=message)


@app.route('/get_contact', methods=['POST', 'GET'])
def get_contact():
    if request.method == 'POST':
        phone_no = request.form['phone_no']
        is_contact_exist = contacts.is_contact_exist(phone_no)
        if is_contact_exist:
            details = contacts.get_contact(phone_no)
            return render_template('view_contact.html', contact=details)
        else:
            message = 'There is no contact with this phone number!'
            return render_template('get_contact.html', message=message)


@app.route('/get_provider_form')
def get_provider_form():
    message = ''
    return render_template('get_provider.html', message=message)


@app.route('/get_provider', methods=['POST', 'GET'])
def get_provider():
    if request.method == 'POST':
        phone_no = request.form['phone_no']
        is_valid_phone_no = contacts.is_valid_phone_no(phone_no)
        if is_valid_phone_no:
            provider_name = contacts.get_provider(phone_no[0:4])
            return render_template('get_provider.html', message=provider_name)
        else:
            message = 'Invalid phone number!'
            return render_template('get_provider.html', message=message)


@app.route('/get_contacts_by_provider_form')
def get_contacts_by_provider_form():
    return render_template('get_contacts_by_provider.html')


@app.route('/get_contacts_by_provider', methods=['POST', 'GET'])
def get_contacts_by_provider():
    if request.method == 'POST':
        provider_name = request.form['provider']
        records = contacts.get_contacts_by_provider(provider_name)
        return render_template('view_contacts.html', contacts=records)


@app.route('/get_contacts_by_field_form')
def get_contacts_by_field_form():
    return render_template('get_contacts_by_field.html')


@app.route('/get_contacts_by_field', methods=['POST', 'GET'])
def get_contacts_by_field():
    if request.method == 'POST':
        string = request.form['string']
        field = request.form['field']
        li = contacts.get_contacts_by_field(string, field)
        return render_template('view_contacts.html', contacts=li)
