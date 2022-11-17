import requests

payload = {
    "name": "Dwaipayan",
    "job": "Automation"
}

# passing the payload as data parameter
response = requests.post('https://reqres.in/api/users', data=payload)
deletion_resp = requests.delete('https://reqres.in/api/users/2')

print(response)
print('Response in json format:\n', response.json())
print(deletion_resp)
# print('\nUpdate response in json format:\n', deletion_resp.json())
print('\nresponse status code:\n', response.status_code)
print('\nUpdate response status code:\n', deletion_resp.status_code)

status_code = deletion_resp.status_code
assert status_code == 204, f'User deletion failed...Expected:204, Found:{status_code}'
