
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest
import math

def specialFilter(numbers):
    count = 0
    for number in numbers:
        number_str = str(abs(number))
        if len(number_str) >= 2:
            first_digit = int(number_str[0])
            last_digit = int(number_str[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count

class TestSpecialFilter:
    def test_specialFilter_empty_list(self):
        """Test with an empty list."""
        assert specialFilter([]) == 0

    def test_specialFilter_no_matching_numbers(self):
        """Test with a list containing numbers greater than 10, but not meeting the digit criteria."""
        assert specialFilter([11, 12, 13, 14, 15]) == 0

    def test_specialFilter_negative_numbers(self):
        """Test with negative numbers that meet the criteria."""
        assert specialFilter([-15, -33, -55]) == 0

    def test_specialFilter_zero(self):
        """Test with zero."""
        assert specialFilter([0]) == 0

    def test_specialFilter_single_matching_number(self):
        """Test with a single number that meets the criteria."""
        assert specialFilter([35]) == 1

    def test_specialFilter_multiple_matching_numbers(self):
        """Test with multiple numbers, some matching, some not."""
        assert specialFilter([15, 22, 35, 44, 57, 66, 78, 91]) == 4

    def test_specialFilter_large_numbers(self):
        """Test with large numbers to ensure digit extraction works correctly."""
        assert specialFilter([13579, 97531, 12345]) == 2

    def test_specialFilter_edge_case_11(self):
        """Test with a number where both digits are the same and odd."""
        assert specialFilter([11]) == 0

    def test_specialFilter_edge_case_101(self):
        """Test with a number where the first and last digits are odd, but the middle digit is even."""
        assert specialFilter([101]) == 0

    def test_specialFilter_edge_case_10001(self):
        """Test with a number where the first and last digits are odd, but the middle digits are even."""
        assert specialFilter([10001]) == 0