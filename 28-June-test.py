import unittest

from June28 import sum_two_smallest_numbers

class TestSumTwoSmallestNumbers(unittest.TestCase):
    def test_bla(self):
        self.assertEqual(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)

    def test_2(self):
        self.assertEqual(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
    
    def test_3(self):
        self.assertEqual(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)