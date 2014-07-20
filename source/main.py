# -*- coding: utf-8 -*-
"""
Python code for generating an Ulam Spiral. Uses generic input to determine
primality of a given number.

Will add:
	other spirals
"""

import ulam
import generate_integers
import argparse

def DemoNormalPrimes(length, output_file):
	# Demo of the Generator on the normal primes
	sp = ulam.SpiralGenerator(int(length), output_file,
							  ulam.InitPrimes(int(length)))
	sp.ColorImage()


def DemoSievedPrimes(length, output_file):
	# Demo of the generator on Beurling systems which have the normal primes
	# with some removed. Runs reasonably fast. Spirals could be generated
	# in a similar fashion with any valid generalized "multiply(x,y)" function.
	# (See InitPrimesSieved())
	sp = ulam.SpiralGenerator(int(length), output_file,
							  ulam.InitPrimesSieved(int(length), [2]))
	sp.ColorImage()


# Demo of the generator on any Beurling generalized integers
def DemoCustom1(output_file):
	ig = generate_integers.IntegersGenerator([2,3,5,7,11,13,17,19,23,29,31])
	length = ulam.LargestLength(len(ig.isprime))
	print("Length is: {}".format(length))
	sp = ulam.SpiralGenerator(length, output_file, ig.isprime)
	sp.ColorImage()


# Demo of the generator on any Beurling generalized integers
# This is VERY slow for large n
def DemoCustom2(output_file):
	primes = ulam.PrimesBelowNSquared(80)
	primes.remove(2)
	generate_integers.AddToSortedList(1.5, primes)
	ig = generate_integers.IntegersGenerator(primes)
	length = ulam.LargestLength(len(ig.isprime))
	print("Length is: {}".format(length))
	sp = ulam.SpiralGenerator(length, output_file, ig.isprime)
	sp.ColorImage()


def main():
	# Get command line arguments
	parser = argparse.ArgumentParser(description='Create an Ulam spiral.')
	parser.add_argument('--length',
						default=200,
						help='the length of a side of the image in pixels')
	parser.add_argument('--output_file',
						default="ulam.bmp",
						help='the name of the image output')
	parser.add_argument('--odds', dest='odds', action='store_true',
						help='If True, prints a spiral for the odd numbers')
	parser.set_defaults(odds=False)
	parser.add_argument('--custom1', dest='custom1', action='store_true',
						help='If True, prints a spiral for ...')
	parser.set_defaults(custom1=False)
	parser.add_argument('--custom2', dest='custom2', action='store_true',
						help='If True, prints a spiral for the set of primes'
							 'with 2 removed and 1.5 added')
	parser.set_defaults(custom2=False)
	args = parser.parse_args()
	
	print("Starting...")
	
	if args.odds:
		DemoSievedPrimes(args.length, args.output_file)
	elif args.custom1:
		DemoCustom1(args.output_file)
	elif args.custom2:
		DemoCustom2(args.output_file)
	else:
		DemoNormalPrimes(args.length, args.output_file)
	
	print("Done!")
	

if __name__ == "__main__":
    main()