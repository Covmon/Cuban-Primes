import math
import datetime
xx = datetime.datetime.now()

def prime_number_identifier(x):
	sqroot = math.sqrt(x)
	sqroot1 = math.ceil(sqroot)
	toprange = int(sqroot1)
	for n in range(2, int(toprange+1)):
		if (x % n == 0):
			return False
			break	
x = 2
listt = []
while x < 17320:
	if prime_number_identifier(x) != False and x % 3 == 1:
		listt.append(x)
	x += 1	

new_list = []

for x in listt:
	for l in range(0,int(x)):
		while l < 900:
			l += x	
		y = ((l)**3 - (l-1)**3)
		if y % x == 0 and y != x:
			while l < 1000:
				new_list.append(l)
				l += x


print sorted(new_list)
y = datetime.datetime.now()
print y - xx