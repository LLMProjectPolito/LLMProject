
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
            if len(num_str) > 0:
                first_digit = int(num_str[0])
                last_digit = int(num_str[-1])
                if (first_digit % 2 != 0 and last_digit % 2 != 0):
                    count += 1
    return count

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_matching_elements():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_single_matching_element():
    assert specialFilter([15]) == 1

def test_multiple_matching_elements():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_mixed_elements():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_negative_numbers():
    assert specialFilter([-15, -33, -45]) == 0

def test_large_numbers():
    assert specialFilter([123, 456, 789]) == 0

def test_numbers_with_zero():
    assert specialFilter([101, 202, 303]) == 0

def test_all_odd_numbers():
    assert specialFilter([11, 13, 15, 17, 19]) == 0

def test_all_even_numbers_greater_than_10():
    assert specialFilter([12, 14, 16, 18, 20]) == 0

def test_complex_case():
    assert specialFilter([111, 131, 151, 171, 191, 212, 333, 353, 373, 393]) == 2

def test_duplicate_numbers():
    assert specialFilter([15, 15, 15]) == 1

def test_mixed_signs_and_values():
    assert specialFilter([-15, 15, -33, 33]) == 2