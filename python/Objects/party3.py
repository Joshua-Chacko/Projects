class PartyAnimal():
    x = 0
    name = ""
    def __init__(self, name): # constructor
        self.name = name
        print(self.name, "constructed")

    def party(self): # method
        self.x = self.x + 1
        print(self.name, "party count", self.x)

class FootballFan(PartyAnimal): # do footballFan extends PartyAnimal
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)


s = PartyAnimal('Sally')
s.party()

j = FootballFan('Jim') # allows jim to use the methods of both classes
s.party()
j.touchdown()
