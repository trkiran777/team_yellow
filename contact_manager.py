import json
class Address:

    def __init__(self):
        pass

    def set_address(self,street, city, state, pin_code):
        self.street = street
        self.city = city
        self.state = state
        self.pin_code = pin_code
        self.di = {"street": street,
              "city": city,
              "state": state,
              "pin_code": pin_code}


class Contact:

    def __init__(self):
        pass


    def set_name(self,name):
        self.name = name
    def set_phone_no(self,phone_no):
        self.phone_no = phone_no
    def set_email(self,email):
        self.email = email
    def set_address(self):
        self.address = Address



class Provider():
    def __init__(self, provider_name, phone_no):
        self.provider_name = provider_name
        self.phone_no = phone_no


class ProviderManager():
    Airtel = ['9900', '9800', '9811']
    BSNL = ['9440', '9822']
    Idea = ['9848', '9912']
    Reliance = ['9300', '9812'] #

    def get_provider_name(self, phone_no):
        if phone_no[0:4] in self.Airtel:
            p = Provider("Airtel", phone_no)
            return p
        elif phone_no[0:4] in self.BSNL:
            p = Provider("BSNL", phone_no)
            return p
        elif phone_no[0:4] in self.Idea:
            p = Provider("Idea", phone_no)
            return p
        elif phone_no in self.Reliance:
            p = Provider("Reliance", phone_no)
            return p
        else:
            p = Provider("Others", phone_no)
            return p
#aaaaaaa


class Contacts:

    provider = {'Airtel': ['9900', '9800', '9811'], 'BSNL': ['9440', '9822'], 'Idea': ['9848', '9912'],
                'Reliance': ['9300', '9812']}

    def __init__(self, data):
        self.data = data

    def add_person(self, contact):
        self.data[contact.phone_no] = contact

    def modify_person(self, phone_no, fields):
        for key in fields.keys():
            if key == 'name':
                self.data[phone_no].name = fields[key]
            elif key == 'phone_no':
                self.data[phone_no].phone_no = fields[key]
                self.data[fields[key]] = self.data.pop[phone_no]
            elif key == 'email':
                self.data[phone_no].email = fields[key]
            elif key == 'street':
                self.data[phone_no].addres.street = fields[key]
            elif key == 'city':
                self.data[phone_no].addres.city = fields[key]
            elif key == 'state':
                self.data[phone_no].addres.state = fields[key]
            elif key == 'pin_code':
                    self.data[phone_no].addres.pin_code = fields[key]

    def delete_person(self, phone_no):
        del self.data[phone_no]

    def get_details(self, phone_no):
        return self.data[phone_no]

    def get_provider(self, phone_no):
        s = phone_no[0:4]
        for key, values in Contacts.provider.items():
            if s in values:
                return key
        return 'Others'

    def get_records_of_provider(self, provider_name):
        li = []
        for key, values in self.data.items():
            if key[0:4] in Contacts.provider[provider_name]:
                li.append(values)
        return li

    def get_records_containing_string(self, st, field):
        li = []
        for key, values in self.data.items():
            if field == 'name' and st in values.name:
                li.append(values)
            elif field == 'phone_no' and st in values.phone_no:
                li.append(values)
            elif field == 'email' and st in values.email:
                li.append(values)
            elif field == 'street' and st in values.address.street:
                li.append(values)
            elif field == 'city' and st in values.address.city:
                li.append(values)
            elif field == 'state' and st in values.address.state:
                li.append(values)
            elif field == 'pin_code' and st in values.address.pin_code:
                li.append(values)
        return li


class ContactManager:

    def manage_contacts(self):
        data = {}
        with open('contacts_data.json') as data_file:
            json_data = json.load(data_file)
        for key, value in json_data.items():
            ct = Contact(value["name"], value["phone_no"], value["email"], value["address"]["street"],
                         value["address"]["city"], value["address"]["state"], value["address"]["pin_code"])
            data[key] = ct
        c = Contacts(data)
        print('1: ADD_PERSON, 2: MODIFY_PERSON, 3: DELETE_PERSON, 4: DISPLAY_DETAILS, 5: DISPLAY_PROVIDER,'
              ' 6: DISPLAY_RECORDS_OF_PROVIDER, 7: DISPLAY_RECORDS_CONTAINING_STRING, 8:EXIT')
        while True:
            print('Enter your command:')
            ip = input()
            if ip == '1':

                name = input('Name:')
                phone_no = input('Phone:')
                email = input('Email:')
                street = input('Street:')
                city = input('City:')
                state = input('State:')
                pin_code = input('Pin_code:')
                if phone_no not in c.data.keys() and len(phone_no) == 10 and phone_no[0] != '0' \
                        and phone_no.isnumeric():
                    contact = Contact(name, phone_no, email, street, city, state, pin_code)
                    c.add_person(contact)
                    print('Contact successfully added!')
                elif phone_no in c.data.keys():
                    print('Phone number already exists.Do you want to\n'
                          '1: Modify the existing contact\n'
                          '2: Do not add this contact')
                    option = input('Enter your option:')
                    if option == '1':
                        c.delete_person(phone_no)
                        contact = Contact(name, phone_no, email, street, city, state, pin_code)
                        c.add_person(contact)
                        print('Existing contact is modified with the new one')
                    elif option == '2':
                        continue
                else:
                    print('Phone number is not valid...Please check it.')
            elif ip == '2':
                phone_no = input('Enter Phone_no:')
                if phone_no in c.data.keys():
                    n = int(input('Enter no. of fields to change:'))
                    d = {}
                    for i in range(n):
                        key = input('Field:')
                        value = input('Field_value:')
                        d[key] = value
                    c.modify_person(phone_no, d)
                    print('Contact details modified')
                else:
                    print('There is no contact with this phone number!')
            elif ip == '3':
                phone_no = input('Phone_no:')
                if phone_no in c.data.keys():
                    c.delete_person(phone_no)
                    print('Contact deleted')
                else:
                    print('There is no contact with this phone number!')
            elif ip == '4':
                phone_no = input('Phone_no:')
                if phone_no in c.data.keys():
                    details = c.get_details(phone_no)
                    print('Name: {name}, Phone_no: {phone_no}, Email: {email}, Street: {street}, City: {city}, '
                          'State: {state}, Pin_code: {pin_code}'.format(name=details.name,
                                                                        phone_no=details.phone_no,
                                                                        email=details.email,
                                                                        street=details.address.street,
                                                                        city=details.address.city,
                                                                        state=details.address.state,
                                                                        pin_code=details.address.pin_code))
                else:
                    print('There is no contact with this phone number!')
            elif ip == '5':
                phone_no = input('Phone_no:')
                if len(phone_no) == 10 and phone_no[0] != '0' and phone_no.isnumeric():
                    provider_name = c.get_provider(phone_no)
                    print(provider_name)
                else:
                    print('Phone number is not valid!')
            elif ip == '6':
                provider_name = input('Provider name:')
                if provider_name in c.provider.keys():
                    records = c.get_records_of_provider(provider_name)
                    for item in records:
                        print('Name: {name}, Phone_no: {phone_no}, Email: {email}, Street: {street}, City: {city}, '
                              'State: {state}, Pin_code: {pin_code}'.format(name=item.name,
                                                                            phone_no=item.phone_no,
                                                                            email=item.email,
                                                                            street=item.address.street,
                                                                            city=item.address.city,
                                                                            state=item.address.state,
                                                                            pin_code=item.address.pin_code))

            elif ip == '7':
                fields = ['name', 'phone_no', 'email', 'street', 'city', 'state', 'pin_code']
                st = input('Enter a string:')
                field = input('Enter a field:')
                if field in fields:
                    li = c.get_records_containing_string(st, field)
                    for item in li:
                        print('Name: {name}, Phone_no: {phone_no}, Email: {email}, Street: {street}, City: {city}, '
                              'State: {state}, Pin_code: {pin_code}'.format(name=item.name,
                                                                            phone_no=item.phone_no,
                                                                            email=item.email,
                                                                            street=item.address.street,
                                                                            city=item.address.city,
                                                                            state=item.address.state,
                                                                            pin_code=item.address.pin_code))
            elif ip == '8':
                final_data = {}
                for key, value in c.data.items():
                    final_data[key] = value.__dict__
                    final_data[key]["address"] = final_data[key]["address"].__dict__
                with open('contacts_data.json', 'w') as data_file:
                    json.dump(final_data, data_file, indent=2)
                break
            else:
                print('Unknown input')


if __name__ == '__main__':
    cm = ContactManager()
    cm.manage_contacts()
