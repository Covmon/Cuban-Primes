import math
import datetime
t_start = datetime.datetime.now()

## Checks if a number is prime
def is_prime(x):
	sqroot = math.sqrt(x)
	sqroot1 = math.ceil(sqroot)
	toprange = int(sqroot1)
	for n in range(2, int(toprange+1)):
		if (x % n == 0):
			return False
	return True

## Checks if a number is prime and that number % 3 == 1
def is_factor_of_cuban_prime(x):
	if is_prime(x) and x % 3 == 1:
		return True

## Comment
x = 2
cuban_prime_factors = []
while x < 17320:
	if is_factor_of_cuban_prime(x):
		cuban_prime_factors.append(x)
	x += 1

new_list = []

#print cuban_prime_factors


for prime in cuban_prime_factors:
	for num in range(0, int(prime)):
		#while num < 900:
			#num += prime
		cuban_number = ((num)**3 - (num-1)**3)
		if cuban_number % prime == 0 and cuban_number != prime:
			while num < 1000:
				new_list.append(num)
				num += prime


print sorted(new_list)
t_final = datetime.datetime.now()
print "Runtime: " + str(t_final - t_start)


