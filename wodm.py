import pyodm

client = pyodm.Client("http://localhost:8000", "root", "toor")

project = client.projects.create(name="My Project", description="This is my project")
print("Project created with ID:", project.id)
