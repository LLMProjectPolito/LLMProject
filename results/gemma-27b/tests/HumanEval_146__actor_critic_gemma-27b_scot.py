
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
    first and last digits of the absolute value of a number are odd (1, 3, 5, 7, 9).
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

def test_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10, 12, 14]) == 0

def test_positive_and_negative_numbers():
    assert specialFilter([15, 33, 14, 57, 21]) == 3
    assert specialFilter([-15, -33, -14, -57, -21]) == 3
    assert specialFilter([11, 13, 15, 17, 19]) == 5
    assert specialFilter([-11, -13, -15, -17, -19]) == 5
    assert specialFilter([22, 24, 26, 28, 30]) == 0
    assert specialFilter([-22, -24, -26, -28, -30]) == 0

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([-11, 22, 33, -44, 55]) == 2

def test_numbers_too_small():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

def test_single_digit_odd_numbers():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_large_number():
    assert specialFilter([1234567891]) == 1

def test_large_numbers():
    assert specialFilter([12345, 54321, 98765, 11111]) == 2
    assert specialFilter([100001, 100002, 100003]) == 1

def test_zero():
    assert specialFilter([0]) == 0

def test_non_integer_input():
    with pytest.raises(TypeError):
        specialFilter([15, "abc", 33])
    with pytest.raises(TypeError):
        specialFilter([15, 33.5, 33])