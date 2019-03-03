#! /usr/bin/env python
import requests, os, json
from requests.auth import HTTPBasicAuth

JAMF_ID = os.getenv('JAMF_ID')

JAMF_PASS = os.getenv('JAMF_PASS')

headers = {
    'accept':'application/json'
}

response = requests.get('https://pindrop.jamfcloud.com/JSSResource/computers', headers=headers, auth=(JAMF_ID,JAMF_PASS))


computer_list = json.dumps(response.json(), indent=4, sort_keys=True, separators=(',', ': '))

print computer_list
