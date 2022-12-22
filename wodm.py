import requests
res = requests.post('http://localhost:8000/api/token-auth/', 
                    data={'username': 'root',
                          'password': 'toor'}).json()
token = res['token']