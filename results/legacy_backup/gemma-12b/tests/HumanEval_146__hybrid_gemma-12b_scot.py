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
            num_str = str(abs(num))  # Handle negative numbers
            first_digit = int(num_str[0])
            last_digit = int(num_str[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count

def test_empty_array():
    assert specialFilter([]) == 0

def test_no_numbers_greater_than_10():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_no_odd_first_and_last_digits():
    assert specialFilter([22, 44, 66, 88]) == 0

def test_mixed_numbers_no_match():
    assert specialFilter([22, 44, 66, 88, 1, 2, 3]) == 0

def test_single_match():
    assert specialFilter([15, 22, 33]) == 1

def test_multiple_matches():
    assert specialFilter([15, 35, 51, 79, 22]) == 3

def test_negative_numbers():
    assert specialFilter([-15, -35, -51, -79, 22]) == 3

def test_zero_as_last_digit():
    assert specialFilter([10, 30, 50, 70]) == 0

def test_large_numbers():
    assert specialFilter([151, 353, 575, 797, 1000]) == 4

def test_all_numbers_match():
    assert specialFilter([11, 13, 15, 17, 19]) == 0 #None are > 10
    assert specialFilter([111, 131, 151, 171, 191]) == 5

def test_single_matching_number():
    assert specialFilter([15]) == 0

def test_no_matching_numbers():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_mixed_numbers():
    assert specialFilter([15, 22, 33, 44, 55, 66, 77, 88, 99]) == 0

def test_negative_numbers_mixed():
    assert specialFilter([-15, 33, -55, 77, -99]) == 1

def test_zero_as_first_digit():
    assert specialFilter([101, 202, 303, 404, 505]) == 0

def test_numbers_close_to_10():
    assert specialFilter([11, 12, 99, 10, 100]) == 0
    assert specialFilter([11, 12, 99, 10, 100, 111]) == 0