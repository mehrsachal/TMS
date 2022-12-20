# Description: This script is used to create a new project and add images to it.
import pyodm
image_path = "image.png"
# Load the project
project = pyodm.Project.from_project_path("myproject")

project.add_image(image_path)
