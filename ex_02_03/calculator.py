# Gather first number from user using the following command:
fnum = float(input('First Number: '))

# Gather the Operator from the user using the following command:
operator = input('*,/,+,-: ')

# Gather second number from user using the following command:
snum = float(input('Second Number: '))

# If multiplication, print fnum * snum
if operator == '*' :
    answer = fnum * snum
    print(fnum, operator, snum, '=', answer )

# If division, print fnum / snum
if operator == '/' :
    answer = fnum / snum
    print(fnum, operator, snum, '=', answer )

# If addition, print fnum + snum
if operator == '+' :
    answer = fnum + snum
    print(fnum, operator, snum, '=', answer )

# If subtraction, print fnum - snum
if operator == '-' :
    answer = fnum - snum
    print(fnum, operator, snum, '=', answer )