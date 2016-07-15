import json


class Address:
    def __init__(self, street, city, state, pin_code):
        self.street = street
        self.city = city
        self.state = state
        self.pin_code = pin_code


class Contact:
    def __init__(self, name, phone_no, email, street, city, state, pin_code):
        self.name = name
        self.phone_no = phone_no
        self.email = email
        self.address = Address(street, city, state, pin_code)


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
    def __init__(self):
        self.Airtel = ['9900', '9800', '9811']
        self.BSNL = ['9440', '9822']
        self.Idea = ['9848', '9912']
        self.Reliance = ['9300', '9812']
        self.provider_name = ""

class ProviderManager():
    def __init__(self):
        self.provider = Provider()
    def set_provider_name(self, phone_no):
        if phone_no in self.provider.Airtel:

            self.provider.provider_name = "Airtel"
        elif phone_no in self.provider.BSNL:
            self.provider.provider_name = "BSNL"

        elif phone_no in self.provider.Idea:
            self.provider.provider_name = "Idea"

        elif phone_no in self.provider.Reliance:
            self.provider.provider_name = "Reliance"
        else:
            self.provider.provider_name = "others"




    def get_provider_name(self,phone_no):
        self.set_provider_name(phone_no)
        return self.provider.provider_name





class Contacts:
    def __init__(self, contact_list):
        self.contact_list = contact_list

    def add_contact(self, contact):
        self.contact_list[contact.phone_no] = contact

    def modify_contact(self, phone_no, fields):
        for key in fields.keys():
            if key == ContactDetails.NAME:
                self.contact_list[phone_no].name = fields[key]
            elif key == ContactDetails.PHONE_NO:
                self.contact_list[phone_no].phone_no = fields[key]
                self.contact_list[fields[key]] = self.contact_list.pop[phone_no]
            elif key == ContactDetails.EMAIL:
                self.contact_list[phone_no].email = fields[key]
            elif key == ContactDetails.STREET:
                self.contact_list[phone_no].addres.street = fields[key]
            elif key == ContactDetails.CITY:
                self.contact_list[phone_no].addres.city = fields[key]
            elif key == ContactDetails.STATE:
                self.contact_list[phone_no].addres.state = fields[key]
            elif key == ContactDetails.PIN_CODE:
                self.contact_list[phone_no].addres.pin_code = fields[key]

    def delete_contact(self, phone_no):
        del self.contact_list[phone_no]

    def get_contact(self, phone_no):
        return self.contact_list[phone_no]

    def get_provider(self, phone_no):
        ProviderManager.get_provider_name(phone_no[0:4])

    def get_contacts_by_provider(self, provider_name):
        li = []
        p = Provider()
        p = p.__dict__
        for key, values in self.contact_list.items():
            if key[0:4] in p[provider_name]:
                li.append(values)
        return li

    def get_contacts_by_string(self, st, field):
        li = []
        for key, values in self.contact_list.items():
            if field == ContactDetails.NAME and st in values.name:
                li.append(values)
            elif field == ContactDetails.PHONE_NO and st in values.phone_no:
                li.append(values)
            elif field == ContactDetails.EMAIL and st in values.email:
                li.append(values)
            elif field == ContactDetails.STREET and st in values.address.street:
                li.append(values)
            elif field == ContactDetails.CITY and st in values.address.city:
                li.append(values)
            elif field == ContactDetails.STATE and st in values.address.state:
                li.append(values)
            elif field == ContactDetails.PIN_CODE and st in values.address.pin_code:
                li.append(values)
        return li


class ContactManager:
    contact_list = {}
    contacts = Contacts(contact_list)

    def get_contacts_from_json(self):
        with open('contacts_data.json') as data_file:
            json_data = json.load(data_file)
        for key, value in json_data.items():
            ct = Contact(value[ContactDetails.NAME], value[ContactDetails.PHONE_NO], value[ContactDetails.EMAIL],
                         value[ContactDetails.ADDRESS][ContactDetails.STREET],
                         value[ContactDetails.ADDRESS][ContactDetails.CITY],
                         value[ContactDetails.ADDRESS][ContactDetails.STATE],
                         value[ContactDetails.ADDRESS][ContactDetails.PIN_CODE])
            cm.contact_list[key] = ct
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

    def check_contact_exists_or_not(self, phone_no):
        if phone_no not in cm.contacts.contact_list.keys():
            return False
        else:
            return True

    def add_contact(self):
        name = input('Name:')
        phone_no = input('Phone:')
        email = input('Email:')
        street = input('Street:')
        city = input('City:')
        state = input('State:')
        pin_code = input('Pin_code:')
        contact_exist = cm.check_contact_exists_or_not(phone_no)
        if (not contact_exist) and len(phone_no) == 10 and phone_no[0] != '0' \
                and phone_no.isnumeric():
            contact = Contact(name, phone_no, email, street, city, state, pin_code)
            cm.contacts.add_contact(contact)
            print('Contact successfully added!')
        elif contact_exist:
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
        fields = [ContactDetails.NAME, ContactDetails.PHONE_NO, ContactDetails.EMAIL, ContactDetails.STREET,
                  ContactDetails.CITY, ContactDetails.STATE, ContactDetails.PIN_CODE]
        phone_no = input('Enter Phone_no:')
        if phone_no in cm.contacts.contact_list.keys():
            n = int(input('Enter no. of fields to change:'))
            d = {}
            for i in range(n):
                key = input('Field:')
                if key not in fields:
                    print('Field name is not valid')
                value = input('Field_value:')
                d[key] = value
            cm.contacts.modify_contact(phone_no, d)
            print('Contact details modified')
        else:
            print('There is no contact with this phone number!')

    def delete_contact(self):
        phone_no = input('Phone_no:')
        if phone_no in cm.contacts.contact_list.keys():
            cm.contacts.delete_contact(phone_no)
            print('Contact deleted')
        else:
            print('There is no contact with this phone number!')

    def get_contact(self):
        phone_no = input('Phone_no:')
        if phone_no in cm.contacts.contact_list.keys():
            details = cm.contacts.get_contact(phone_no)
            print(cm.get_formatted_details(details))
        else:
            print('There is no contact with this phone number!')

    def get_provider(self):
        phone_no = str(input('Phone_no:'))
        s = ProviderManager()
        if len(phone_no) == 10 and phone_no[0] != '0' and phone_no.isnumeric():
            print(s.get_provider_name(phone_no[0:4]))

        else:
            print('Phone number is not valid!')

    def get_contacts_by_provider(self):
        provider_name = input('Provider name:')

        records = cm.contacts.get_contacts_by_provider(provider_name)
        for item in records:
            print(cm.get_formatted_details(item))

    def get_contacts_by_string(self):
        fields = [ContactDetails.NAME, ContactDetails.PHONE_NO, ContactDetails.EMAIL, ContactDetails.STREET,
                  ContactDetails.CITY, ContactDetails.STATE, ContactDetails.PIN_CODE]
        st = input('Enter a string:')
        field = input('Enter a field:')
        if field in fields:
            li = cm.contacts.get_contacts_by_string(st, field)
            for item in li:
                print(cm.get_formatted_details(item))

    def add_contact_list_to_json(self):
        final_contact_list = {}
        for key, value in cm.contacts.contact_list.items():
            final_contact_list[key] = value.__dict__
            final_contact_list[key][ContactDetails.ADDRESS] = \
                final_contact_list[key][ContactDetails.ADDRESS].__dict__
        with open('contacts_data.json', 'w') as data_file:
            json.dump(final_contact_list, data_file)

    def main(self):
        cm.get_contacts_from_json()
        print('1: ADD_PERSON, 2: MODIFY_PERSON, 3: DELETE_PERSON, 4: DISPLAY_DETAILS, 5: DISPLAY_PROVIDER,'
              ' 6: DISPLAY_RECORDS_OF_PROVIDER, 7: DISPLAY_RECORDS_CONTAINING_STRING, 8:EXIT')
        while True:
            print('Enter your command:')
            ip = input()
            if ip == '1':
                cm.add_contact()
            elif ip == '2':
                cm.modify_contact()
            elif ip == '3':
                cm.delete_contact()
            elif ip == '4':
                cm.get_contact()
            elif ip == '5':
                cm.get_provider()
            elif ip == '6':
                cm.get_contacts_by_provider()
            elif ip == '7':
                cm.get_contacts_by_string()
            elif ip == '8':
                cm.add_contact_list_to_json()
                break
            else:
                print('Unknown input')


if __name__ == '__main__':
    cm = ContactManager()
    cm.main()