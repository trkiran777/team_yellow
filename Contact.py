
class Address(object):

    def __init__(self,values):
        self.street = values["street"]
        self.city = values["city"]
        self.state = values["state"]
        self.pin_code = values["pin_code"]
class Contact():
    def __init__(self,values ):


        self.name=values["name"]
        self.phone_no=values["phone_no"]
        self.email=values["email"]


        self.address = Address(values)


class ContactOperation():
    def __init__(self,data):
        self.data = data
    '''
Airtel mobile numbers starts with 9900, 9800, 9811
BSNL mobile numbers starts with 9440, 9822
Idea mobile numbers starts with 9848, 9912
Reliance mobile numbers starts with 9300,9852

    '''
    global provider
    provider = {'Airtel': ['9900', '9800', '9811'], 'BSNL': ['9440', '9822'], 'Idea': ['9848', '9912'],
                'Reliance': ['9300', '9812']}

    #add a new person
    def add_person(self,contact):


        self.data[contact.phone_no]  = contact
     #   self.data[contact.phone_no] =

        '''
        self.data[contact.phone_no]['name'] = contact.name
        self.data[contact.phone_no]['email'] = contact.email
        self.data[contact.phone_no]['street'] = contact.street
        self.data[contact.phone_no]['city'] = contact.city
        self.data[contact.phone_no]['state'] = contact.state
        self.data[contact.phone_no]['pin_code'] = contact.pin_code
        '''
        return self.data

    def modify_person_detail(self,phone_no):
        pass

    def delete_contact(self, phone_no):
        del self.data[phone_no]


    def get_details(self,phone_no):
        return self.data[phone_no]
    def get_provider(self,phone_no):
        s = phone_no[0:4]
        for key ,values in provider.items():
            if s in values:
                return key
        return "Others"
    def get_records_of_provider(self,provider_name):
        provider = {'Airtel': ['9900', '9800', '9811'], 'BSNL': ['9440', '9822'], 'Idea': ['9848', '9912'],
                    'Reliance': ['9300', '9812']}
        lis = []
        lis2 = []
        for key,values in self.data.items():
            lis.append(key)
            lis2.append(values)
        print(lis)

        for item in lis:
            if item[0:4] not in provider[provider_name]:
                try:
                    a = lis.index(item)
                    del lis[a]
                    del lis2[a]
                except:
                    print("Err....")
        print(lis)
        return lis2
    def get_record_contains_string(self,sr,field):
        lis = []
        dictt = {}
        for key, values in self.data.items():
            dictt[key] = (values.__dict__)
            dictt[key]["address"] = dictt[key]["address"].__dict__
            if field in dictt[key]:
                if sr in dictt[key][field]:
                    lis.append(values)
            if field in dictt[key]["address"]:
                if sr in dictt[key]["address"][field]:
                    lis.append(values)

        return lis



import json

class ContactManager():
    data = {}
    with open('data.json') as data_file:
        data1 = json.load(data_file)
    lis = []
    for key , values in data1.items():

        c = Contact(data1[key])
        data[key]  = c
    print('1: ADD_PERSON\n2: MODIFY_PERSON\n3: DELETE_PERSON\n4: DISPLAY_DETAILS\n5: DISPLAY_PROVIDER,'
          '\n6: DISPLAY_RECORDS_OF_PROVIDER\n7: DISPLAY_RECORDS_CONTAINING_STRING\n8:EXIT')
    c = ContactOperation(data)

    while True:
        ip = input("Please Enter Your Choice")
        if ip == '1':
            name = input('Name:')
            phone_no = input('Phone:')
            email = input('Email:')
            street = input('Street:')
            city = input('City:')
            state = input('State:')
            pin_code = input('Pin_code:')
            values = {}
            values = {"name": name, "phone_no": phone_no, "email": email, "street": street, "city": city,
             "state": state, "pin_code": pin_code}

            if phone_no not in data.keys() and len(phone_no) == 10 and phone_no[0] != '0' and phone_no.isnumeric():
                contact = Contact(values)
                c.add_person(contact)
        elif ip == '2':
            pass
        elif ip == '3':
            phone_no = input('Phone_no:')
            if phone_no in c.data.keys():
                c.delete_contact(phone_no)
            else:
                    print("phone Number not found")
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
        elif ip == '5':
            phone_no = input('Phone_no:')
            provider_name = c.get_provider(phone_no)
            print(provider_name)
        elif ip == '6':
            provider_name = input('Provider name:')
            if provider_name in provider.keys():
                records = c.get_records_of_provider(provider_name)
                for key in records:
                    key = key.__dict__
                    key["address"] = key["address"].__dict__
                    print(key)

        elif ip == '7':
            fields = ['name', 'phone_no', 'email', 'street', 'city', 'state', 'pin_code']
            st = input('Enter a string:')
            field = input('Enter a field:')
            if field in fields:
                li = c.get_record_contains_string(st,field)
                for item in li:
                    print(item.__dict__)
        elif ip == '8':
                break
        else:
            print('Unknown input')

    dictt = {}
    dict1 = {}
    for key, values in data.items():
        dictt[key] = (values.__dict__)
        dictt[key]["address"] = dictt[key]["address"].__dict__

    print(dictt)
    with open('final.json', 'w') as outfile:
        json.dump(dictt, outfile)
    print("Data successfully written in file")



