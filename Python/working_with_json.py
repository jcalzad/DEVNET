import json

# open the json file as 'data'
with open("OCG_json_sample.json") as data:
    #assign the contents to a variable
    json_data = data.read()

# create a dictionary and load the json data from the previous variable
json_dict = json.loads(json_data)

# print the dictionary
print(json_dict) # {'interface': {'name': 'GigabitEthernet1', 'description': 'Router Uplink', 'enabled': True, 'ipv4': {'address': [{'ip': '192.168.1.1', 'netmask': '255.255.255.0'}]}}}

# Modify/update the interface description - 2 tiers down
json_dict["interface"]["description"] = "Backup Link"

# print the updated json dictionary
print(json_dict) #{'interface': {'name': 'GigabitEthernet1', 'description': 'Backup Link', 'enabled': True, 'ipv4': {'address': [{'ip': '192.168.1.1', 'netmask': '255.255.255.0'}]}}}


# Modify/update the interface ipv4 address - 3 tiers down

"""
Originally had they following:

json_dict["interface"]["ipv4"]["address"] = "10.1.1.1"

which output the following:

{'interface': {'name': 'GigabitEthernet1', 'description': 'Backup Link', 'enabled': True, 'ipv4': {'address': '10.1.1.1'}}}

What happened to the netmask???

The issue arises because the original JSON structure for the address field is a list of dictionaries, 
but in your script, you are directly assigning a string to json_dict["interface"]["ipv4"]["address"], 
which changes the type of address from a list to a string. This results in the loss of the netmask field.

Corrected line to preserve is below.
"""

json_dict["interface"]["ipv4"]["address"][0]["ip"] = "10.1.1.1" 

# print the updated json dictionary
print(json_dict) # {'interface': {'name': 'GigabitEthernet1', 'description': 'Backup Link', 'enabled': True, 'ipv4': {'address': [{'ip': '10.1.1.1', 'netmask': '255.255.255.0'}]}}}

"""
We need the [0] because the address field is a list of dictionaries
and we are working with the first one.
"""

# Modify/update the interface ipv4 netmask
json_dict["interface"]["ipv4"]["address"][0]["netmask"] = "255.255.255.255"

# print the updated json dictionary
print(json_dict) # {'interface': {'name': 'GigabitEthernet1', 'description': 'Backup Link', 'enabled': True, 'ipv4': {'address': [{'ip': '10.1.1.1', 'netmask': '255.255.255.255'}]}}}

with open("OCG_json_sample_changed.json", "w") as fh:
    json.dump(json_dict, fh, indent = 4)
    