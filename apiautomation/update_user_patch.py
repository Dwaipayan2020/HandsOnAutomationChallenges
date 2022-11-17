import requests

payload = {
    "name": "Dwaipayan",
    "job": "Automation"
}

partial_payload = {
    "name": "Dwaipayan Das"
}
# passing the payload as data parameter
response = requests.post('https://reqres.in/api/users', data=payload)
updated_resp = requests.patch('https://reqres.in/api/users/2', data=partial_payload)

print(response)
print('Response in json format:\n', response.json())
print(updated_resp)
print('\nUpdate response in json format:\n', updated_resp.json())
print('\nresponse status code:\n', response.status_code)
print('\nUpdate response status code:\n', updated_resp.status_code)
