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
            num_str = str(abs(num))
            if num_str[0] in '13579' and num_str[-1] in '13579':
                count += 1
    return count

class TestSpecialFilter:
    def test_empty_list(self):
        assert specialFilter([]) == 0

    def test_no_matching_numbers(self):
        assert specialFilter([1, 2, 3, 4, 5]) == 0

    def test_example_1(self):
        assert specialFilter([15, -73, 14, -15]) == 1

    def test_example_2(self):
        assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

    def test_positive_numbers(self):
        assert specialFilter([11, 33, 55, 77, 99, 111, 333, 555, 777, 999]) == 10

    def test_negative_numbers(self):
        assert specialFilter([-11, -33, -55, -77, -99, -111, -333, -555, -777, -999]) == 0

    def test_mixed_positive_and_negative(self):
        assert specialFilter([11, -33, 55, -77, 99, -111, 333, -555, 777, -999]) == 1

    def test_numbers_greater_than_10(self):
        assert specialFilter([11, 12, 13, 14, 15]) == 1

    def test_numbers_less_than_10(self):
        assert specialFilter([1, 3, 5, 7, 9]) == 0

    def test_zero_and_negative_numbers(self):
        assert specialFilter([0, -1, -3, -5, -7, -9]) == 0

    def test_large_numbers(self):
        assert specialFilter([13579, 98765, 12345, 54321]) == 1

    def test_numbers_with_leading_zeros(self):
        assert specialFilter([101, 303, 505, 707, 909]) == 0

    def test_duplicate_numbers(self):
        assert specialFilter([15, 15, 15, 15]) == 4

    def test_numbers_with_different_signs(self):
        assert specialFilter([15, -15, 15, -15]) == 2

    def test_edge_case_1(self):
        assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 0

    def test_edge_case_2(self):
        assert specialFilter([31, 33, 35, 37, 39]) == 0