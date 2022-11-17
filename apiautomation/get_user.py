import requests

pa = {'page': 2}
resp = requests.get('https://reqres.in/api/users', params=pa)
# resp = requests.get('https://reqres.in/api/users?page=2')
print('\nResponse url:\n', resp.url)
print('\nResponse content:\n', resp.content)
print('\nResponse headers:\n', resp.headers)
print('\nResponse cookies:\n', resp.cookies)
print('\nResponse encoding:\n', resp.encoding)
print('\nPrinting Serialized response in json:\n', resp.json())
print('\nPrinting response in plain text:\n', resp.text)
print('\nPrinting response type:\n', type(resp))
print('\nPrinting list of properties for response object :\n', dir(resp))
print('\nResponse status code:\n', resp.status_code)

assert resp.status_code == 200
