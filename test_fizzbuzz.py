import unittest
from fizzbuzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
	def test_it_should_be_default_value(self):
		fizzbuzz = FizzBuzz(1)
		self.assertEqual("1",fizzbuzz.count())
		fizzbuzz = FizzBuzz(2)
		self.assertEqual("2",fizzbuzz.count())