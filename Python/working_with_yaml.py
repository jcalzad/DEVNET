import yaml


with open("OCG_yaml_sample.yaml") as data:
    yaml_sample = data.read()

# Convert the yaml file to a dictionary
yaml_dict = yaml.load(yaml_sample, Loader=yaml.FullLoader)

# Print the dictionary
print(yaml_dict) # {'interface': {'name': 'GigabitEthernet2', 'description': 'Wide Area Network', 'enabled': True, 'ipv4': {'address': [{'ip': '172.16.0.2', 'netmask': '255.255.255.0'}]}}}

# Change parameters
yaml_dict["interface"]["name"] = "GigabitEthernet1"
yaml_dict["interface"]["ipv4"]["address"][0]["ip"] = "10.1.1.1"
yaml_dict["interface"]["ipv4"]["address"][0]["netmask"] = "255.255.255.255"

# Print in yaml format
print(yaml.dump(yaml_dict, default_flow_style=False))

#Output
"""
interface:
  description: Wide Area Network
  enabled: true
  ipv4:
    address:
    - ip: 172.16.0.2
      netmask: 255.255.255.0
  name: GigabitEthernet2
"""

# Write to new yaml file
with open("OCG_yaml_sample_changed.yaml", "w") as data:
    data.write(yaml.dump(yaml_dict, default_flow_style=False))
