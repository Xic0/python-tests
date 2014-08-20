#!/usr/bin/python --
# -*- coding: UTF-8

### Marvel Avengers Alliance by Xic0

class Character:
    count = 0
    chars = []

    name = ''
    type = ''
    skills = []
    effects = []
    health = 0
    stamina = 0
    attack = 0
    accuracy = 0
    defense = 0
    evasion = 0
    points = 366
    _attributes = ['name', 'type', 'skills', 'health', 'stamina', 'attack', 'accuracy', 'defense', 'evasion', 'effects']
    def __init__ (self, name):
        assert self.valid_name(name)
        self.name = name
        Character.count += 1
        Character.chars.append(name)
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
    def list ():
        """ Lists all characters defined by this class """
        print("There is {} characters:".format(Character.count))
        for c in Character.chars:
            print "\t" + c
    @staticmethod
    def valid_name(name):
        return True if bool(name) and type(name) == str else False



spidey = Character("Spider-Man")
spidey.type = "Infiltrator"
spidey.health = 117
spidey.stamina = 143
spidey.attack = 23
spidey.defense = 26
spidey.accuracy = 26
spidey.evasion = 31
spidey.effects = ['Great Responsability']
spidey.skills = ['Web Shot', 'Spider-Sense', 'Web Slingshot', 'Web Swing']
print str(spidey)
#print Character.list(-1)
print spidey.getattribute('health')
hulk = Character('Hulk')


print Character.list()


class effects:
    """ Class doc """

    def __init__ (self, name):
        """ Class initialiser """
        self.name = name
        self.description = ''
