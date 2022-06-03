"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

# Ask user to input file name.  If the input is less than 1, then default to the text file.
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

# Open file and save data to the handle.
handle = open(name)

# Create a Dictionary using the handle
counts = dict()

# Loop through the lines of the document
for line in handle:

    # Go through each line and continue if it does not start with "From "
    if not line.startswith("From "):
        continue

    # Split the lines into words
    wds = line.split()

    # The email is always index number 1. I saved it to a friendly variable.
    emails = wds[1]
    
    # Go through the emails, check if the email is there, if the email is not there, add it to the dictionary, if the email is there, increment the value by 1.
    counts[emails] = counts.get(emails, 0) + 1
    
# Create variables that will hold the high cound and email.
hc = None
he = None

# Loop through the  for both keys and values.
# Key(k) will display emails
# Value(v) will display the count.
for k,v in counts.items() :

    # Create an if statement to search for the highest value.  If the count (or value = v) is None or greater then the high count
    if hc is None or v > hc:
        he = k # key
        hc = v # value
        
# Print Desired Output
print(he,hc)