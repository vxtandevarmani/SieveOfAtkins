import random

def SieveOfAtkin(limit):
	import math

	primes = {2, 3, 5}
	bound = int(math.sqrt(limit)) + 1
	for x in range(1, bound):       # limit + 1
		for y in range(1, bound):   # limit + 1
			n = (4 * x * x) + (y * y)
			if (n <= limit and (n % 12 == 1 or n % 12 == 5)):
				primes.add(n)

			n = (3 * x * x) + (y * y)
			if n <= limit and n % 12 == 7:
				primes.add(n)

			n = (3 * x * x) - (y * y)
			if (x > y and n <= limit and n % 12 == 11):
				primes.add(n)

	primes = list(primes)
	sieved = primes

	print(primes)

	'''
	filtering needs more speed optimization
	maybe use toggling
	'''

	for i in primes:
		for n in range(len(primes)):
			if(primes[n] % i == 0 and primes[n] != i):
				print(f'{primes[n]} is not a prime because {primes[n]} is not {i} and {primes[n]} mod {i} is 0') # can comment this out
				sieved[n] = math.inf

	final = list(filter(lambda x: x != math.inf, sieved))
	return final


limit = 100
Primes = SieveOfAtkin(limit=limit) 
print(Primes)
