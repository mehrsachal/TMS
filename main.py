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