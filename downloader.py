import requests
import shutil
import os
import pathlib
import json
from cryptography.fernet import Fernet


#NEED TO ITERATE CID FROM A LIST
current_dir = str(pathlib.Path().absolute()) #Current Directory 

for files in os.listdir(current_dir):
    if (files.endswith(".json")):
        filpath = current_dir + '\\'+files #fetch latest json file
print(filpath)


j = open(filpath)
  
data = json.load(j)
  
#Iterating through the json file
for i in data:
    cid=i
    file_name=data[i]
    url = 'https://' + cid +'.ipfs.w3s.link'
    savpath = 'downloads\\' + file_name
    res = requests.get(url, stream = True)

    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        
        
        shutil.move(file_name, savpath)
        print('Image sucessfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved')



j.close()