import requests
import shutil
import os
import pathlib




#NEED TO ITERATE CID FROM A LIST
current_dir = str(pathlib.Path().absolute()) #Current Directory 

for files in os.listdir(current_dir):
    if (files.endswith(".json")):
        filpath = current_dir+'\data'+'\\' +files #fetch latest json file
print(filpath)




# url = 'https://api.ipfsbrowser.com/ipfs/get.php?hash=' + cid

# #Iterate file name from list
# file_name = 'IMAGE.jpg'

# res = requests.get(url, stream = True)

# if res.status_code == 200:
#     with open(file_name,'wb') as f:
#         shutil.copyfileobj(res.raw, f)
#     print('Image sucessfully Downloaded: ',file_name)
# else:
#     print('Image Couldn\'t be retrieved')


# #DECRYPT IMAGES