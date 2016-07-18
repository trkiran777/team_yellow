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
    def set_provider_name(self, phone_no, ):
        if phone_no in self.provider.Airtel:

            self.provider.provider_name = "Airtel"
        elif phone_no in self.provider.BSNL:
            self.provider.provider_name = "Bsnl"

        elif phone_no in self.provider.Idea:
            self.provider.provider_name = "Idea"

        elif phone_no in self.provider.Reliance:
            self.provider.provider_name = "Reliance"
        else:
            self.provider.provider_name = "others"





    def get_provider_name(self,phone_no):
        self.set_provider_name(phone_no)
        return self.provider.provider_name


c = ProviderManager()
print(c.get_provider_name("9900"))