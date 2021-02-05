#!/usr/bin/python3
#(c) 2020 Will Smith

import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

username = 'username'
password = 'password'
baseurl = 'https://<CX Switch IP or Hostname>//rest/v1/'
poe_data = "{\n  \"config\": {\n    \"admin_disable\": false\n  }\n}"
port1 = 'system/interfaces/<Port # in this formate 1%2F1%2F14>/poe_interface'
#port2 = 'system/interfaces/1%2F1%2F33/poe_interface'
#port3 = 'system/interfaces/1%2F1%2F35/poe_interface'

creds = {'username': username, 'password': password}


def login(baseurl, creds):
    session = requests.Session()
    response = session.post(baseurl + 'login', params=creds, verify=False, timeout=2)
    print('Login status code {}'.format(response.status_code))
    return session

def set_poe(session, baseurl, port, poe_data):
    poe = session.put(baseurl + port, data=poe_data, timeout=2, verify=False)
    print('POE Port Status: ', poe.status_code)

def logout(baseurl, session):
    logout_response = session.post(baseurl + 'logout', verify=False, timeout=2)
    print('Logout_Status: ', logout_response.status_code)


if __name__ == "__main__":
    print("Starting CX POE Enable Script")
    try:
        print("Enabling POE Ports")
        session = login(baseurl, creds)
        set_poe(session, baseurl, port1, poe_data)
#        set_poe(session, baseurl, port2, poe_data)
#        set_poe(session, baseurl, port3, poe_data)
        logout(baseurl, session)
    except:
        print("There was an error with CX Switch")
        pass
    print('CX POE Enable Script DONE!')
