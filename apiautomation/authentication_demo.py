import requests
from requests.auth import HTTPBasicAuth

resp = requests.get('https://the-internet.herokuapp.com/basic_auth', auth=HTTPBasicAuth('asda', 'asd'))
print(resp.status_code, end='\n')
assert resp.status_code == 401
# print(resp.json(), end='\n\n')
resp1 = requests.get('https://the-internet.herokuapp.com/basic_auth', auth=('admin', 'admin'))
print(resp1.status_code, end='\n')
assert resp1.status_code == 200
# print(resp1.json(), end='\n\n')
