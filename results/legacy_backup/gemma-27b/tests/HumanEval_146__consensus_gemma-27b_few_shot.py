import pytest

def test_special_filter_empty():
    assert specialFilter([]) == 0

def test_special_filter_no_match():
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

def test_special_filter_single_match():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_special_filter_multiple_matches():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_special_filter_negative_numbers():
    assert specialFilter([-11, -13, -15, -17, -19]) == 5

def test_special_filter_mixed_numbers():
    assert specialFilter([11, 22, 33, 44, 55, 66, 77, 88, 99]) == 5

def test_special_filter_large_numbers():
    assert specialFilter([111, 123, 135, 147, 159]) == 5

def test_special_filter_numbers_close_to_10():
    assert specialFilter([9, 11, 10, 12]) == 1

def test_special_filter_all_numbers_greater_than_10():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_special_filter_with_zero():
    assert specialFilter([11, 13, 0, 15, 17, 19]) == 4

def test_special_filter_edge_cases():
    assert specialFilter([111, 333, 555, 777, 999]) == 5
    assert specialFilter([10, 12, 14, 16, 18]) == 0
    assert specialFilter([1, 3, 5, 7, 9]) == 0
    assert specialFilter([101, 103, 105, 107, 109]) == 0