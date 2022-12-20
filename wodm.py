import os
from pyodm import Node
n = Node('139.177.187.136', 8000)
task = n.create_task(['image.png'], {'dsm': True})
task.wait_for_completion()
os.listdir(task.download_assets("results"))[0:2]