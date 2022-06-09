# Class is a reserved word.
# This is the template for making PartyAnimal objects.
class PartyAnimal:

    # Each PartyAnimal object has a bit of data.
    x = 0

    # Each PartyAnimal object has a bit of code.
    def party(self):
        self.x = self.x + 1
        print("So Far", self.x)

# Construct a PartyAnimal Object and store in an variable.
an = PartyAnimal()

# Tell the 'an' object to run the party() code within it.
an.party()

# An is equal to PartyAnimal() so the following code is the same.
PartyAnimal.party(an)

# What is the type of an
print('Type', type(an))

# What is the Dir of an
print('Dir', dir(an))