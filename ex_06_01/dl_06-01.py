str = 'banana'

# Every string is considered a list.  
# For example str[0] will equal the first letter (b), str[3] will equal (a)
print(str[0],str[3])

print('**********')
# Looping through strings
# Using a while statement and iteration variable, and the lend function, we can contruct a loop to look at each of the letters in a string individually
index = 0 # Establish the before statement or starting statment for index.

# While the index is less then the length of the string, perform this infinite loop.
# This should run 6 times.
while index < len(str):

    # Pull the letter that corresponds to the index of the list.
    letter = str[index]

    # Print both the index number and the letter that corresponds with that number.
    print(index, letter)

    # Increment the index variable and check through while loop.
    index = index + 1

print('**********')
# A Definite loop using a for statement is much more elegant
# The iteration variable is completely taken care of by the for loop
# Pull value from str list and save it in letter, print it out and go through loop again.
for letter in str:

    # Print the value saved in the letter variable that was pulled from the str
    print(letter)

print('**********')
# Looping and counting
# This is a simple loop that loops through each letter in a string and counts the number of times the loop encounters the 'a' character.
count = 0 # Establish the start count
for letter in str:

    # Evaluate the value that is pulled from str and see if it is equal to 'a'
    if letter == 'a':

        # If it is equal to 'a', increment the count variable.
        count = count + 1

# Print out the Count variable.
print(count)
print('**********')

# We can also look at any continuous section of a string using a colon operator
# The second number is one beyond the end of the slice-"up to but not including"
# If the second number is beyond the end of the string, it stops at the end
# Print out all the characters from the starting point to the 2 digit
print(str[0:3])

# If we leave off the first number or the last number of the slice, it is assumed to be the beginning or end of the string respectivity.
print(str[:2], str[3:], str[:])