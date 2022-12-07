import requests
import shutil

cid= 'bafkreifi2ofdvlmawtqk7jqp6k4coccfr3izxipt6iq5odtoavdwfdqjmi'
#NEED TO ITERATE CID FROM A LIST

url = 'https://api.ipfsbrowser.com/ipfs/get.php?hash=' + cid

#STORE DIFFERENT FILETYPES WITH INDICATOR
file_name = 'IMAGE.jpg'

res = requests.get(url, stream = True)

if res.status_code == 200:
    with open(file_name,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    print('Image sucessfully Downloaded: ',file_name)
else:
    print('Image Couldn\'t be retrieved')


#DECRYPT IMAGES