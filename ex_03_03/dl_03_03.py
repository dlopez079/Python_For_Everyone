"""
3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
"""

# Gather score from input
score = input("What is your score? ")

# Check to make sure the input is a number
try:
    # Convert input to float
    score = float(score)

# If the input is not a number, display an error message to the user and quit application.
except:
    # Print an error message to user.
    print("Enter a numberic value within range of 0.0 to 1.0")

    # Quit running the program.
    quit()

# If try and except clears, run the rest of the code.
else:

    # Make sure score is within the range and use elif to determine the grades.
    if score >=0.0 and score<=1.0: 
        if score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        elif score < 0.6:
            print("F")
    else:
        print("Enter a numberic value within rage of 0.0 to 1.1")