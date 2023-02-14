import uploader
import ethwriter
import downloader

#upload the data folder to web3.storage and return hash of the JSON file
cid = uploader.upload()

#need mechanism to name the json file stored on web3.storage
#ethwriter.add_hash(1, cid) adds the hash of the JSON file to the smart contract
ethwriter.add_hash(1, cid)
#ethwriter.get_hash(1) returns the hash of the JSON file stored on web3.storage
pr = ethwriter.get_hash(1)
print(pr)
#downloader.downl() uses a JSON file to download the files from web3.storage

downloader.downl(pr)
# #read the log.txt file and find the latest hash id
# #add 1 to the id and fetch it using ethwriter.get_hash(id) and download it using downloader.downl()
# #repeat the process until the hash id is found in the smart contract 
# #once done, create an entry in the log.txt file of the hash id for each succesful download

# with open('log.txt', 'r') as f:
#     lines = f.readlines()
#     last_line = lines[-1]
#     last_line = last_line.split()
#     last_line = int(last_line[0])
#     last_line += 1
#     f.close()

# if ethwriter.get_hash(last_line):
#     downloader.downl(ethwriter.get_hash(last_line))
#     with open('log.txt', 'a') as f:
#         f.write(last_line)

