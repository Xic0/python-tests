#!/usr/bin/python --
# -*- coding: UTF-8

### Marvel Avengers Alliance by Xic0

class iso8:
    def __init__(self, Type, Color):
        self.type = Type
        self.color = Color
        self.cost = 0
        self.attack = 0
        self.accuracy = 0
        self.defense = 0
        self.evasion = 0
        self.health = 0
        self.stamina = 0
        self.pvp = dict(offense=0, defense=0)
    def __str__(self):
        return "This is an ISO-8 %s %s and cost %d. It has an accuracy of +%d" % (self.color, self.type, self.cost, self.accuracy)

chipRedPrecise = iso8("Chip", "Red")
chipRedPrecise.cost = 1300
chipRedPrecise.accuracy = 6
chipRedPrecise.pvp['offense'] = 32
chipRedPrecise.pvp['defense'] = 17

print chipRedPrecise.__str__

class Character:
    name = ''
    type = ''
    skills = ''
    health = 0
    stamina = 0
    attack = 0
    accuracy = 0
    defense = 0
    evasion = 0
    points = 366
    _attributes = ['name', 'type', 'skills', 'health', 'stamina', 'attack', 'accuracy', 'defense', 'evasion']
    def __init__ (self, name):
        #assert self.valid_name(name)
        self.name = name
    def getattribute(self, attribute):
        return eval("self." + attribute) if attribute in self._attributes else "### ERROR ###"
    def setattribute(self, attribute, ammount):
        eval("self." + attribute + " = " + ammount) if attribute in self._attributes else "### ERROR ###"
    def addPoints(self):
        accepted = ['health', 'stamina', 'attack', 'accuracy', 'defense', 'evasion']
        accepted_dict = dict(enumerate(accepted, start=1))
        prompt = "\nWich attribute?\n\t" + "\n\t".join("%d. %s"%n for n in accepted_dict.items())+"\n?"
        attribute = False
        while attribute not in accepted:
            attribute = raw_input(prompt)
            try:
                attribute = accepted_dict[int(attribute)]
            except:
                print "Input was invalid."
            amount = None
            while type(amount) != int or amount > self.points:
                try:
                    amount = int(raw_input("By how much?"))
                    assert amount <= self.points
                except AssertionError:
                    print "You do not have that many points remaining"
                except:
                    print "You must enter an integer amount"
        self.setattribute(attribute, self.getattribute(attribute) + amount)
        self.points -= amount
    def __str__(self):
        return "\n".join("%s\t:\t%s"%(n, self.getattribute(n)) for n in self._attributes)

    @staticmethod

    def valid_name(name):
        return True if bool(name) and type(name) == str else False

    #if __name__ == "__main__":
        #running = True
        #print "Create a character! You have points to assign to strength, health, wisdom, and dexterity."
        #name = ''
        #while not character.valid_name(name):
            #name = raw_input("Please enter your character's name:")
        #CHAR = character(name)
        #OPTIONS_LIST = ["Add points", "Remove points", "See current attributes", "Exit"]
        #OPTIONS_DICT = dict(enumerate(OPTIONS_LIST, start=1))
        #PROMPT = "\n".join("\t%d. %s"%n for n in OPTIONS_DICT.items())+"\nChoice:"
        #while running:
            #CHOICE = raw_input(PROMPT)
            #try:
                #CHOICE = int(CHOICE)
            #except:
                #pass
            #if CHOICE in OPTIONS_DICT.keys():
                #CHOICE = OPTIONS_DICT[CHOICE]
            #if CHOICE == "Add points":
                #CHAR.add_points()
            #elif CHOICE == "Remove points":
                #raise NotImplementedError()
            #elif CHOICE == "See current attributes":
                #print CHAR
            #elif CHOICE == "Exit":
                #break

spidey = Character("Spider-Man")
spidey.type = "Infiltrator"
print str(spidey)




class Dog:
    count = 0 # this is a class variable
    dogs = [] # this is a class variable

    def __init__(self, name):
        self.name = name #self.name is an instance variable
        Dog.count += 1
        Dog.dogs.append(name)

    def bark(self, n): # this is an instance method
        print("{} says: {}".format(self.name, "woof! " * n))
    @staticmethod
    def rollCall(n): #this is implicitly a class method (see comments below)
        print("There are {} dogs.".format(Dog.count))
        if n >= len(Dog.dogs) or n < 0:
            print("They are:")
            for dog in Dog.dogs:
                print("  {}".format(dog))
        else:
            print("The dog indexed at {} is {}.".format(n, Dog.dogs[n]))

#fido = Dog("Fido")
#fido.bark(3)
#Dog.rollCall(-1)
#rex = Dog("Rex")
#Dog.rollCall(-1)
#Dog.rollCall(6)
#Dog.rollCall(0)
#Dog.rollCall(1)


