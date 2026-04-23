
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
            num_str = str(abs(num))  # Handle negative numbers
            if num_str[0] in '13579' and num_str[-1] in '13579':
                count += 1
    return count

@pytest.suite()
class TestSpecialFilter:

    def test_empty_list(self):
        assert specialFilter([]) == 0

    def test_no_numbers_greater_than_10(self):
        assert specialFilter([1, 2, 3, 4, 5]) == 0

    def test_basic_example_1(self):
        assert specialFilter([15, -73, 14, -15]) == 1

    def test_basic_example_2(self):
        assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

    def test_all_numbers_satisfy_condition(self):
        assert specialFilter([11, 13, 15, 31, 33, 35, 51, 53, 55, 71, 73, 75, 91, 93, 95]) == 15

    def test_negative_numbers(self):
        assert specialFilter([-15, -33, -45, -109]) == 0

    def test_mixed_positive_and_negative(self):
        assert specialFilter([15, -33, 45, -109, 11, -13]) == 2

    def test_zero(self):
        assert specialFilter([0, 1, 3, 5, 7, 9]) == 0

    def test_single_element_greater_than_10_satisfying_condition(self):
        assert specialFilter([15]) == 1

    def test_single_element_greater_than_10_not_satisfying_condition(self):
        assert specialFilter([14]) == 0

    def test_single_element_less_than_or_equal_to_10(self):
        assert specialFilter([10]) == 0

    def test_large_numbers(self):
        assert specialFilter([123456789, 987654321]) == 2

    def test_numbers_with_leading_zeros(self):
        assert specialFilter([105, 307, 519, 731, 953]) == 5

    def test_numbers_with_multiple_digits(self):
        assert specialFilter([115, 337, 559, 771, 993]) == 5

    def test_numbers_with_mixed_odd_and_even_digits(self):
        assert specialFilter([123, 456, 789, 101, 203]) == 2