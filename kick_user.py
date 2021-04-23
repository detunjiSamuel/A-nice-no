import requests

from secrets import username,password

BASE_URL= ''


class KickUser:
    def __int__(self):
        self.own_mac_address = ""
        self.user_mac_address= ""

    def bounce_the_person(self):
        pass
    
    def get_cookies(self):
        pass

    def get_user_mac(self):
        pass

    def get_own_mac(self):
        pass

    def change_mac(self):
        pass

    def logout_user(self):
        pass

    def revert_and_login(self):
        pass

if __name__=='__main__':
    ku = KickUser()
    ku.bounce_the_person()