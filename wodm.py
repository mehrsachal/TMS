import os
from pyodm import Node
n = Node('localhost', 3000)
task = n.create_task(['image1.jpg'], {'dsm': True})
task.wait_for_completion()
os.listdir(task.download_assets("results"))[0:2]