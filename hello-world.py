#!/usr/bin/python

a = True
while  a == True:
	try:
		a  = int(input("Insert number: "))
	except ValueError:
		print ("Nie podales liczby")
	
if a == 10:
	print ("Hello World")
else:
	print ("Podales liczbe {} ".format(a))


