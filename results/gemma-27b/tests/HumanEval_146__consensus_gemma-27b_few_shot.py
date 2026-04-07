
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
            if num_str[0] in '13579' and num_str[-1] in '13579':
                count += 1
    return count

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_single_special_number():
    assert specialFilter([15]) == 1

def test_multiple_special_numbers():
    assert specialFilter([15, 33, 55, 77, 99]) == 5

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_negative_numbers():
    assert specialFilter([-11, -13, -15, -17, -19]) == 5

def test_large_numbers():
    assert specialFilter([1001, 12345, 98765, 11111]) == 2

def test_numbers_with_even_digits():
    assert specialFilter([12, 34, 56, 78, 90]) == 0

def test_numbers_close_to_10():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_example_1():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_example_2():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_all_negative():
    assert specialFilter([-11, -13, -15, -22, -34]) == 3

def test_zero():
    assert specialFilter([0]) == 0

def test_one_digit_odd():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_two_digit_odd():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_mixed_positive_negative():
    assert specialFilter([15, -33, 14, -55, 21, -79]) == 3