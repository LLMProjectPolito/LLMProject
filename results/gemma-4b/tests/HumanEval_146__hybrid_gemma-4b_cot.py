
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
                if first_digit % 2 != 0 and last_digit % 2 != 0:
                    count += 1
    return count

def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_no_matching_numbers():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_single_matching_number():
    assert specialFilter([15]) == 1

def test_specialFilter_multiple_matching_numbers():
    assert specialFilter([15, 22, 33, 44, 55]) == 2

def test_specialFilter_negative_numbers():
    assert specialFilter([-15, -22, -33, -44, -55]) == 0

def test_specialFilter_mixed_positive_negative():
    assert specialFilter([-15, 22, -33, 44, -55]) == 0

def test_specialFilter_with_zero():
    assert specialFilter([11, 22, 33, 44, 55]) == 0

def test_specialFilter_large_numbers():
    assert specialFilter([111, 222, 333, 444, 555]) == 0

def test_specialFilter_example_1():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_example_2():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_all_greater_than_10_and_odd_digits():
    assert specialFilter([111, 131, 151, 171, 191]) == 5

def test_specialFilter_all_less_than_10_and_odd_digits():
    assert specialFilter([11, 13, 15, 17, 19]) == 0

def test_specialFilter_mixed_odd_and_even_digits():
    assert specialFilter([12, 13, 14, 15, 16]) == 1

def test_specialFilter_with_zero_as_first_digit():
    assert specialFilter([015, 22, 33, 44, 55]) == 0

def test_specialFilter_with_zero_as_last_digit():
    assert specialFilter([15, 220, 33, 44, 55]) == 0

def test_specialFilter_with_negative_first_digit():
    assert specialFilter([-15, 22, 33, 44, 55]) == 0

def test_specialFilter_with_negative_last_digit():
    assert specialFilter([15, 22, -33, 44, 55]) == 0

def test_specialFilter_with_negative_and_odd_digits():
    assert specialFilter([-15, 22, -33, 45, 21, 109]) == 2