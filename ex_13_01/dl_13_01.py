import xml.etree.ElementTree as ET

input = 'http://py4e-data.dr-chuck.net/comments_42.xml'
print(input)
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))