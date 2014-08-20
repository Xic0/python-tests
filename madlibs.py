#!/usr/bin/python --
# -*- coding: UTF-8

### Mad Libs by Xic0 ###


madlib = "My \"Dream Man\" should, first of all be very %s and %s. He should have a physique like %s, a profile like %s, and the intelligence of a/an %s. He must be polite and must always remember to %s my %s, to tip his %s and to take my %s when crossing the street. He should move %s, have a/an %s voice, and should always dress %s. I would also like him to be a/an %s dancer, and when we are alone he should whisper %s nothings into my %s and hold my %s. I know a/an %s is hard to find. In fact the only one I can think of is %s"

adjective = range(6)
noun = range(4)
celeb = range(2)
adverb = range(2)
body = range(2)

adjective[0] = raw_input("Adjective: ")
adjective[1] = raw_input("Adjective: ")
celeb[0] = raw_input("Celebrity: ")
celeb[1] = raw_input("Celebrity: ")
animal = raw_input("Animal: ")
verb = raw_input("Verb: ")
noun[0] = raw_input("Noun: ")
noun[1] = raw_input("Noun: ")
body[0] = raw_input("Part of Body: ")
adverb[0] = raw_input("Adverb: ")
adjective[2] = raw_input("Adjective: ")
adverb[1] = raw_input("Adverb: ")
adjective[3] = raw_input("Adjective: ")
adjective[4] = raw_input("Adjective: ")
body[1] = raw_input("Part of Body: ")
adjective[5] = raw_input("Adjective: ")
noun[2] = raw_input("Noun: ")
noun[3] = raw_input("Noun: ")
person = raw_input("Person in room (male): ")

print madlib % (adjective[0], adjective[1], celeb[0], celeb[1], animal, verb, noun[0], noun[1], body[0], adverb[0], adjective[2], adverb[1], adjective[3], adjective[4], body[1], adjective[5], noun[2], noun[3], person)
