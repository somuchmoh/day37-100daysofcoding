import requests
from datetime import datetime
import os

# ---------------- CREATE A USER ACCOUNT ---------------- #
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)  # user_params is in the form of a JSON
# print(response.text)
# Since the user is now setup, you can common out the code.

# ---------------- CREATE A GRAPH ---------------- #

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPHID = "graph1"
graph_config = {
    "id": GRAPHID,
    "name": "My Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)


# ---------------- ADD A NEW PIXEL ---------------- #
data_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

today = datetime.now()
DATE = today.strftime("%Y%m%d")
data_config = {
    "date": DATE,
    "quantity": "14",
}

data_response = requests.post(url=data_endpoint, json=data_config, headers=headers)


# ---------------- UPDATE AN EXISTING PIXEL ---------------- #
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{DATE}"
update_config = {
    "quantity": "25"
}
# update_response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(update_response.text)

# Code is commoned out since I don't want to update any pixel

