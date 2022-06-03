# Definite Loops and Dictionaires

# Even though dictionaires are not stored in order, we can write a for loop that goes through all the keys in the dictionary and looks up the values.

# Example
# Lets say you have a bag of 3 names and you want to keep count of the names that you pull out.  
counts = { 'chuck' : 1, 'fred' : 42, 'jan' : 100 }

# loop though the count using the key withing the counts dictionary
for key in counts:

    # Print out the key and pull the value of the key using brackets.
    print(key, counts[key])

"""
You should get the following: 
chuck 1
fred 42
jan 100
"""
print('**********')
# Retrieving lists of keys and values.

jjj = { 'chuck' : 1 , 'fred': 42, 'jan' : 100 }

# Use list to convert the dictionary to a list.  This will only bring in the keys
print(list(jjj)) # Should get ['chuck', 'fred', 'jan']

# Use the keys method to grab the keys from the Dictionaries
print(jjj.keys()) # Should get dict_keys(['chuck', 'fred', 'jan' ])

# Use the value method to grab the keys from the Dictionaries
print(jjj.values()) # Should get dict_values([ '1', '42', '100' ])

# Use the items method to grab the set from the Dictionaries ***Tuple
print(jjj.items()) # Should get dict_items([ ('chuck', 1), ('fred', 42), ('jan', 100) ])

print('**********')

# Bonus: Two Iteration Variables (using the same dictionary jjj )
for k,v in jjj.items() : 
    # print the keys (k) and values (v)
    print(k,v)

stuff = dict()
print(stuff.get('candy',-1))