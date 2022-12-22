import requests
res = requests.post('http://localhost:8000/api/token-auth/', 
                    data={'username': 'root',
                          'password': 'toor'}).json()
token = res['token']
print(token)

res = requests.post('http://localhost:8000/api/projects/', 
                    headers={'Authorization': 'JWT {}'.format(token)},
                    data={'name': 'Hello WebODM!'}).json()
project_id = res['id']