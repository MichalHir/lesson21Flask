import json

my_contacts = [
    {"name": "Ran", "age": 44, "email": "admin@", "phone": 6546895865, "fav":True},
    {"name": "aviad", "age": 21, "email": "admin@", "phone": 6546895865, "fav":False},
    {"name": "tal", "age": 25, "email": "admin@", "phone": 6546895865, "fav":False},
]
# Specify the path to your JSON file
file_path = 'data.json'

# Open the file in write mode
with open(file_path, 'w') as f:   # f=open()
    json.dump(my_contacts, f)

#########################################
# Read data from the JSON file
with open(file_path, 'r') as f:
    loaded_data = json.load(f)
