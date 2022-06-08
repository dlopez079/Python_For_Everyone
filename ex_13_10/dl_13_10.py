import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Prompt user for a URL
# URL should be either http://py4e-data.dr-chuck.net/comments_42.json or http://py4e-data.dr-chuck.net/comments_1554151.json
url = input('Enter: ')
# url = 'http://py4e-data.dr-chuck.net/comments_42.json'

# Display confirmation of URL that you are retrieving
print('Retrieving', url)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Establish connection using urllib to the URL provided in input.
connection = urllib.request.urlopen(url, context=ctx)

# Read what you get back from the connection and save it into a data variable.
data = connection.read()

# You will get a string back so you wantt to have the json module read the data and save it into a varable that will be type dictionary
info = json.loads(data)

# Print the ccount as requested by excercise. 
print('Count:', len(info['comments']))

# Variable for running total.
total = 0

# Inside of info are two key value pairs.  One is for note and the other is for comments.
# Comments is a list of objects that have key value pairs of name and count.
# I looped through the comments 'info['counts'] and pulled out the count. 
for item in info['comments']:
    
    # Pull the counts and saved it to a variable.
    count = (item['count'])

    # Everytime we loop, we add to the previous number.
    total = total + count

# Print the total.
print('Sum', total)


