
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
        if abs(num) > 10:
            num_str = str(abs(num))
            if num_str[0] in '13579' and num_str[-1] in '13579':
                count += 1
    return count

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10, 12, 14]) == 0

def test_positive_special_numbers():
    assert specialFilter([15, 33, 57, 79, 91]) == 5

def test_negative_special_numbers():
    assert specialFilter([-15, -33, -57, -79, -91]) == 5

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15, 2, 33, -2, 45, 21, 109]) == 4

def test_single_digit_numbers():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_numbers_equal_to_ten():
    assert specialFilter([10, -10]) == 0

def test_large_numbers():
    assert specialFilter([12345679, -98765431]) == 2

def test_zero_in_number():
    assert specialFilter([101, 303, 505, 707, 909]) == 0
    assert specialFilter([111, 333, 555, 777, 999]) == 5