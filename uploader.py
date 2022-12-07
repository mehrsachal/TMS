import w3storage
import json


w3 = w3storage.API(token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDREQTVhNUREMGQxNjhiOGQzNjNCRDEzMjc5MDZERWE5NzRFQjU0MmUiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NzAzOTQ0NjA1MjAsIm5hbWUiOiJ0bXNkZXNrdG9wIn0.DbezhIwSY8tNkH2hsHM_cYwf-pc3g5W8XxoPYb3VneA')
cidlist = {}

#some_uploads = w3.user_uploads(size=25)

#ITERATE WITHIN FOLDER AND UPLOAD ALL FILES

#ENCRYPT IMAGES
cid = w3.post_upload((open('p5.jpg', 'rb')))

#SAVE ALL FILES AS JSON STRING WITH FILE TYPES AND CID.


cidlist[filename] = cid #write to dict
print(cidlist)

# Serializing json
json_object = json.dumps(cidlist, indent=4)

# Writing to file
with open("timestampedname.json", "w") as outfile:
	outfile.write(json_object)


