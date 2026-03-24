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
        assert specialFilter([151, -737, 14, -15, 35, -91, 101, 13579]) == 4

    def test_mixed_numbers(self):
        assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 0

    def test_numbers_greater_than_10(self):
        assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 100]) == 0

    def test_all_numbers_match(self):
        assert specialFilter([111, 333, 555, 777, 999]) == 0