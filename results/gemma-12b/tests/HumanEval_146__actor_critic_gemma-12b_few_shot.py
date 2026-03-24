
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

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
        if not isinstance(num, (int, float)):
            continue  # Skip non-numeric inputs

        num_str = str(num)
        if len(num_str) == 0:
            continue # Skip empty strings

        try:
            first_digit = int(num_str[0])
            last_digit = int(num_str[-1])
        except (IndexError, ValueError):
            continue # Skip single-digit numbers and invalid strings

        if num > 10:
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count


import pytest

def test_special_filter_basic():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_special_filter_example2():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_special_filter_empty_list():
    assert specialFilter([]) == 0

def test_special_filter_no_matches():
    assert specialFilter([22, 44, 66, 88]) == 0

def test_special_filter_single_digit():
    assert specialFilter([5]) == 0

def test_special_filter_negative_leading_zero():
    assert specialFilter([-015]) == 0

def test_special_filter_number_starting_with_zero():
    assert specialFilter([09]) == 0

def test_special_filter_mixed_positive_negative():
    assert specialFilter([11, -35, 22, -79, 101]) == 2

def test_special_filter_with_floats():
    assert specialFilter([15.0, -73.5, 14.2, -15.1]) == 1

def test_special_filter_invalid_input():
    assert specialFilter([15, "abc", -73, 14, -15]) == 1

def test_special_filter_all_odd_digits_greater_than_10():
    assert specialFilter([11, 33, 55, 77, 99]) == 5