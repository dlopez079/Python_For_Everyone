"""
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""

# Gather file information from user.
fname = input("Enter file name: ")

# If the length of the file name is less than 1; then default the value to the file name.
if len(fname) < 1:
    fname = "mbox-short.txt"

# Open the file and save the data to a variable.
fh = open(fname)

# Create a count variable so you can summarize the count later.
count = 0

# Go through lines in the document.
for line in fh:

    # Go through each line and continue if it does not start with "From "
    if not line.startswith("From "):
        continue

    # If it starts with "From ", strip and split the data.
    wds = line.rstrip().split()

    # Pull the value from the number 1 index of the list.
    email = wds[1]

    # Print the email
    print(email)

    # Increment the count.
    count = count +1

print("There were", count, "lines in the file with From as the first word")
