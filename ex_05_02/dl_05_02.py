"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
"""
# Create the variables/lists that are required for program.
largest = None
smallest = None
nums = [] 

# Create a indefinite loop
while True:
    snum = input("Enter a number: ")
    if snum == "done":
        break
    
    # validate the input.
    try:
        inum = int(snum)
    except:
        print("Invalid input")
        continue

    # Pop value into array
    nums.append(inum)

    # Iterate throught the values in the new array.
    for value in nums:

        # Determine the smallest
        if smallest is None:
            smallest = value
        elif value < smallest:
            smallest = value

        # Determine the largest
        if largest is None:
            largest = value
        elif value > largest:
            largest = value

# Final Print Out
print("Maximum is", largest)
print("Minimum is", smallest)