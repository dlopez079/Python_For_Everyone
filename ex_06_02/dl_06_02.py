# String Concatenation
# When the + operator is applied to strings, it means "concatenation"
a = 'Hello'
b = a + 'There'
print(b)
c = a + ' ' + 'There'
print(c)
print('**********')

# Using in as a Logical Operator
# The in keyword can also be used to check to see if one string is "in" another string.

fruit = "banana"

print('n' in fruit) # returns True
print('m' in fruit) # returns False
print('nan' in fruit) # returns True
if 'a' in fruit: 
    print('Found it!')
print('**********')

# Python has a number of string functions which are in the string library
# These functions are already built into every string - we invoke them by appending the afunction to the string variable.
# These function do not modify the original string, instead they return a new string that has been altered.
greet = "Hello bob"
zap = greet.lower()
print(zap)
print(greet)
print("Hi there".lower())
print('**********')

# Searching a String
# We use the find() function to search for a substring within another string
# find() finds the first occurence of the substring
# If the substring is not found, find() returns -1
# Remember that string position starts at zero
pos = fruit.find('na')
print(pos)
aa = fruit.find('z')
print(aa)
print('**********')

# Sometimes we want to take a string and remove whitespace at the beginning and/or end
# Istrip() and rstrip() remove whitespace at the left or right
# strip() removes both beginning and ending whitespace
greet = "   Hello Bob   "
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())
print('**********')

# Prefixes
line = 'Please have a nice day'
print(line.startswith('Please'))
print(line.startswith('p'))
print('**********')

