import Contact
class ContactManager:


    def main(self):
        c = Contacts({})
        print('1: ADD_PERSON, 2: MODIFY_PERSON, 3: DELETE_PERSON, 4: DISPLAY_DETAILS, 5: DISPLAY_PROVIDER,'
              ' 6: DISPLAY_RECORDS_OF_PROVIDER, 7: DISPLAY_RECORDS_CONTAINING_STRING, 8:EXIT')
        while True:
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
            elif ip == '2':
                pass
            elif ip == '3':
                phone_no = input('Phone_no:')
                if phone_no in c.data.keys():
                    c.delete_person(phone_no)
            elif ip == '4':
                phone_no = input('Phone_no:')
                if phone_no in c.data.keys():
                    details = c.get_details(phone_no)
                    print('Name: {name}, Phone_no: {phone_no}, Email: {email}, Street: {street}, City: {city}, '
                          'State: {state}, Pin_code: {pin_code}'.format(name = details.name,
                                                                        phone_no = details.phone_no,
                                                                        email = details.email,
                                                                        street = details.address.street,
                                                                        city = details.address.city,
                                                                        state = details.address.state,
                                                                        pin_code = details.address.pin_code))
            elif ip == '5':
                phone_no = input('Phone_no:')
                if phone_no in c.data.keys():
                    provider_name = c.get_provider(phone_no)
                    print(provider_name)
            elif ip == '6':
                provider_name = input('Provider name:')
                if provider_name in c.provider.keys():
                    records = c.get_records_of_provider(provider_name)
                    print(records)
            elif ip == '7':
                fields = ['name', 'phone_no', 'email', 'street', 'city', 'state', 'pin_code']
                st = input('Enter a string:')
                field = input('Enter a field:')
                if field in fields:
                    li = c.get_records_containing_string(st, field)
                    for item in li:
                        print(item.name, item.phone_no, item.email, item.address.street, item.address.city,
                              item.address.state, item.address.pin_code)
            elif ip == '8':
                pass
            else:
                print('Unknown input')