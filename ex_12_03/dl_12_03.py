# Inport the libraries needed to scrape using beautiful Soup
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Enter the URL for the 
url = input('Enter - ')

# Read the URL and parse using BeautifulSoup
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')

# Create a variable to keep the total the numbers extracted.
total = 0

# Create a variable to keep the count.
count = 0

# Loop through the span tags
for tag in tags:

    # Pull all numbers from the span tag.
    nums = int(tag.contents[0])

    # Create a running balance for all numbers and save it into total
    total = total + nums

    # Increment the count.
    count = count + 1

# Pring the Output for both the count and the sum
print('Count', count, '\nSum', total)
