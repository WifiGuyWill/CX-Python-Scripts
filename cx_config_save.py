#!/usr/bin/python3
#(c) 2020 Will Smith

import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

username = 'username'
password = 'password'
switch1 = 'https://<1st Switch IP or Hostname>/rest/v10.04/'
switch2 = 'https://<2nd Switch IP or Hostname>/rest/v10.04/'
switch3 = 'https://<3nd Switch IP or Hostname>/rest/v10.04/'

config_data ='startup-config?from=%2Frest%2Fv10.04%2Ffullconfigs%2Frunning-config'
creds = {'username': username, 'password': password}


def login(switch, creds):
    session = requests.Session()
    response = session.post(switch + 'login', params=creds, verify=False, timeout=2)
    print('Login status code {}'.format(response.status_code))
    return session

def save_config(session, switch, config_data):
    config = session.put(switch + 'fullconfigs/' + config_data, verify=False, timeout=2)
    print('Config Status: ', config.status_code)

def logout(switch, session):
    logout_response = session.post(switch + 'logout', verify=False, timeout=2)
    print('Logout_Status: ', logout_response.status_code)

if __name__ == "__main__":
#switch1
    try:
        print("1st CX Switch Staring Config Save")
        session = login(switch1, creds)
        save_config(session, switch1, config_data)
        logout(switch1, session)
        print("1st CX Switch Config Saved")
    except:
        print("1st CX Switch Not Online....Continuing")
        pass
#switch2
    try:
        print("2nd CX Switch Staring Config Save")
        session = login(switch2, creds)
        save_config(session, switch2, config_data)
        logout(switch2, session)
        print("2nd CX Switch  Config Saved")
    except:
        print("2nd CX Switch  Not Online....Continuing")
        pass   
#switch3    
    try:
        print("3rd CX Switch Staring Config Save")
        session = login(switch3, creds)
        save_config(session, switch3, config_data)
        logout(switch3, session)
        print("3rd CX Switch Config Saved")
    except:
        print("3rd CX Switch Not Online....Continuing")
        pass   
    print('Config Script Save DONE!')
