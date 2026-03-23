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
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

def test_single_special_number():
    assert specialFilter([15]) == 1

def test_multiple_special_numbers():
    assert specialFilter([15, 33, 57, 79, 91]) == 5

def test_negative_special_number():
    assert specialFilter([-73]) == 1

def test_negative_non_special_number():
    assert specialFilter([-72]) == 0

def test_number_equal_to_ten():
    assert specialFilter([10]) == 0

def test_number_less_than_ten():
    assert specialFilter([5]) == 0

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15, 2, 33, -2, 45, 21, 109]) == 4

def test_large_numbers():
    assert specialFilter([12345, 13579, 97531, 11111]) == 3

def test_negative_large_number():
    assert specialFilter([-13579]) == 1