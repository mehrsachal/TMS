import pyodm
project_path = "myproject"
# Add an image to the project
image_path = "image.png"
pyodm.add_to_project(project_path, image_path)

# Process the image
pyodm.process(project_path, tasks=["orthophoto"])
