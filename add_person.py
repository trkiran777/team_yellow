class Address(object):
    def __init__(self,street,city,state,pin_code):
        self.street=street
        self.city=city
        self.state=state
        self.pin_code=pin_code

class Contact(object):
    def __init__(self,name,phone_no,email,street,city,state,pin_code):
        self.name = name
        self.phone_no = phone_no
        self.email = email
        self.address=Address(street,city,state,pin_code)
        #Address.street = street
        #Address.city = city
        #Address.state = state
        #Address.pin_code = pin_code
class Contacts:
    provider={'airtel':['9900','9800','9811'],'bsnl':['9440','9822'],'idea':['9848','9912'],'reliance':['9300','9812']}
    #address=Address()
    def __init__(self,data):
        self.data=data
    def add_person(self,contact):
        self.data[contact.phone_no] = contact
        return "\n Contact added successfully"

    def modify_persin(self,phone_no,name='',email='',street='',city='',state='',pin_code=''):
        #if phone_no not in self.data.keys():
        #   return 'not exist'
        if name!='':
            #print('inside cond')
            self.data[phone_no].name=name
        if email!='':
            self.data[phone_no].email=email
        if street!='':
            self.data[phone_no].address.street=street
        if city!='':
            self.data[phone_no].address.city=city
        if state!='':
            self.data[phone_no].address.state=state
        if pin_code!='':
            self.data[phone_no].address.pin_code=pin_code
        return 'Modified Successfully'

    def delete_person(self,phone_no):
        if phone_no not in self.data.keys():
            return 'not exist'
        else:
            del (self.data[phone_no])
            return 'deleted successfully'

    def get_details(self,phone_no):
        if phone_no in self.data.keys():
            return self.data[phone_no]

    def get_provider(self,phone_no):
        s=phone_no[0:4]
       # provider = {'airtel': ['9900', '9800', '9811'], 'bsnl': ['9440', '9822'], 'idea': ['9848', '9912'],
      #              'reliance': ['9300', '9812']}
        for key,values in Contacts.provider.items():
            if s in values:
                return key
        return 'others'

    def get_records(self,provider_name):
       _li=[]
       for _key in self.data:
           _li.append(_key)
       for items in _li:
           if items[0:4] not in Contacts.provider[provider_name]:
               _li.remove(items)
       return _li

    def display_record_contains_string(self,str,field):
        dipt=[]
        for key,val in self.data.items():
            if field=='name' and str in val.name:
                dipt.append(self.data[key])
            if field=='phone_no' and str in val.phone_no:
                dipt.append(self.data[key])
            if field=='email' and str in val.email:
                dipt.append(self.data[key])
            if field=='street' and str in val.address.street:
                dipt.append(self.data[key])
            if field=='city' and str in val.address.city:
                dipt.append(self.data[key])
            if field=='state' and str in val.address.state:
                dipt.append(self.data[key])
            if field=='pin_code' and str in val.address.pin_code:
                dipt.append(self.data[key])
        return dipt
        #return self.data[lis]


class main(object):
    #contacts=Contacts()
    def main1(self):
        #c=[{}]
        contacts = Contacts({})
        while True:
            print("PLEASE SELECT FIELD OF SHOWN BELOW")
            print("\n 1.Add contact \n 2.Edit contact \n 3.Delete Contact \n 4.Get phone_no details \n 5.Get provider details of your number\n 6.Get records of provider \n 7.Display record of field \n 8.Exit")
            val=int(input())
            if val==1:
                print("enter contact details:")
                contact=Contact(input('name:'),input('phone_no:'),input('email:'),input('street:'),input('city:'),input('state:'),input('pin_code:'))
                print(contacts.add_person(contact))

            if val==2:
                print("enter mobile number to edit:")
                _num=input()
                if _num not in contacts.data:
                    print("number not exist")
                else:
                    print("enter data to edit:")
                    print(contacts.modify_persin(_num,input('name:'),input('email:'),input('street:'),input('city:'),input('state:'),input('pin_code:')))

            if val==3:
                print("please enter phone number to delete:")
                print(contacts.delete_person(input()))

            if val==4:
                print("please enter phone no to get details:")
                details = contacts.get_details(input())
                print('Name=', details.name,'\n Email=', details.email,'\n street=',details.address.street,'\n city=', details.address.city,'\n state=',details.address.state,'\n pincode=',details.address.pin_code)

            if val==5:
                print("enter phone no:")
                print('your sevice provider is:',contacts.get_provider(input()))

            if val==6:
                print("enter provider name:")
                print(contacts.get_records(input()))
            if val==7:
                print("enter field u want to search:")
                _fild=input()
                print("enter name u want to search")
                _str=input()
                li=contacts.display_record_contains_string(_str,_fild)
                for i in range(len(li)):
                    print('name is:',li[i].name,'phone_no:',li[i].phone_no)
                #print('name is :',li.name,'phone_no is:',li.phone_no)

            if val==8:
                break



if __name__=='__main__':
    a=main()
    a.main1()