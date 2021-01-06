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
    for device in resp_json:
        print(10*'*')
        print(f'Name: {device["hostname"]}')
        print(f'MAC: {device["macAddress"]}')
        print(f'Soft: {device["softwareVersion"]}')
        print(f'IP: {device["managementIpAddress"]}')


if __name__ == '__main__':
    main()
