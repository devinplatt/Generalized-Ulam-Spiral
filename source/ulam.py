# -*- coding: utf-8 -*-
"""
Python code for generating an Ulam Spiral. Uses generic input to determine
primality of a given number.

Will add:
	other spirals
"""

from PIL import Image
import math
import generate_integers

class SpiralGenerator:
	# We require that len(prime) >= length. (Put check in this function!)
	def __init__(self, length, outputFile, prime):
		# Length of a side of the square (the Ulam spiral, the bitmap)
		self.length = length
		# Used for keeping track current point during writing of spiral
		self.current_point = [0,0]
		# The current number, which is equal to the current index + 1
		self.c = 1
		# We declare an array of booleans giving which numbers are/aren't prime. It is
		# initialized to True to all values except prime[0] == False. Note that
		# prime[n] corresponds to the primality of number n+1.
		self.prime = prime
		# Create the new image
		# Note that PIL follows the notation (0,0) = upper left
		# see: 
		self.im = Image.new("1", (length, length), "white")
		# Data that we will "put" to the image
		# Initialized to white (1). Primes will be set to black (0).
		self.data = [1] * (length*length)
		self.outputFile = outputFile

	def CoordinateToDataNumber(self, x, y):
		return x+self.length*y
	
	# Increase the sequence one step.
	# Move current pixel left.
	# Color the current pixel.
	def left(self):
		self.c += 1
		self.current_point[0] -= 1
		if self.prime[self.c-1]:
			self.data[self.CoordinateToDataNumber(self.current_point[0], 
												  self.current_point[1])] = 0
			
	# Increase the sequence one step.
	# Move current pixel right.
	# Color the current pixel.
	def right(self):
		self.c += 1
		self.current_point[0] += 1
		if self.prime[self.c-1]:
			self.data[self.CoordinateToDataNumber(self.current_point[0],
												  self.current_point[1])] = 0
		
	# Increase the sequence one step.
	# Move current pixel up.
	# Color the current pixel.
	def up(self):
		self.c += 1
		self.current_point[1] -= 1
		if self.prime[self.c-1]:
			self.data[self.CoordinateToDataNumber(self.current_point[0],
												  self.current_point[1])] = 0

	# Increase the sequence one step.
	# Move current pixel down.
	# Color the current pixel.
	def down(self):
		self.c += 1
		self.current_point[1] += 1
		if self.prime[self.c-1]:
			self.data[self.CoordinateToDataNumber(self.current_point[0],
												  self.current_point[1])] = 0

	def even(self, k):
		self.left()
		for _ in range(1,k+1):
			self.down()
		for _ in range(1,k+1):
			self.right()
			
	def odd(self, k):
		self.right()
		for _ in range(1,k+1):
			self.up()
		for _ in range(1,k+1):
			self.left()	

	def ColorImage(self):		
		self.current_point[0] = int((self.length-1)/2)
		self.current_point[1] = int(self.length/2)
		
		# k increases as we spiral outwards. It counts how many pixels we must go
		# in any direction
		k = 1
		while (k < self.length):
			if (self.c % 2 == 0):
				self.even(k)
			else:
				self.odd(k)
			k += 1
		
		self.im.putdata(self.data)
		self.im.show()
		try:
			self.im.save(self.outputFile)
		except IOError:
			print("IOError\n")

# Initializes the prime array using the sieve method
def InitPrimes(length):
	prime = [True] * (length*length)
	prime[0] = False
	for i in range(2,length*length+1):
		# If we find a new prime, we remove all of its multiples
		if (prime[i-1]):
			multiple = 2*i
			# Sieve: disregard multiples of i as primes
			while (multiple <= length*length):
				prime[multiple-1] = False
				multiple += i
	return prime
	
# Initialize the prime bools for Beurling systems of the construction:
# natural number primes minus some. Eg. [2] gives the odd primes
def InitPrimesSieved(length, primes_to_remove):
	sm = generate_integers.SieveMultiply(primes_to_remove)
	prime = [True] * (length*length)
	prime[0] = False
	for i in range(2,length*length+1):
		# If we find a new prime, we remove all of its multiples
		if (prime[i-1]):
			j = 2
			multiple = sm.multiply(i,j)
			# Sieve: disregard multiples of i as primes
			while (multiple <= length*length):
				prime[multiple-1] = False
				j += 1
				multiple = sm.multiply(i,j)
	return prime
	
# Returns a list of the primes below N^2
def PrimesBelowNSquared(length):
	IsPrime = InitPrimes(length)
	primes = []
	for i, isprime in enumerate(IsPrime):
		if isprime:
			primes.append(i+1)
	return primes

# returns the floor of the square root of a number, the largest
# length of a square that we can use
def LargestLength(N):
	return int(math.sqrt(N))