#!/usr/bin/python3
#(c) 2020 Will Smith

import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

username = 'username'
password = 'password'
baseurl = 'https://<CX Switch IP or Hostname>/rest/v1/'
port1 = 'system/interfaces/<Port # in this formate 1%2F1%2F14>/poe_interface'
#port2 = 'system/interfaces/1%2F1%2F15/poe_interface'
#port3 = 'system/interfaces/1%2F1%2F36/poe_interface'

creds = {'username': username, 'password': password}

def login(baseurl, creds):
    session = requests.Session()
    response = session.post(baseurl + 'login', params=creds, verify=False, timeout=2)
    print('Login Status Code: {}'.format(response.status_code))
    return session

def get_poe(baseurl, port, session):
    poe = session.get(baseurl + port, verify=False)
    poe_status = json.loads(poe.content)
    print('POE DISABLED: ', poe_status['config']['admin_disable'])
#    print('POE Status: ', poe.status_code)

def logout(baseurl, session):
    logout_response = session.post(baseurl + 'logout', verify=False, timeout=2)
    print('Logout Status: ', logout_response.status_code)

if __name__ == '__main__':
    session = login(baseurl, creds)
    get_poe(baseurl, port1, session)
    get_poe(baseurl, port2, session)
    get_poe(baseurl, port3, session)
    logout(baseurl, session)
    print('DONE!')
