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

print(project_id)


images = [
    ('images', ('image1.jpg', open('image1.jpg', 'rb'), 'image/jpg')), 
    ('images', ('image2.jpg', open('image2.jpg', 'rb'), 'image/jpg')),

]
options = json.dumps([
    {'name': "orthophoto-resolution", 'value': 24}
])

res = requests.post('http://localhost:8000/api/projects/{}/tasks/'.format(project_id), 
            headers={'Authorization': 'JWT {}'.format(token)},
            files=images,
            data={
                'options': options
            }).json()

task_id = res['id']