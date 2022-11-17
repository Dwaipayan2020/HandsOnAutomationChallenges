import json

import requests

payload_json = open('data_payload.json', 'r').read().strip()

# Performing Deserialization (json object to python object):
# payload = json.loads(payload_json)

# passing the payload as data parameter
response = requests.post('https://reqres.in/api/users', data=json.loads(payload_json))

print(response)
print('Response in json format:\n', response.json())
print('\nresponse status code:\n', response.status_code)
