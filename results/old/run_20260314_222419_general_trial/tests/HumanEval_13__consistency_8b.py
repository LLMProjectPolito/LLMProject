import unittest
from math import gcd

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Check for invalid inputs
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")
    
    # Handle zero and very large inputs
    if a == 0 and b == 0:
        raise ValueError("GCD is undefined for both inputs being zero.")
    elif a == 0:
        return abs(b)
    elif b == 0:
        return abs(a)
    
    # Apply the Euclidean algorithm to find GCD
    while b != 0:
        a, b = b, a % b
    
    return abs(a)

class TestGreatestCommonDivisorFunction(unittest.TestCase):

    def test_gcd_zero_inputs(self):
        self.assertEqual(greatest_common_divisor(0, 10), 10)
        self.assertEqual(greatest_common_divisor(5, 0), 5)
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_positive_integers(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)
        self.assertEqual(greatest_common_divisor(12, 12), 12)
        self.assertEqual(greatest_common_divisor(48, 18), 6)

    def test_zero(self):
        self.assertEqual(greatest_common_divisor(0, 5), 5)
        self.assertEqual(greatest_common_divisor(5, 0), 5)
        self.assertEqual(greatest_common_divisor(0, 0), 0)
        self.assertEqual(greatest_common_divisor(0, 1), 1)
        self.assertEqual(greatest_common_divisor(1, 0), 1)

    def test_negative_integers(self):
        self.assertEqual(greatest_common_divisor(-3, 5), 1)
        self.assertEqual(greatest_common_divisor(-25, 15), 5)
        self.assertEqual(greatest_common_divisor(-12, -12), 12)
        self.assertEqual(greatest_common_divisor(-48, 18), 6)

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            greatest_common_divisor(3.5, 5)
        with self.assertRaises(TypeError):
            greatest_common_divisor(3, 5.5)

    def test_large_numbers(self):
        self.assertEqual(greatest_common_divisor(123456789, 987654321), 3)
        self.assertEqual(greatest_common_divisor(1000000000, 123456789), 1)

    def test_duplicate_inputs(self):
        self.assertEqual(greatest_common_divisor(12, 12), 12)
        self.assertEqual(greatest_common_divisor(48, 48), 48)

if __name__ == '__main__':
    unittest.main()