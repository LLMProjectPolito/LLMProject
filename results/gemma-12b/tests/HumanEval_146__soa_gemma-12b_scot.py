
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
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

def test_single_matching_number():
    assert specialFilter([15]) == 1

def test_multiple_matching_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_numbers_greater_than_10():
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 10

def test_numbers_less_than_10():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_negative_numbers():
    assert specialFilter([-11, -13, -15, -17, -19]) == 0

def test_zero():
    assert specialFilter([0]) == 0

def test_large_numbers():
    assert specialFilter([151, 353, 575, 797, 919]) == 5

def test_numbers_with_leading_zeros():
    assert specialFilter([15, 33, 55, 77, 99]) == 5

def test_mixed_positive_and_negative():
    assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109, -11]) == 2

def test_edge_case_1():
    assert specialFilter([111, 333, 555, 777, 999]) == 5

def test_edge_case_2():
    assert specialFilter([101, 303, 505, 707, 909]) == 5

def test_edge_case_3():
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 15

def test_large_list():
    nums = list(range(1, 101))
    assert specialFilter(nums) == 10

def test_all_numbers_match():
    assert specialFilter([11, 13, 15, 17, 19, 31, 33, 35, 37, 39, 51, 53, 55, 57, 59, 71, 73, 75, 77, 79, 91, 93, 95, 97, 99]) == 25