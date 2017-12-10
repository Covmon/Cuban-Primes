print "CUBAN PRIME CALCULATOR"

import datetime

nn = raw_input("Enter a number: ") 
nn = int(nn)**3-(int(nn)-1)**3

x = datetime.datetime.now()

n = int(nn) 
print n
import math 

def prime_number_identifier(x):
	print "K"
	sqroot = math.sqrt(x)
	sqroot1 = math.ceil(sqroot)
	toprange = int(sqroot1)
	for n in range(2, toprange):
		print n
		if (x % n == 0):
			return False
			break	

if prime_number_identifier(n) == False:
	print "%s" %n + " is not prime. Please try a prime number."

else:
	print "%s" %n  + " is prime."

y = datetime.datetime.now()

z = y - x	

print "The process took " + "%s" %z + " seconds." 	