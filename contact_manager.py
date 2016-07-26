import json
import os

class Address:
    def __init__(self, street, city, state, pin_code):
        self.street = street
        self.city = city
        self.state = state
        self.pin_code = pin_code

    def get_json(self):
        json = {}
        json["street"] = self.street
        json["city"] = self.city
        json["state"] = self.city
        json["pin_code"] = self.pin_code
        return json

    def set_street(self, street):
        self.street = street

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_pin_code(self, pin_code):
        self.pin_code = pin_code

    def get_street(self):
        return self.street

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_pin_code(self):
        return self.pin_code


class Contact:
    def __init__(self, name, phone_no, email, street, city, state, pin_code):
        self.name = name
        self.phone_no = phone_no
        self.email = email
        self.address = Address(street, city, state, pin_code)

    def get_json(self):
        json = {}
        json["name"] = self.name
        json["phone_no"] = self.phone_no
        json["email"] = self.email
        json["address"] = self.address.get_json()
        return json

    def set_name(self, name):
        self.name = name

    def set_phone_no(self, phone_no):
        self.phone_no = phone_no

    def set_email(self, email):
        self.email = email

    def set_address(self, address):
        self.address = address

    def get_name(self):
        return self.name

    def get_phone_no(self):
        return self.phone_no

    def get_email(self):
        return self.email

    def get_address(self):
        return self.address




class ContactDetails:
    NAME = 'name'
    PHONE_NO = 'phone_no'
    EMAIL = 'email'
    ADDRESS = 'address'
    STREET = 'street'
    CITY = 'city'
    STATE = 'state'
    PIN_CODE = 'pin_code'


class Provider():
    def __init__(self, provider_name):
        self.provider_name = provider_name
        self.series_list =[]
    def add_series(self,series):
        self.series_list.append(series)


class ProviderManager():
    provider_list = []
    provider = Provider("Airtel")
    provider.add_series("9900")
    provider.add_series("9800")
    provider.add_series("9811")
    provider_list.append(provider)
    provider = Provider("BSNL")
    provider.add_series("9440")
    provider.add_series("9822")
    provider_list.append(provider)
    provider = Provider("Reliance")
    provider.add_series("9300")
    provider.add_series("9812")
    provider_list.append(provider)

    @staticmethod
    def get_provider_name(phone_no):
        for provider in ProviderManager.provider_list:
            if phone_no[0:4] in provider.series_list:
                return provider.provider_name
        return "Other"


class Contacts:
    def __init__(self, contact_list):
        self.contact_list = contact_list

    def add_contact(self, contact):
        self.contact_list[contact.phone_no] = contact

    def modify_contact(self, phone_no, fields):
        for field in fields.keys():
            if field == ContactDetails.NAME:
                self.contact_list[phone_no].name = fields[field]
            elif field == ContactDetails.PHONE_NO:
                self.contact_list[phone_no].phone_no = fields[field]
                self.contact_list[fields[field]] = self.contact_list.pop[phone_no]
            elif field == ContactDetails.EMAIL:
                self.contact_list[phone_no].email = fields[field]
            elif field == ContactDetails.STREET:
                self.contact_list[phone_no].addres.street = fields[field]
            elif field == ContactDetails.CITY:
                self.contact_list[phone_no].addres.city = fields[field]
            elif field == ContactDetails.STATE:
                self.contact_list[phone_no].addres.state = fields[field]
            elif field == ContactDetails.PIN_CODE:
                self.contact_list[phone_no].addres.pin_code = fields[field]

    def delete_contact(self, phone_no):
        del self.contact_list[phone_no]

    def get_contact(self, phone_no):
        return self.contact_list[phone_no]

    def get_provider(self, phone_no):
        return  ProviderManager.get_provider_name(phone_no[0:4])

    def get_contacts_by_provider(self, provider_name):
        li = []
        for phone, contact in self.contact_list.items():
            if self.get_provider(phone) == provider_name:
                li.append(contact)
        return li

    def get_contacts_by_field(self, st, field):
        li = []
        for phone, contact in self.contact_list.items():
            if field == ContactDetails.NAME and st in contact.name:
                li.append(contact)
            elif field == ContactDetails.PHONE_NO and st in contact.phone_no:
                li.append(contact)
            elif field == ContactDetails.EMAIL and st in contact.email:
                li.append(contact)
            elif field == ContactDetails.STREET and st in contact.address.street:
                li.append(contact)
            elif field == ContactDetails.CITY and st in contact.address.city:
                li.append(contact)
            elif field == ContactDetails.STATE and st in contact.address.state:
                li.append(contact)
            elif field == ContactDetails.PIN_CODE and st in contact.address.pin_code:
                li.append(contact)
        return li


class ContactManager:
    contact_list = {}
    contacts = Contacts(contact_list)

    def load_contacts_from_file(self):
        if os.path.isfile('contacts_data.json') and os.path.getsize('contacts_data.json') > 0:
            with open('contacts_data.json') as data_file:
                json_data = json.load(data_file)
        for phone, contact in json_data.items():
            ct = Contact(contact[ContactDetails.NAME], contact[ContactDetails.PHONE_NO], contact[ContactDetails.EMAIL],
                         contact[ContactDetails.ADDRESS][ContactDetails.STREET],
                         contact[ContactDetails.ADDRESS][ContactDetails.CITY],
                         contact[ContactDetails.ADDRESS][ContactDetails.STATE],
                         contact[ContactDetails.ADDRESS][ContactDetails.PIN_CODE])
            cm.contact_list[phone] = ct
        cm.contacts = Contacts(cm.contact_list)

    def get_formatted_details(self, details):
        return 'Name: {name}, Phone_no: {phone_no}, Email: {email}, Street: {street}, City: {city}, ' \
               'State: {state}, Pin_code: {pin_code}'.format(name=details.name,
                                                             phone_no=details.phone_no,
                                                             email=details.email,
                                                             street=details.address.street,
                                                             city=details.address.city,
                                                             state=details.address.state,
                                                             pin_code=details.address.pin_code)

    def is_contact_exist(self, phone_no):
        if phone_no not in cm.contacts.contact_list.keys():
            return False
        else:
            return True

    def is_valid_phone_no(self, phone_no):
        if len(phone_no) == 10 and phone_no[0] != '0' and phone_no.isnumeric():
            return True
        else:
            return False


    def add_contact(self):
        name = input('Name:')
        phone_no = input('Phone:')
        email = input('Email:')
        street = input('Street:')
        city = input('City:')
        state = input('State:')
        pin_code = input('Pin_code:')
        is_contact_exist = cm.is_contact_exist(phone_no)
        valid_phone_no = cm.is_valid_phone_no(phone_no)
        if (not is_contact_exist) and valid_phone_no:
            contact = Contact(name, phone_no, email, street, city, state, pin_code)
            cm.contacts.add_contact(contact)
            print('Contact successfully added!')
        elif is_contact_exist:
            print('Phone number already exists.Do you want to\n'
                  '1: Modify the existing contact\n'
                  '2: Do not add this contact')
            option = input('Enter your option:')
            if option == '1':
                cm.contacts.delete_contact(phone_no)
                contact = Contact(name, phone_no, email, street, city, state, pin_code)
                cm.contacts.add_contact(contact)
                print('Existing contact is modified with the new one')
            elif option == '2':
                return
        else:
            print('Phone number is not valid...Please check it.')

    def modify_contact(self):
        cm.get_contact()
        fields = [ContactDetails.NAME, ContactDetails.PHONE_NO, ContactDetails.EMAIL, ContactDetails.STREET,
                  ContactDetails.CITY, ContactDetails.STATE, ContactDetails.PIN_CODE]
        phone_no = input('Enter Phone_no:')
        is_contact_exist = cm.is_contact_exist(phone_no)
        if is_contact_exist:
            n = int(input('Enter no. of fields to change:'))
            d = {}
            for i in range(n):
                field = input('Field:')
                if field not in fields:
                    print('Field name is not valid')
                field_value = input('Field_value:')
                d[field] = field_value
            cm.contacts.modify_contact(phone_no, d)
            print('Contact details modified')
        else:
            print('There is no contact with this phone number!')

    def delete_contact(self):
        phone_no = input('Phone_no:')
        is_contact_exist = cm.is_contact_exist(phone_no)
        if is_contact_exist:
            cm.contacts.delete_contact(phone_no)
            print('Contact deleted')
        else:
            print('There is no contact with this phone number!')

    def get_contact(self):
        phone_no = input('Phone_no:')
        is_contact_exist = cm.is_contact_exist(phone_no)
        if is_contact_exist:
            details = cm.contacts.get_contact(phone_no)
            print(cm.get_formatted_details(details))
        else:
            print('There is no contact with this phone number!')

    def get_provider(self):
        phone_no = input('Phone_no:')
        valid_phone_no = cm.is_valid_phone_no(phone_no)
        if valid_phone_no:
            print((ProviderManager.get_provider_name(phone_no[0:4])))
        else:
            print('Phone number is not valid!')

    def get_contacts_by_provider(self):
        provider_name = input('Provider name:')
        records = cm.contacts.get_contacts_by_provider(provider_name)
        for item in records:
            print(cm.get_formatted_details(item))

    def get_contacts_by_field(self):
        fields = [ContactDetails.NAME, ContactDetails.PHONE_NO, ContactDetails.EMAIL, ContactDetails.STREET,
                  ContactDetails.CITY, ContactDetails.STATE, ContactDetails.PIN_CODE]
        st = input('Enter a string:')
        field = input('Enter a field:')
        if field in fields:
            li = cm.contacts.get_contacts_by_field(st, field)
            for item in li:
                print(cm.get_formatted_details(item))
        else:
            print('There is no such field!')

    def save_contact_to_file(self):
        final_contact_list = {}

        for key, value in cm.contacts.contact_list.items():
            final_contact_list[key] = value.get_json()

        with open('contacts_data.json', 'w') as data_file:
            json.dump(final_contact_list, data_file)

