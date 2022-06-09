# Create a PartyAnimal Class
class PartyAnimal:
    
    # Create a variable to increment
    x = 0

    # Create a empty string variable
    name = ""

    # IT IS IMPORTANT TO REMEMBER THAT SELF EQUALS THE OJBECT THAT YOU ARE PASSING THROUGH THE CLASS. 
    # THE VARIABLE (OR OBJECT) (s) WILL CREATE ONE INSTANCE.
    # THE VARIABLE (OR OBJECT) (j) WILL CREATE ANOTHER INSTANCE.
    # Initialize the Contructor for name.
    def __init__(self, z):

        # Pass in the name and save it to this present instance of name.
        self.name = z

        # Print out the constructor with name.
        print(self.name, "constructed")

    # Initialize the constructor for the count.
    def party(self):

        # Increment the variable X
        self.x = self.x + 1

        print(self.name, "party count",self.x)

    
# Save the class to a variable and pass 'Sally' as a name.
s = PartyAnimal("Sally")

# Run the class using the variable and grab the party method that's inside.
s.party()

# Save the class to a variable and pass 'Jim' as a name.
j = PartyAnimal('Jim')

# Run the class using the variable and grab the party method that's inside.
j.party()

# Re-run the first class which contains the variable (or object) 's' so you can see the two instances.
s.party()