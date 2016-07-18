class Provider():
    def __init__(self, provider_name, phone_no):
        self.provider_name = provider_name
        self.phone_no = phone_no


class ProviderManager():

    Airtel = ['9900', '9800', '9811']
    BSNL = ['9440', '9822']
    Idea = ['9848', '9912']
    Reliance = ['9300', '9812']

    def set_provider_name(self, phone_no):
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


c = ProviderManager()
p = c.set_provider_name("9440123456")
print p.phone_no,p.provider_name