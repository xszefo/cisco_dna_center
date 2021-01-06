#!/usr/bin/env python3

import requests
from get_token import get_token

def main():
    token = get_token()
    if token == 'ERROR':
        print('NO TOKEN')
        return False

    headers = {
    'X-Auth-Token': token,
    }

    url = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device'
    print(url)

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print('ERROR')
        print(response.text)
        return False

    resp_json = response.json()['response']
    
    print('\n{:24} {:17} {:10} {:15}'.format('Name', 'MAC', 'Soft', 'IP'))
    print(67*'-')
    for device in resp_json:
        if device['hostname']:
            hostname = device['hostname']
            macAddress = device['macAddress']
            softwareVersion = device['softwareVersion']
            managementIpAddress = device['managementIpAddress']
            print(f'{hostname:24} {macAddress:17} {softwareVersion:10} {managementIpAddress:15}')


if __name__ == '__main__':
    main()
