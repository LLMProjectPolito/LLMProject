
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

def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_no_matching_numbers():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_single_matching_number():
    assert specialFilter([15]) == 1

def test_specialFilter_multiple_matching_numbers():
    assert specialFilter([15, 33, 45, 109]) == 3

def test_specialFilter_negative_numbers():
    assert specialFilter([-15, -33, -45]) == 0

def test_specialFilter_mixed_positive_negative():
    assert specialFilter([15, -33, 45, -109]) == 2

def test_specialFilter_with_zero():
    assert specialFilter([11, 12, 13, 14, 15]) == 1

def test_specialFilter_large_numbers():
    assert specialFilter([111, 133, 155, 177, 199]) == 5

def test_specialFilter_duplicate_numbers():
    assert specialFilter([15, 15, 15]) == 3

def test_specialFilter_numbers_around_threshold():
    assert specialFilter([11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1

def test_specialFilter_complex_example():
    assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_all_negative_greater_than_10():
    assert specialFilter([-11, -13, -15, -17, -19]) == 0

def test_specialFilter_single_digit_greater_than_10():
    assert specialFilter([11, 13, 15, 17, 19]) == 0

def test_specialFilter_mixed_single_and_multi_digit():
    assert specialFilter([11, 15, 13, 17, 19]) == 3