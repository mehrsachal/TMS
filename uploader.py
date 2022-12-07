import w3storage

w3 = w3storage.API(token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDREQTVhNUREMGQxNjhiOGQzNjNCRDEzMjc5MDZERWE5NzRFQjU0MmUiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NzAzOTQ0NjA1MjAsIm5hbWUiOiJ0bXNkZXNrdG9wIn0.DbezhIwSY8tNkH2hsHM_cYwf-pc3g5W8XxoPYb3VneA')

#some_uploads = w3.user_uploads(size=25)


#helloworld_cid = w3.post_upload(('hello_World.txt', 'Hello, world.'))
# readme_cid = w3.post_upload((open('p5.jpg', 'rb')))
# print(readme_cid)
imag = w3.car('bafkreifi2ofdvlmawtqk7jqp6k4coccfr3izxipt6iq5odtoavdwfdqjmi')
print(format(imag))