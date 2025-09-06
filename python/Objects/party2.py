class PartyAnimal():
    x = 0
    name = ""
    def __init__(self, name): # constructor
        self.name = name
        print(self.name, "constructed")

    def party(self): # method
        self.x = self.x + 1
        print(self.name, "party count", self.x)

    def __del__(self): # deconstructor
        print('I am destructed', self.x)

an = PartyAnimal("Sally")
an.party()

j = PartyAnimal("Jim")
j.party()
an.party()

"""an = 42 # destroys the object 
print('an contains', an)"""