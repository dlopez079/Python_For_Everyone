"""
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

# Establish an accumulator so you can increment the amount of lines that start with X-DSPAM...
count = 0 

# Establish an accumulator total so you can add the numbers that are in each of the lines.
num = 0 
total = 0

for line in fh:

    # Go through each line and continue if it does not start with x=DSPAM-Confidence
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    # Find the number 
    ppos = line.find('.')
    num = float(line[ppos-1:len(line)])

    # Get running total
    total = float(total) + num

    count = count + 1  
    ## Get a running balance 

print('Average spam confidence:', total/count)

