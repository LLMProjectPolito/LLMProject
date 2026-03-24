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

def test_specialFilter_no_matching_elements():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_single_matching_element():
    assert specialFilter([15]) == 1

def test_specialFilter_multiple_matching_elements():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_mixed_elements():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_negative_numbers():
    assert specialFilter([-15, -33, -45]) == 0

def test_specialFilter_large_numbers():
    assert specialFilter([123, 456, 789]) == 0

def test_specialFilter_numbers_with_zero():
    assert specialFilter([101, 202, 303]) == 0

def test_specialFilter_all_odd_first_last():
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_specialFilter_some_odd_some_even():
    assert specialFilter([11, 22, 33, 44, 55]) == 2

def test_specialFilter_with_zero_and_positive():
    assert specialFilter([0, 11, 22, 33, 44, 55]) == 2

def test_specialFilter_with_negative_and_positive():
    assert specialFilter([-11, 11, -22, 22, -33, 33]) == 2