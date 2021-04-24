import requests
import subprocess
from hashlib import md5
import hmac
import datetime as dt
import re

from secrets import username, password

BASE_URL = 'http://radsvr2.csis.int/user.php'


class KickUser:
    def __int__(self):
        self.own_mac_address = ""
        self.user_mac_address = ""
        self.cookies = ""
        self.wlan_interface_used = ""

    def bounce_the_person(self):
        #self.get_user_mac()
        #print(self.user_mac_address)
        self.get_own_mac()
        print(self.own_mac_address)

    def get_cookies(self):
        pass

    def get_user_mac(self):
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
        #search for mac address pattern
        all_macs =  re.findall(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',r.text)
        # The logged in system is last for on the list
        self.user_mac_address = all_macs[len(all_macs)-1]
        

    def get_own_mac(self):
        #get the wlan interface that is used for network request with google DNS server(8.8.8.8)
        interface_check_result = subprocess.getstatusoutput(f"ip route get 8.8.8.8 | grep -Po '(?<=dev\s)\w+' | cut -f1 -d ' '")
        #output I received (0, 'wlo1')
        self.wlan_interface_used = interface_check_result[1]
        ifconfig = subprocess.check_output(["ifconfig",self.wlan_interface_used])
        #make ifconfig a string , Got back byte array type as output 
        mac_result = re.findall(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
        self.own_mac_address = mac_result[0]


    def change_mac(self,):
        pass

    def logout_user(self):
        pass

    def revert_and_login(self):
        pass


if __name__ == '__main__':
    ku = KickUser()
    ku.bounce_the_person()
