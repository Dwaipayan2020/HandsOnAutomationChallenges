import requests

payload1 = {
    "name": "Dwaipayan",
    "job": "Automation"
}

payload2 = {
    "name": "Dwaipayan",
    "job": "Python Developer"
}
# passing the payload as data parameter
response = requests.post('https://reqres.in/api/users', data=payload1)
update_resp = requests.put('https://reqres.in/api/users/2', data=payload2)

print(response)
print('Response in json format:\n', response.json())
print(update_resp)
print('\nUpdate response in json format:\n', update_resp.json())
print('\nresponse status code:\n', response.status_code)
print('\nUpdate response status code:\n', update_resp.status_code)
