import math
import unittest

def truncate_number(number: float) -> float:
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a floating-point number.")
    if number <= 0:
        raise ValueError("Input must be a positive floating-point number.")
    
    # Get the integer part using math.floor()
    integer_part = math.floor(number)
    
    # Calculate the decimal part
    decimal_part = number - integer_part
    
    # Check if the decimal part is greater than or equal to 1
    if decimal_part >= 1:
        raise ValueError("Decimal part cannot be greater than or equal to 1.")
    
    return decimal_part

class TestTruncateNumber(unittest.TestCase):

    def test_positive_number(self):
        # Test with a positive number
        self.assertEqual(truncate_number(3.5), 0.5)

    def test_zero(self):
        # Test with zero
        self.assertEqual(truncate_number(0), 0)

    def test_negative_number(self):
        # Test with a negative number
        with self.assertRaises(ValueError):
            truncate_number(-3.5)

    def test_large_number(self):
        # Test with a large number
        self.assertEqual(truncate_number(1234567.89), 0.89)

    def test_decimal_part_only(self):
        # Test with a decimal number only
        self.assertEqual(truncate_number(0.5), 0.5)

    def test_decimal_part_zero(self):
        # Test with a number that is exactly an integer
        self.assertEqual(truncate_number(1.0), 0.0)

    def test_edge_case_decimal_part_greater_than_or_equal_to_one(self):
        # Test the edge case where the decimal part is greater than or equal to 1
        with self.assertRaises(ValueError):
            truncate_number(2.1)

    def test_edge_case_invalid_input(self):
        # Test the edge case where the input is not a floating-point number
        with self.assertRaises(TypeError):
            truncate_number('3.5')

if __name__ == '__main__':
    unittest.main()