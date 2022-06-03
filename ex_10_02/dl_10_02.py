"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

# Gather an input from the user to open up the file mbbox-short.txt
name = input("Enter file:")

# If there is no name entered, default to the file we need to open.
if len(name) < 1:
    name = "mbox-short.txt"

# Establish a handle after opening the file.
handle = open(name)

# Create a dictionary to remove the duplicates
hrs = dict()

# Got through each line and print save each line inside the variable line.
for line in handle :
    
    # Search only lines that begining with 'From '.  Pass the lines that do not start with 'From '.
    if not line.startswith('From ') :
        continue
    
    # Split the line into sections
    section = line.split()
    
    # Grab the time from the section
    time = section[5]
    
    # Grab the hour
    # Get location of the first colon
    colon = time.find(':')

    # Use splice range to grab hour.
    hour = time[colon-2:colon]
    
    # Insert key value pairs into hrs.
    hrs[hour] = hrs.get(hour, 0) + 1

# Print out the key value part for the sorted tuple
for k,v in sorted(hrs.items()):
    print(k,v)

