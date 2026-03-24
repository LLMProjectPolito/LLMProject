
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

def test_single_special_number():
    assert specialFilter([15]) == 1

def test_multiple_special_numbers():
    assert specialFilter([15, 37, 59, 71, 93]) == 5

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_more_mixed_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_negative_numbers():
    assert specialFilter([-15, -37, -59, -71, -93]) == 5

def test_numbers_with_even_first_digit():
    assert specialFilter([25, 47, 69, 81]) == 0

def test_numbers_with_even_last_digit():
    assert specialFilter([12, 34, 56, 78, 90]) == 0

def test_numbers_with_both_even_digits():
    assert specialFilter([24, 46, 68, 80]) == 0

def test_numbers_close_to_10():
    assert specialFilter([9, 11, 10, 101]) == 1

def test_large_numbers():
    assert specialFilter([111, 333, 555, 777, 999]) == 5

def test_large_numbers_mixed():
    assert specialFilter([111, 222, 333, 444, 555]) == 3

def test_zero():
    assert specialFilter([0]) == 0

def test_one():
    assert specialFilter([1]) == 0

def test_ten():
    assert specialFilter([10]) == 0

def test_hundred():
    assert specialFilter([100]) == 0

def test_edge_case_1():
    assert specialFilter([11]) == 0

def test_edge_case_2():
    assert specialFilter([99]) == 0