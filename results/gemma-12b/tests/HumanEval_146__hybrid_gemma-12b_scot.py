
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
            first_digit = int(num_str[0])
            last_digit = int(num_str[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_numbers_greater_than_10():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_all_numbers_greater_than_10_invalid_digits():
    assert specialFilter([21, 43, 65, 87, 10]) == 0

def test_single_valid_number():
    assert specialFilter([15]) == 1

def test_multiple_valid_numbers():
    assert specialFilter([15, 22, 37, 44, 59]) == 2

def test_negative_numbers():
    assert specialFilter([-15, -37, -59]) == 3

def test_mixed_positive_and_negative():
    assert specialFilter([15, -22, 37, -44, 59, -71]) == 3

def test_numbers_with_leading_zeros():
    assert specialFilter([15, 037, 059]) == 2

def test_edge_case_11():
    assert specialFilter([11]) == 0

def test_edge_case_19():
    assert specialFilter([19]) == 1

def test_no_valid_numbers():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

def test_even_first_digit():
    assert specialFilter([25, 47, 61, 83]) == 0

def test_even_last_digit():
    assert specialFilter([12, 34, 56, 78, 90]) == 0

def test_valid_numbers():
    assert specialFilter([15, 37, 59, 71, 93]) == 5

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15, 21, 33, 45, 21, 109, 11]) == 4

def test_negative_valid_numbers():
    assert specialFilter([-15, -37, -59, -71, -93]) == 5

def test_single_digit_numbers():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_large_numbers():
    assert specialFilter([151, 373, 595, 717, 939]) == 5

def test_zero_as_first_digit():
    assert specialFilter([015, 037]) == 0

def test_numbers_not_greater_than_10():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_numbers_with_multiple_digits_invalid():
    assert specialFilter([123, 345, 567, 789]) == 0

def test_numbers_with_multiple_digits_valid():
    assert specialFilter([111, 333, 555, 777, 999]) == 5