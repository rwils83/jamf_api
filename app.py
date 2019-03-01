import requests, os, json
from requests.auth import HTTPBasicAuth

headers = {
    'accept':'application/json'
}

response = requests.get('https://pindrop.jamfcloud.com/JSSResource/computers', headers=headers, auth=('rwilson', os.getenv('JAMFPASS')))


#print "the response.text is: {}".format(response.text)

print "the response.headers is: {}".format(response.headers)


# print "the response.status is: {}".format(response.status_code)
#

print json.dumps(response.json(), indent=4, sort_keys=True, separators=(',', ': '))
#print type(response.content)
#print response.content