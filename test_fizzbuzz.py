import unittest
from fizzbuzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
	def setUp(self):
		self.fizzbuzz = FizzBuzz()

	def test_it_should_be_default_value(self):
		self.assertEqual("1",self.fizzbuzz.count(1))
		self.assertEqual("2",self.fizzbuzz.count(2))
		self.assertEqual("4",self.fizzbuzz.count(4))
		self.assertEqual("7",self.fizzbuzz.count(7))
		self.assertEqual("8",self.fizzbuzz.count(8))

	def test_it_should_be_fizz(self):
		self.assertEqual("fizz",self.fizzbuzz.count(3))
		self.assertEqual("fizz",self.fizzbuzz.count(6))
		self.assertEqual("fizz",self.fizzbuzz.count(9))

	def test_it_should_be_buzz(self):
		self.assertEqual("buzz",self.fizzbuzz.count(5))
		self.assertEqual("buzz",self.fizzbuzz.count(10))

	def test_it_should_be_fizzbuzz(self):
		self.assertEqual("fizzbuzz",self.fizzbuzz.count(15))