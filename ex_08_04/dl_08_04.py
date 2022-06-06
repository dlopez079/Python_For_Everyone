"""
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
"""

# Capture input from user.
fname = input("Enter file name: ")

# Open the file name (which is located on the same directory as this python program.)
fh = open(fname)

# Create an empty list so you can save the lines into.
lst = list()

# Loop through the lines in the document
for line in fh:

        # Break lines into words
        line = line.rstrip()
        wds = line.split()
        
        # Break words into lines and append into list.
        for w in wds: 
            w.rstrip()
            w.split()
            lst.append(w)

# Convert the list into a dictionary to remove duplicates then convert back to list. 
lst = list( dict.fromkeys(lst) )
lst = list( dict.fromkeys(lst) )

# print(str)
lst.sort()

# Print List.
print(lst)