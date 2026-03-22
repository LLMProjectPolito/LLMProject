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

    def test_positive_and_negative_numbers(self):
        assert specialFilter([15, -73, 14, -15, 35, -91]) == 3

    def test_numbers_with_leading_zeros(self):
        assert specialFilter([15, -73, 14, -15, 35, -91, 101]) == 3

    def test_large_numbers(self):
        assert specialFilter([15, -73, 14, -15, 35, -91, 101, 13579]) == 4

    def test_mixed_numbers(self):
        assert specialFilter([11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 59, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 78, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99]) == 0

    def test_numbers_greater_than_10(self):
        assert specialFilter([11, 12, 13, 14, 15]) == 1

    def test_negative_numbers_greater_than_10(self):
        assert specialFilter([-11, -12, -13, -14, -15]) == 0