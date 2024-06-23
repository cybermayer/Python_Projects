import requests
from datetime import datetime

# Define the base URL for the Pixela API
URL = "https://pixe.la//v1/users"

# Replace "YOUR USER NAME" with your actual Pixela username
USERNAME = "YOUR USER NAME"

# Replace "YOUR TOKEN" with your actual Pixela token
TOKEN = "YOUR TOKEN"

# Parameters for creating a new user on Pixela
PARAMS = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Uncomment the following line to create a user on Pixela
# response = requests.post(url=URL, json=PARAMS)

# Graph ID for the new graph to be created
GID = "graph1"

# Configuration for creating a new graph
graph_confing = {
    "id": GID,
    "name": "Coding Graph",
    "unit": "project",
    "type": "int",
    "color": "shibafu"
}

# Headers for authentication using the Pixela token
headers = {
    "X-USER-TOKEN": TOKEN
}

# Uncomment the following line to create a graph on Pixela
#response = requests.post(url=f"{URL}/{USERNAME}/graphs", json=graph_confing, headers=headers)

# Endpoint for creating a pixel on the specified graph
pixel_creation_endpoint = f"{URL}/{USERNAME}/graphs/{GID}"

# Get the current date
TDY = datetime.now()

# Configuration for creating a new pixel
pixel_config = {
    "date": TDY.strftime("%Y%m%d"),  # Format the date as YYYYMMDD
    "quantity": "1"
}

# Create a pixel on the graph
response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
