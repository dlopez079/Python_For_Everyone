# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

# Input for Hours
hours = input("Hours: ")

# Input for Rate
rate = input("Rate: ")

# Use the try and accept in case that users enter works instead of numbers.
try:
    # Convert the string input to float 
    hours = float(hours)
    rate = float(rate)
except:
    print("Error, please enter a numeric input for both hours and rate.")
    quit()

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
    print(totalPay)

else :  

    # Compute Gross Calculation
    gross = hours * rate

    #  Print out gross
    print(gross)