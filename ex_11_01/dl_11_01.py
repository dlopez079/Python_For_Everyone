"""
Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
"""
# Import RE Library
import re

# Gather an iput from the user to open up a file.
name = input("Enter file (regex_sum_42.txt or regex_sum_1554146.txt): ")

# If there is no name entered, I defaulted to the assignment data file.
if len(name) < 1:
    name = "regex_sum_1554146.txt"

# Establish a hanlde after opening the file.
handle = open(name)

# Create a list to store the numbers I find on the file.
nums = list()

# Go through each line on the document
for line in handle: 

    # [x] Search for the digits on the document for each line.
    digits = re.findall('[0-9]+', line)

    # Combine all line lists into a large list.
    nums = nums + digits

# Use variable to get a running balance begining with 0
total = 0

# Go through the nums list
for num in nums:

    # [x] Convert String to Integer.
    num = int(num)

    # [x] Add num to total to get running total
    total = total + num

# Print the total and the type of the total
print(total, type(total))


