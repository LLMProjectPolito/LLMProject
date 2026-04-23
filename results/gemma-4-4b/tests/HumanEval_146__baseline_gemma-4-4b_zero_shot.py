
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

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
            if int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0:
                count += 1
    return count

@pytest.suite()
class TestSpecialFilter:

    def test_empty_list(self):
        assert specialFilter([]) == 0

    def test_no_numbers_greater_than_10(self):
        assert specialFilter([-1, -2, -3]) == 0

    def test_example_1(self):
        assert specialFilter([15, -73, 14, -15]) == 1

    def test_example_2(self):
        assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

    def test_all_numbers_satisfy_condition(self):
        assert specialFilter([11, 13, 15, 31, 33, 35, 51, 53, 55, 71, 73, 75, 91, 93, 95]) == 15

    def test_mixed_numbers(self):
        assert specialFilter([1, 2, 3, 4, 5, 11, 13, 15, 21, 23, 25, 31, 33, 35, 41, 43, 45, 51, 53, 55, 61, 63, 65, 71, 73, 75, 81, 83, 85, 91, 93, 95, 10, 12, 14, 16, 18, 20]) == 6

    def test_negative_numbers(self):
        assert specialFilter([-15, -33, -45, -1, -3, -5]) == 0

    def test_zero(self):
        assert specialFilter([0, 1, 3, 5, 7, 9]) == 0

    def test_large_numbers(self):
        assert specialFilter([1111, 3333, 5555, 7777, 9999, 1001, 1003, 1005, 1007, 1009]) == 5

    def test_mixed_positive_negative_large(self):
        assert specialFilter([-111, 111, -333, 333, -555, 555, 1001, -1001]) == 4