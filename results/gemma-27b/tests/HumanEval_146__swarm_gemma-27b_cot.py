
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_no_match():
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

def test_specialFilter_single_match():
    assert specialFilter([15]) == 1

def test_specialFilter_multiple_matches():
    assert specialFilter([15, 37, 59, 71, 93]) == 5

def test_specialFilter_mixed_matches():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_negative_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_large_numbers():
    assert specialFilter([111, 123, 135, 157, 179]) == 0

def test_specialFilter_edge_case_11():
    assert specialFilter([11]) == 0

def test_specialFilter_edge_case_13():
    assert specialFilter([13]) == 1

def test_specialFilter_edge_case_101():
    assert specialFilter([101]) == 0

def test_specialFilter_edge_case_1111():
    assert specialFilter([1111]) == 0

def test_specialFilter_edge_case_99():
    assert specialFilter([99]) == 1

def test_specialFilter_edge_case_1001():
    assert specialFilter([1001]) == 0

def test_specialFilter_edge_case_10001():
    assert specialFilter([10001]) == 0

def test_specialFilter_edge_case_100001():
    assert specialFilter([100001]) == 0

def test_specialFilter_edge_case_1000001():
    assert specialFilter([1000001]) == 0

def test_specialFilter_edge_case_10000001():
    assert specialFilter([10000001]) == 0

def test_specialFilter_edge_case_19():
    assert specialFilter([19]) == 1

def test_specialFilter_edge_case_91():
    assert specialFilter([91]) == 1