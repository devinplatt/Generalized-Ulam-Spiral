# -*- coding: utf-8 -*-
"""
Some tests for the integer generating code.
"""

import unittest
import ulam
import generate_integers

class GenerateIntegersTestCase(unittest.TestCase):
	def setUp(self):
		self.prime_input = [2,3,5,7,11,13,17,19,23,29,31]
		self.ig = generate_integers.IntegersGenerator(self.prime_input)
		
	def test_generated_integers(self):
		for x,y in enumerate(self.ig.integers):
			self.assertEqual(x+1,y)

	def test_generated_primes(self):
		for index, value in enumerate(self.ig.isprime):
			self.assertEqual(value, index+1 in self.prime_input)		

class SieveMultiplyTestCase(unittest.TestCase):
	def setUp(self):
		self.sm = generate_integers.SieveMultiply([2,3])
		
	def test_sieve_multiply(self):
		self.assertEqual(self.sm.partitions[0], 4)
		self.assertEqual(self.sm.partitions[1], 2)
		self.assertEqual(self.sm.uTn(1), 1)
		self.assertEqual(self.sm.uTn(2), 5)
		self.assertEqual(self.sm.uTn(3), 7)
		self.assertEqual(self.sm.uTn(4), 11)
		self.assertEqual(self.sm.uTn(5), 13)
		self.assertEqual(self.sm.uTn(6), 17)
		self.assertEqual(self.sm.nTu(1), 1)
		self.assertEqual(self.sm.nTu(5), 2)
		self.assertEqual(self.sm.nTu(7), 3)
		self.assertEqual(self.sm.nTu(11), 4)
		self.assertEqual(self.sm.nTu(13), 5)
		self.assertEqual(self.sm.nTu(17), 6)
		self.assertEqual(self.sm.multiply(2,2), 9)
		self.assertEqual(self.sm.multiply(2,3), 12)		

if __name__ == '__main__':
	unittest.main()