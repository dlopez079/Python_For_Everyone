# Import the libraries needed to scape using beautiful soup.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Gather Input from user.
url = input('Enter URL:')
inCount = int(input('Enter Count:'))
position = int(input('Enter Position:')) - 1
# Establish Count for increment comparison to incount.
count = 0

# While loop to keep looping through urls
while count < inCount: 

    # Increment the count.
    count = count + 1
    print('Count', count)
    print('Scanning', url)
    
    # Have Beautiful Soup read the document and parse everything.
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve all of the anchor tags
    tags = soup('a')

    # Empty out old lists from previous loop
    names = list()
    links = list() 
    # Hope or loop through the tags.
    for tag in tags:

        # Get Name from Anchor tag
        name = tag.contents[0]

        # Get Link from Anchor Tag.
        url = tag.get('href', None)

        # Append the name for the page to the names list.
        names.append(name)

        # Append the url for the page.
        links.append(url)

    # Save the new names and links for next loop.
    name = names[position]
    url = links[position]
    

    print('Name', name)
    print('Names', names)
    
    
# Print out name.
print(name)
