"""
6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
"""

text = "X-DSPAM-Confidence:    0.8475"

# Find the decimal point on the above 'text' using the find method and save the index to a variable.
decpos = text.find('.') # Equals 24.

# Is going to give you the length of the string. 
length = len(text) # Equals 29

# Cover the extracted value to a floating point number and print it out.
number = float(text[decpos-1:length]) #text[sr:fr] will get me the range from start to finish.  float() will make the value into a float.
print(number)