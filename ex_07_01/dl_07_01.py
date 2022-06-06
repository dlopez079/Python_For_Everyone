"""
7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
"""

# Use words.txt as the file name
# Save the data from the entered file into a variable.
fname = input("Enter file name: ")

# Open the file name that is saved in the input variable.
fh = open(fname)

# Read the text from the document and apply upper case using the upper method.
inp = fh.read().upper().strip()

# Pring the inpp
print(inp)