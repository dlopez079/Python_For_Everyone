"""
Exercise 1

Write a program which repeatedly reads numbers until the user enters "done".  Once "done" is entered, print out the total, count, and average of the numbers.  If the user enters anything other than a number, detect their mistake using 'try' and 'except' and print an error message and skip to the next number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16  3  5.3333333333
"""
# Set the variables before the loop
num = 0  # variable that will be used for the count.
tot = 0.0 # variable that will be used for the total.

# Gather the input data from user.
num = input('Enter a number: ')

# Set the instructions that will happen after the loop
print(tot,num,tot/num)