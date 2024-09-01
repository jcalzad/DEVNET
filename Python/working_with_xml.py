import xmltodict

with open("OCG_xml_sample.xml") as data:
    xml_example = data.read()

xml_dict = xmltodict.parse(xml_example)

print(xml_dict) # OrderedDict([('interface', OrderedDict([('@xmlns', 'ietf-interfaces'), ('name','GigabitEthernet2'), ('description', 'Wide Area Network'), ('enabled', 'true'),('ipv4', OrderedDict([('address', OrderedDict([('ip', '192.168.0.2'), ('netmask','255.255.255.0')]))]))]))])

# Modify an xml interface
xml_dict["interface"]["ipv4"]["address"]["ip"] = "192.168.55.3"

# Print the changes in XML format
print(xmltodict.unparse(xml_dict, pretty=True))

#Output
"""
<?xml version="1.0" encoding="UTF-8" ?>
<interface xmlns="ietf-interfaces">
  <name>GigabitEthernet2</name>
  <description>Wide Area Network</description>
  <enabled>true</enabled>
  <ipv4>
    <address>
      <ip>192.168.1.5</ip>
      <netmask>255.255.255.0</netmask>
    </address>
  </ipv4>
</interface>
"""

# Write changes to new file uses 4 spaces for indent
with open("OCG_xml_sample_changed_4spaces.xml", "w") as data:
    data.write(xmltodict.unparse(xml_dict, pretty=True))

# Write changes to new file uses 2 spaces for indent
with open("OCG_xml_sample_changed_2spaces.xml", "w") as data:
    data.write(xmltodict.unparse(xml_dict, pretty=True, indent="  "))

