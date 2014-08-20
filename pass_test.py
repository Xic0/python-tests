#!/usr/bin/python --

users = ["sasuke", "naruto", "shika"]
passwords = ["uchiha", "uzumaki", "nara"]

usrname = raw_input('Enter your username => ')
pwd = raw_input('Enter your password => ')

if usrname in users:
	position = users.index(usrname)
	if pwd == passwords[position]:
		print "Hi there, %s. Access Granted." % usrname
	else:
		print "Password Incorrect. Access Denied."
else:
	print "Sorry... I don't recognize you. Access Denied."
