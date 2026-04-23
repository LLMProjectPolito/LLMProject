
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
            if len(num_str) > 0:  # Handle potential empty string after abs()
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

def test_large_numbers():
    assert specialFilter([111, 333, 555, 777, 999]) == 5

def test_mixed_positive_negative():
    assert specialFilter([-11, -15, 11, 15, 22, 33, 121, -121]) == 2

def test_single_odd_number():
    assert specialFilter([11]) == 1

def test_single_even_number():
    assert specialFilter([22]) == 0

def test_numbers_greater_than_10_with_odd_digits():
    assert specialFilter([11, 13, 15, 17, 19, 31, 33, 35, 37, 39, 51, 53, 55, 57, 59, 71, 73, 75, 77, 79, 91, 93, 95, 97, 99]) == 25

def test_numbers_starting_with_zero():
    assert specialFilter([01, 03, 05, 07, 09]) == 0

def test_numbers_less_than_or_equal_to_10_with_odd_digits():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_mixed_numbers_with_and_without_odd_digits():
    assert specialFilter([11, 22, 33, 44, 55, 66, 77, 88, 99]) == 9