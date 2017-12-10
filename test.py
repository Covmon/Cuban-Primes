import math
import datetime

## Checks if a number is prime
def is_prime(x):
	sqroot = math.sqrt(x)
	sqroot1 = math.ceil(sqroot)
	toprange = int(sqroot1)
	for n in range(2, int(toprange+1)):
		if (x % n == 0):
			return False
	return True


cuban_primes = []

for n in range(9999900, 10000000):
	t_init = datetime.datetime.now()
	cuban = n**3 - (n-1)**3
	if is_prime(cuban):
		print n
		cuban_primes.append(cuban)
		t_final = datetime.datetime.now()
		print t_final - t_init


print sorted(cuban_primes)



