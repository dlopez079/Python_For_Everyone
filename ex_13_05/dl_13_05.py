# Import the Json Library
import json

# JSON data will resemble what is in the comments
# JSON respresents data as nested "lists" and "dictionaries"
data = """ {
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
        },
    "email" : {
        "hide" : "yes"
        }
    }
    """

# Pass the json through the loads method which comes from the json library and save the results into a variable. (info)
# Change from string to an object using the loads method.  This may blow up and give you tracebacks.  If it does, there there is someone wrong with the JSON.
info = json.loads(data)

# Print the content in which you extracted located in info.
# Fetch the data using key value pairs.
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

# Here is an example of a list.
# This list has two dictionaries in it. 
input = """[
    {   
        "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    },
    {
        "id" : "009",
        "x" : "7",
        "name" : "Chuck"
    }
]
"""

# Pass the Input throw the loads method from the JSON library and turn the string into an object.
info = json.loads(input)

# Pring the length of the list.
print("User count: ", len(info))

# Loop through the items of this list
for item in info:

    # Print the names on this list.
    print('Name:', item['name'])

    # Print the IDs on this list.
    print('Id:', item['id'])

    # Print the Attribute (x) of the list
    print('Attribute', item['x'])