#!/usr/bin/python --
# -*- coding: UTF-8

### Dice by Xic0 ###

import random

DIE = range(1, 7)              # Standard die

### Non Numeric Dice
DIE_POKER = ["Ace", "King", "Queen", "Jack", "Ten", "Nine"]
DIE_BICHA_NAME = ["Jessica", "Gisela", "Gabriela", "Gabi", "Kiki", "Armanda", "Rica", "Marigold", "Nani", "Suéli", "Lídia", "Nádia", "Deborah"]
DIE_BICHA_MIDDLE = ["Rosa", "Fushia", "Vibrante", "Escarlate", "Creme", "do Rio", "Esfoliante", "Unhas", "Rímel", "Banana", "Implantes"]
DIE_BICHA_LAST = ["da Avon", "da Oriflame", "Nivea", "de fungos", "People", "Azul-Banana", "Pipino", "de Lama", "Murcha", "da Conceição", "do LiDL", "de Crystal"]

### Non Cubic Dice
DIE_PLATONIC4 = range(1, 5)             # tetrahedron
DIE_PLATONIC8 = range(1, 9)             # octahedron
DIE_PLATONIC12 = range(1, 13)           # dodecahedron
DIE_PLATONIC20 = DIE_MTG = range(1, 21) # icosahedron AKA Magic The Gathering Die
DIE_NC10 = range(1, 11)                 # pentagonal trapezohedron

def Roll (die_set, turns=1):
    rolled = []
    if turns == 1:
        return random.choice(die_set)
    else:
        for i in xrange(turns):
            rolled.append(random.choice(die_set))
        return rolled

def BICHA ():
    return Roll(DIE_BICHA_NAME), Roll(DIE_BICHA_MIDDLE), Roll(DIE_BICHA_LAST)

### TESTS ###
#print "Your Magic The Gathering Life: %s" % Roll(DIE_MTG)
#print "Your Dice Poker Roll: %s" % Roll(DIE_POKER, 5)


#while (True):
#    key = raw_input("\nDo you want to roll the dice? [y/n]")
#    if (key.upper() == 'Y'):
#        #print "You rolled ", Roll(DIE)
#        print " ".join(BICHA())
#    else:
#        print "\nOK THANKS BYE!\n"
#        break
###

for i in xrange(10):
    print str(i) + " - " + " ".join(BICHA())
