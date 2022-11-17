import requests

resp = requests.get('https://reqres.in/api/users?page=2')
# Performing Serialization
json_resp = resp.json()


