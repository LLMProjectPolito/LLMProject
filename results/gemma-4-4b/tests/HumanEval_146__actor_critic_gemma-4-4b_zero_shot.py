
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
            if num_str[0] in '13579' and num_str[-1] in '13579':
                count += 1
    return count

@pytest.suite()
class TestSpecialFilter:
    def test_empty_list(self):
        assert specialFilter([]) == 0

    def test_no_numbers_greater_than_10(self):
        assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

    def test_all_numbers_greater_than_10_but_not_matching_criteria(self):
        assert specialFilter([12, 14, 16, 18, 20]) == 0

    def test_some_numbers_greater_than_10_matching_criteria(self):
        assert specialFilter([15, -73, 14, -15]) == 1

    def test_multiple_numbers_greater_than_10_matching_criteria(self):
        assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

    def test_negative_numbers(self):
        assert specialFilter([-15, -73, -14, -15]) == 1

    def test_zero(self):
        assert specialFilter([0]) == 0

    def test_single_number_greater_than_10_matching_criteria(self):
        assert specialFilter([13]) == 1

    def test_single_number_greater_than_10_not_matching_criteria(self):
        assert specialFilter([12]) == 0

    def test_mixed_positive_and_negative_numbers(self):
        assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109, 11, 13, 15, 17]) == 5

    def test_large_numbers(self):
        assert specialFilter([13579, 1357, 135, 13, 1]) == 1

    def test_edge_case_10(self):
        assert specialFilter([10]) == 0

    def test_edge_case_11(self):
        assert specialFilter([11]) == 0
    
    def test_all_odd_first_and_last(self):
        assert specialFilter([11, 33, 55, 77, 99]) == 5
    
    def test_mixed_odd_and_even(self):
        assert specialFilter([11, 33, 55, 77, 99, 22, 44, 66, 88]) == 5