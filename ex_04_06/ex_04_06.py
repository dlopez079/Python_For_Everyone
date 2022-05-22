"""
4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.
"""

# Gather hours from user input
hours = input("Hours: ")

# Gather rate of pay from user input.
rate = input("Rate: ")

# Create a function to compute the pay for the data input by user.
def computepay(hours, rate):

    # Check to see if there are overtime hours.
    if hours > 40 :

        # Run rate for first 40 hours
        regularPay = 40 * rate

        # Over Time Hours
        overtimeHours = hours - 40

        # Over Time Rate
        overTimeRate = rate * 1.5

        # Run rate for the hours above 40.
        overTimePay = overtimeHours * overTimeRate

        # Get Total Pay
        totalPay = regularPay + overTimePay

        # Print Total Pay
        return(totalPay)

    else :  
        # Compute Gross Calculation
        totalPay = hours * rate

        #  Print out gross
        return(totalPay)


# Check to make sure the input is a number and not a string
try:
    # Convert input to float
    hours = float(hours)
    rate = float(rate)

# If the input is not a number, display an error message to the user and quit application.
except:
    # Print an error message to user.
    print("Enter a numberic value")

    # Quit running the program.
    quit()

# If try and except clears, run the rest of the code.
else:

    # Invoke the compute function that you created earlier.
    print("Pay", computepay(hours, rate))