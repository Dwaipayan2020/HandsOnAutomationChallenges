import requests

# Following end point we need to hit for creating a user
# 'https://reqres.in/api/users'

"""Below is the payload or a dictionary we need to send to create a user:

{
    "name": "morpheus",
    "job": "leader"
}

"""

payload = {
    "name": "Dwaipayan",
    "job": "Automation"
}

# passing the payload as data parameter
response = requests.post('https://reqres.in/api/users', data=payload)

print(response)
print('Response in json format:\n', response.json())
print('\nresponse status code:\n', response.status_code)
