"""
  Sample Tests
"""

from django.test import SimpleTestCase
from app import calc

class TestCalculation(SimpleTestCase):
    """ Test case """
    def test_add_number(self):
        res = calc.calculate(5 ,6)

        self.assertEqual(res , 11)

    def test_subtract_number(self):
        res = calc.subtract(5 ,10)

        self.assertEqual(res , 5)    