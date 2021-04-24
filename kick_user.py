import requests
from hashlib import md5
import hmac
import datetime as dt

from secrets import username, password

BASE_URL = 'http://radsvr2.csis.int/user.php'


class KickUser:
    def __int__(self):
        self.own_mac_address = ""
        self.user_mac_address = ""
        self.cookies = ""

    def bounce_the_person(self):

        # encode password in right format and make bytes array
        string_encoded = md5(bytes(password,'utf-8')).hexdigest()
        # hash details before sending
        hashed_password = hmac.new(bytes(username,'utf-8'),bytes(string_encoded,'utf-8')).hexdigest()
        # send request to get cookie
        r = requests.post(BASE_URL+'?cont=login',
                          data=dict(username=username, password='', Lang="English", url="", md5=hashed_password))
        self.cookies = r.cookies['PHPSESSID']
        #get the intruder's mac address
        headers = {'Cookie': 'PHPSESSID={0}'.format(self.cookies)}
        r = requests.get(BASE_URL , params=dict(cont='detailed_traffic_report', username=username,fromdate=dt.datetime.now().strftime('%y-%m-%d')),headers=headers)
        
        print(r.status_code)
        


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


if __name__ == '__main__':
    ku = KickUser()
    ku.bounce_the_person()
