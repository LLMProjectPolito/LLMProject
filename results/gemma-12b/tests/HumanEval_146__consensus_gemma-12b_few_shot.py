
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest
from your_module import specialFilter  # Replace your_module

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_matching_numbers():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_single_matching_number():
    assert specialFilter([15]) == 1

def test_multiple_matching_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_numbers_greater_than_10():
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 10

def test_negative_numbers():
    assert specialFilter([-11, -13, -15, -17, -19]) == 0

def test_zero_and_positive_numbers():
    assert specialFilter([0, 11, 13, 15, 17, 19]) == 5

def test_large_numbers():
    assert specialFilter([111, 133, 155, 177, 199]) == 5

def test_numbers_with_leading_zeros():
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_numbers_with_same_digits():
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_numbers_with_different_digits():
    assert specialFilter([13, 15, 17, 19]) == 4

def test_numbers_with_mixed_digits():
    assert specialFilter([12, 14, 16, 18]) == 0

def test_edge_case_1():
    assert specialFilter([11, 12, 13, 14, 15]) == 2

def test_edge_case_2():
    assert specialFilter([99, 100, 101, 102, 103]) == 1

def test_large_list():
    nums = [i for i in range(1, 101)]
    assert specialFilter([x for x in nums if x > 10 and str(x)[0] in '13579' and str(x)[-1] in '13579']) == 10