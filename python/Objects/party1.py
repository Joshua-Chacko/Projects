class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 1
        print('So far' , self.x)

an = PartyAnimal() # has a type of PartyAnimal

print('Type', type(an))
print('Dir', dir(an))

# the same as PartAnimal.party(an) 
# so party sets the self as an inside of the class PartyAnimal
an.party() 
an.party()
an.party()