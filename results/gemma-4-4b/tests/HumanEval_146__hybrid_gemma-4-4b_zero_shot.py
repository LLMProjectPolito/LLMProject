
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
        assert specialFilter([-1, -2, -3]) == 0

    def test_no_numbers_with_odd_first_and_last_digits(self):
        assert specialFilter([21, 23, 25]) == 0

    def test_mixed_numbers(self):
        assert specialFilter([15, -73, 14, -15]) == 1

    def test_multiple_numbers(self):
        assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

    def test_all_numbers_satisfy_conditions(self):
        assert specialFilter([11, 13, 15, 31, 33, 35, 51, 53, 55, 71, 73, 75, 91, 93, 95]) == 15

    def test_negative_numbers(self):
        assert specialFilter([-15, -33, -11, -13]) == 2

    def test_zero(self):
        assert specialFilter([1, 3, 5, 7, 9, 0]) == 5

    def test_single_number_satisfies(self):
        assert specialFilter([15]) == 1
        
    def test_single_number_does_not_satisfy(self):
        assert specialFilter([14]) == 0
    
    def test_large_numbers(self):
        assert specialFilter([1357900, 13579, 12345]) == 1
    
    def test_duplicate_numbers(self):
        assert specialFilter([15, 15, 15]) == 3

    def test_all_negative_and_satisfying(self):
        assert specialFilter([-15, -33, -11, -13, -51, -53, -55, -71, -73, -75, -91, -93, -95]) == 12

    def test_mixed_positive_negative_and_zero(self):
      assert specialFilter([15, -33, 13, -57, 1, 35, -11]) == 4
    
    def test_numbers_with_leading_zeros(self):
      assert specialFilter([105, 301, 503]) == 3

Suite 2:
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

    def test_no_matching_numbers(self):
        assert specialFilter([2, 4, 6, 8]) == 0

    def test_single_matching_number(self):
        assert specialFilter([15]) == 1

    def test_multiple_matching_numbers(self):
        assert specialFilter([33, 45, 21]) == 3

    def test_negative_numbers(self):
        assert specialFilter([-73, -15, -33]) == 3

    def test_mixed_positive_and_negative(self):
        assert specialFilter([15, -73, 14, -15]) == 1

    def test_large_numbers(self):
        assert specialFilter([115, 333, 555, 777, 999]) == 5

    def test_mixed_large_and_small(self):
        assert specialFilter([15, 21, 33, 45, 109, 12, 10]) == 4
    
    def test_zero(self):
        assert specialFilter([1, 3, 5, 7, 9, 0]) == 5

    def test_single_digit_numbers(self):
      assert specialFilter([1, 3, 5, 7, 9]) == 0
      assert specialFilter([2, 4, 6, 8]) == 0

    def test_special_characters_in_input(self):
        assert specialFilter([15, "abc", 15]) == 1 #Handles non-numeric inputs

    def test_edge_case_10(self):
        assert specialFilter([10]) == 0

    def test_edge_case_11(self):
        assert specialFilter([11]) == 0

    def test_edge_case_13(self):
        assert specialFilter([13]) == 1
    
    def test_mixed_odd_even_digits(self):
      assert specialFilter([12,34,56,78,90]) == 0

    def test_all_odd_first_last_digits(self):
        assert specialFilter([13, 35, 57, 79, 91]) == 5

    def test_all_even_first_last_digits(self):
        assert specialFilter([24, 46, 68, 80, 02]) == 0