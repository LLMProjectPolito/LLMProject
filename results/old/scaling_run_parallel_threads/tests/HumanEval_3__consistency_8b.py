import unittest
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

class TestBelowZeroFunction(unittest.TestCase):
    def test_no_below_zero(self):
        self.assertFalse(below_zero([1, 2, 3]))

    def test_below_zero(self):
        self.assertTrue(below_zero([1, 2, -4, 5]))

    def test_zero(self):
        self.assertFalse(below_zero([0]))

    def test_series_of_zeros(self):
        self.assertFalse(below_zero([0, 0, 0]))

    def test_all_positives(self):
        self.assertFalse(below_zero([1, 2, 3, 4]))

    def test_all_negatives(self):
        self.assertFalse(below_zero([-1, -2, -3, -4]))

    def test_mixed_positives_and_negatives(self):
        self.assertTrue(below_zero([-1, 2, -3, 4]))
        self.assertTrue(below_zero([1, -2, 3, -4]))

    def test_large_numbers(self):
        self.assertTrue(below_zero([-1000000, 2000000, -3000000, 4000000]))

    def test_empty_list(self):
        self.assertFalse(below_zero([]))

    def test_single_positive(self):
        self.assertFalse(below_zero([10]))

    def test_single_negative(self):
        self.assertTrue(below_zero([-10]))

if __name__ == '__main__':
    unittest.main()