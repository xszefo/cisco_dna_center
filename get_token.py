#!/usr/bin/env python3

import requests
import base64
from credentials import user, password
from requests.auth import HTTPBasicAuth

def get_token():
    cred = f'{user}:{password}'
    cred_bytes = cred.encode('ascii')
    encoded_cred = base64.b64encode(cred_bytes).decode('ascii')
    
    headers = {
    'Authorization': f'Basic {encoded_cred}',
    }

    url = 'https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token'
    print(url)

    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        token = response.json()['Token']
    else:
        token = 'ERROR'
    
    return token

if __name__ == '__main__':
    get_token()
