import pytest

def test_specialFilter_empty_array():
    assert specialFilter([]) == 0

def test_specialFilter_no_match():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_single_match():
    assert specialFilter([15]) == 1

def test_specialFilter_multiple_match():
    assert specialFilter([15, 33, 109]) == 3

def test_specialFilter_negative_numbers():
    assert specialFilter([-15, -73, -14, -15]) == 0

def test_specialFilter_large_numbers():
    assert specialFilter([151, 331, 1091]) == 3

def test_specialFilter_numbers_with_even_last_digit():
    assert specialFilter([12, 34, 56]) == 0

def test_specialFilter_numbers_with_even_first_digit():
    assert specialFilter([20, 40, 60]) == 0

def test_specialFilter_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_mixed_numbers_with_multiple_match():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2