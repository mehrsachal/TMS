import uploader
import ethwriter
import downloader

cid = uploader.upload()
ethwriter.add_hash(1, cid)

pr = ethwriter.get_hash(1)
print(pr)

downloader.downl(pr)