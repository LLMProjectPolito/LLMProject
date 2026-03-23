import pytest

def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(abs(num))  # Handle negative numbers
            if len(num_str) > 0:
                first_digit = int(num_str[0])
                last_digit = int(num_str[-1])
                if first_digit % 2 != 0 and last_digit % 2 != 0:
                    count += 1
    return count

class TestSpecialFilter:
    def test_empty_list(self):
        assert specialFilter([]) == 0

    def test_no_matching_numbers(self):
        assert specialFilter([2, 4, 6, 8, 10]) == 0

    def test_single_matching_number(self):
        assert specialFilter([15, 2, 4, 6, 8]) == 1

    def test_multiple_matching_numbers(self):
        assert specialFilter([15, 33, 57, 79, 2, 4, 6, 8]) == 4

    def test_negative_numbers(self):
        assert specialFilter([-15, -33, -57, -79, 2, 4, 6, 8]) == 4

    def test_mixed_positive_negative(self):
        assert specialFilter([15, -33, 57, -79, 2, 4, 6, 8]) == 4

    def test_numbers_less_than_10(self):
        assert specialFilter([1, 3, 5, 7, 9]) == 0

    def test_edge_case_11(self):
        assert specialFilter([11]) == 0

    def test_edge_case_13(self):
        assert specialFilter([13]) == 1

    def test_large_numbers(self):
        assert specialFilter([151, 333, 575, 797, 919]) == 5

    def test_zero_as_first_digit(self):
        assert specialFilter([015, 033]) == 0