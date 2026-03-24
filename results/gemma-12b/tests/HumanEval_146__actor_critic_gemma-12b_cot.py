
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
            first_digit = int(num_str[0])
            last_digit = int(num_str[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_numbers_greater_than_10():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_no_odd_first_and_last_digits():
    assert specialFilter([22, 44, 66, 88]) == 0

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_positive_and_negative_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_single_number_11():
    assert specialFilter([11]) == 0

def test_single_number_15():
    assert specialFilter([15]) == 1

def test_single_number_21():
    assert specialFilter([21]) == 0

def test_single_number_109():
    assert specialFilter([109]) == 1

def test_large_numbers():
    assert specialFilter([111, 333, 555, 777, 999]) == 5

def test_numbers_with_leading_zeros():
    assert specialFilter([101, 303, 505, 707, 909]) == 5

def test_number_equal_to_10():
    assert specialFilter([10]) == 0

def test_all_numbers_satisfying_condition():
    assert specialFilter([11, 13, 15, 17, 19, 31, 33, 35, 37, 39, 51, 53, 55, 57, 59, 71, 73, 75, 77, 79, 91, 93, 95, 97, 99]) == 25

def test_negative_numbers_with_odd_digits():
    assert specialFilter([-11, -13, -15, -17, -19]) == 0