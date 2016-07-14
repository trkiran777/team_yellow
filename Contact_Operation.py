class ContactOperation():
    def __init__(self,data ={}):
        self.data = data
    '''
Airtel mobile numbers starts with 9900, 9800, 9811
BSNL mobile numbers starts with 9440, 9822
Idea mobile numbers starts with 9848, 9912
Reliance mobile numbers starts with 9300, 9812

    '''

    global provider
    provider = {'Airtel':['9900','9800','9811'],'BSNL':['9440','9822'],'Idea':['9848','9912'],'Reliance':['9300','9812']}
    #add a new person
    def add_person(self,contact):
        self.data[contact.phone_no]  = {contact}
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

    def delete_person_detail(self,phone_no):
        del self.data[phone_no]
        return self.data

    def get_details(self,phone_no):
        return self.data[phone_no]
    def get_provider(self,phone_no):
        s = phone_no[0:4]
        for key ,values in provider.items():
            if s in values:
                return key
        return "Others"
    def get_records(self,provider_name):
        lis = []
        for key,values in self.data.items():
            lis.append(key)
        for item in lis:
            if item[0:4] not in provider[provider_name]:
                lis.remove(item)
        return lis
    def get_record_contains_string(self,sr,field):
        lis = []
        for key , values in self.data.items():
            if str in self.data[key][values.field]:
                lis.append(self.data[key])
        return lis

