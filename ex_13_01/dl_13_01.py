# Import the libraries needed to parse XML
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Enter either one of the following URLS:
# url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
# url = 'http://py4e-data.dr-chuck.net/comments_1554150.xml'
url = input('Enter - ')

# Retrieve data using urllib request
data = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(data)

# Use the finall method to retrieve all the comments in the XML
lst = tree.findall('comments/comment')

# Create a list to create a running balance for count.
total = 0

# Loop through the tags and retieve the count information
for tag in lst :

    # find and grab the text from the tag 'count', convert it into integer and save to variable.
    count = int(tag.find('count').text)

    # Get a running balance 
    total = total + count

# Print the total of the data you fetched.
print(total)