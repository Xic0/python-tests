#!/usr/bin/python --
# -*- coding: UTF-8

### Guess Number by Xic0 ###

import random

msg = dict(intro="I've chosen a random number between 1 and 1000. Try to guess it.", WIN="You've got it!!!", LOW="That's too low...", HIGH="That's too high...")
number = random.choice(range(1, 1001))
counter = 0
debug = True
min = 0
max = 1000

print msg["intro"]
while (True):
    guess = raw_input("\nYour guess: ")
    guessint = int(guess)

    if (guessint == number):
        counter += 1
        print msg["WIN"]
        print "It took you %s attempts..." % counter
        break
    elif (guessint < number):
        print msg["LOW"]
        min = guessint+1
        counter += 1
    else:
        print msg["HIGH"]
        max = guessint - 1
        counter += 1

    if debug:
        print "hint: ", min + (max - min) / 2
