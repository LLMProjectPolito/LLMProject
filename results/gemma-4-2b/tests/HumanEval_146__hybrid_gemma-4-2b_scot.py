
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
        num_str = str(abs(num))
        if num > 10:
            if int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0:
                count += 1
    return count


class TestSpecialFilterSuite:
    def test_empty_array(self):
        assert specialFilter([]) == 0

    def test_no_valid_numbers(self):
        assert specialFilter([-12, -14, -16]) == 0

    def test_single_valid_number(self):
        assert specialFilter([11]) == 1

    def test_multiple_valid_numbers(self):
        assert specialFilter([15, 33, 55, 77, 99]) == 5

    def test_positive_numbers(self):
        assert specialFilter([15, 33, 55, 77, 99]) == 5
        assert specialFilter([11, 22, 33, 44, 55]) == 2

    def test_negative_numbers(self):
        assert specialFilter([-15, -33, -55, -77, -99]) == 5
        assert specialFilter([-11, -22, -33, -44, -55]) == 2

    def test_mixed_numbers(self):
        assert specialFilter([15, -33, 55, -77, 99, 22, -11]) == 4
        assert specialFilter([11, 22, -33, 44, -55]) == 2

    def test_zero(self):
        assert specialFilter([0, 10, 20]) == 0

    def test_large_numbers(self):
        assert specialFilter([1234567890, 1111111111]) == 1
        assert specialFilter([1111111111, 2222222222]) == 1
        assert specialFilter([1234567890, 9999999999]) == 1

    def test_edge_cases(self):
        assert specialFilter([10, 11, 12]) == 1
        assert specialFilter([11, 12, 13]) == 1

    def test_all_odd_numbers(self):
        assert specialFilter([11, 33, 55, 77, 99, 101]) == 6
        assert specialFilter([11, 33, 55, 77, 99]) == 5

    def test_all_even_numbers(self):
        assert specialFilter([22, 44, 66, 88, 100]) == 0
        assert specialFilter([22, 44, 66, 88, 100, 102]) == 0

    def test_positive_odd_first_last_greater_than_10(self):
        assert specialFilter([15, 33, 55, 77, 99]) == 5

    def test_positive_odd_first_last_greater_than_10_negative(self):
        assert specialFilter([-15, 33, -55, 77, -99]) == 5

    def test_negative_odd_first_last_greater_than_10(self):
        assert specialFilter([-15, -33, -55, -77, -99]) == 5

    def test_less_than_or_equal_to_10(self):
        assert specialFilter([5, 10, 15, 20]) == 0

    def test_even_first_or_last(self):
        assert specialFilter([22, 44, 66, 88]) == 0

    def test_empty_list(self):
        assert specialFilter([]) == 0

    def test_no_numbers_greater_than_10(self):
        assert specialFilter([1, 2, 3, 4, 5]) == 0

    def test_all_less_than_or_equal_to_10(self):
        assert specialFilter([1, 2, 3, 4, 5]) == 0

    def test_greater_than_or_equal_to_10_odd_digits_not_present(self):
        assert specialFilter([12, 34, 56, 78, 90]) == 0
        
    def test_mixed_list_edge_cases(self):
        assert specialFilter([15, 22, 33, -15, -22, 44, 55, -1, 11, 13]) == 3
    
    def test_large_numbers_edge_cases(self):
        assert specialFilter([1000, 2000, 3000, 1001, 1003, 1005, 1007, 1009]) == 8
    
    def test_zero_in_list(self):
        assert specialFilter([0, 15, -15, 33, -33]) == 2