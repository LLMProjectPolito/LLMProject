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
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_mixed_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_negative_numbers():
    assert specialFilter([-15, -33, -45]) == 0

def test_specialFilter_large_numbers():
    assert specialFilter([1111111111, 1333333333]) == 2

def test_specialFilter_zero_and_negative():
    assert specialFilter([-10, -11, -12, -13]) == 0

def test_specialFilter_with_zero_in_string():
    assert specialFilter([101]) == 0

def test_specialFilter_with_single_digit():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_specialFilter_with_decimal():
    assert specialFilter([15.5, 20.1]) == 0

def test_specialFilter_with_negative_decimal():
    assert specialFilter([-15.5, -20.1]) == 0

def test_specialFilter_all_negative_greater_than_10():
    assert specialFilter([-11, -13, -15]) == 0

def test_specialFilter_complex_case():
    assert specialFilter([123, 135, 157, 179, 191, 213, 335, 557, 779, 991]) == 5