import w3storage
import json
import os
from os import listdir
import pathlib
import time
import calendar
from cryptography.fernet import Fernet


#Paste web3.storage token
w3 = w3storage.API(token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDREQTVhNUREMGQxNjhiOGQzNjNCRDEzMjc5MDZERWE5NzRFQjU0MmUiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NzAzOTQ0NjA1MjAsIm5hbWUiOiJ0bXNkZXNrdG9wIn0.DbezhIwSY8tNkH2hsHM_cYwf-pc3g5W8XxoPYb3VneA')
cidlist = {} # initialize dict


def upload():
    #ITERATE WITHIN FOLDER AND UPLOAD ALL FILES
    #Upload & Write to Dict
    current_dir = str(pathlib.Path().absolute()) #Current Directory 
    folder_dir = current_dir + '\data'

    for files in os.listdir(folder_dir):
        imgpath = current_dir+'\data'+'\\' +files # jump to data folder and fetch image

        cid = w3.post_upload((open(imgpath, 'rb'))) #upload to web3 storage
        cidlist[cid] = files #write to dict
            

    #CONVERT TO JSON
    json_object = json.dumps(cidlist, indent=4)
    #Get current timestamp
    gmt = time.gmtime()
    ts = str(calendar.timegm(gmt)) + '.json' #Convert timestamp to string and add relevent file extension
    #Write to json file with latest timestamp as file name in UNIX format
    with open(ts, "w") as outfile:
        outfile.write(json_object)
    file  = open(ts, 'rb')
    id = w3.post_upload(file)
    return id