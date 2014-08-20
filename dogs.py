class Dog():
    def __init__(self, dogname, dogcolor, dogheight, dogbuild, dogmood, dogage):
        self.name = dogname
        self.color = dogcolor
        self.height = dogheight
        self.build = dogbuild
        self.mood = dogmood
        self.age = dogage
        self.Hungry = False
        self.Tired = False

    def Eat(self):
        if self.Hungry:
            print "Yum yum... Num num..."
            self.Hungry = False
        else:
            print "Sniff sniff... Not Hungry"

    def Sleep(self):
        print "ZZZZZZzzzzzzZZZZZZ"
        self.Tired = False

    def Bark(self):
        if self.mood == "Grumpy":
            print "GRRRRR.... Woof Woof"
        elif self.mood == "Laid Back":
            print "Yawn... OK... Woof..."
        elif self.mood == "Crazy":
            print "Bark Bark Bark Bark Bark Bark Bark Bark Bark Bark"
        else:
            print "Woof Woof"

Beagle = Dog("Archie", "Brown", "Short", "Chubby", "Grumpy", 12)

print "My name's %s\nMy color's %s\nMy mood is %s\n Hungry Status = %s" % (Beagle.name, Beagle.color, Beagle.mood, Beagle.Hungry)

Beagle.Eat()
Beagle.Hungry = True
Beagle.Eat()
Beagle.Bark()
