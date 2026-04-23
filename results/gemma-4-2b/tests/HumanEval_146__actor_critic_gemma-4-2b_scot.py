
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
        if num > 10 and (num % 10 != 0) and (abs(num) % 10 != 0):
            count += 1
    return count

def test_positive_numbers_greater_than_10():
    assert specialFilter([15, 25, 35, 45, 55]) == 5

def test_negative_numbers_greater_than_10():
    assert specialFilter([-15, -25, -35, -45, -55]) == 5

def test_numbers_with_odd_first_and_last_digits():
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_numbers_with_even_first_or_last_digit():
    assert specialFilter([12, 34, 56, 78, 90]) == 0

def test_numbers_less_than_or_equal_to_10():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

def test_empty_array():
    assert specialFilter([]) == 0

def test_array_with_only_numbers_less_than_or_equal_to_10():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

def test_array_with_numbers_greater_than_10_but_not_satisfying_odd_digits():
    assert specialFilter([11, 12, 13, 14, 15]) == 1

def test_array_with_numbers_satisfying_both_conditions():
    assert specialFilter([15, 25, 35, 45, 55, 110, 135]) == 3

def test_single_digit_odd():
    assert specialFilter([1]) == 1

def test_single_digit_even():
    assert specialFilter([2]) == 0

def test_single_digit_odd_and_even():
    assert specialFilter([1, 2]) == 0

def test_leading_zeros():
    assert specialFilter([01, 03, 05, 07, 09]) == 5

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15, 110, -120, 135]) == 3

def test_large_array():
    assert specialFilter(list(range(11, 101))) == 10

def test_negative_number_with_multiple_digits():
    assert specialFilter([-12345]) == 0

def test_negative_number_with_multiple_digits_satisfying_condition():
    assert specialFilter([-12345]) == 0

def test_negative_number_with_multiple_digits_satisfying_condition2():
    assert specialFilter([-12345]) == 0