import pytest

def test_double_the_difference_basic():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_double_the_difference_negative():
    assert double_the_difference([-1, -2, 0]) == 0

def test_double_the_difference_mixed():
    assert double_the_difference([9, -2]) == 81

def test_double_the_difference_zero():
    assert double_the_difference([0]) == 0

def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_floats():
    assert double_the_difference([1.0, 3.0, 2.5, 0.0]) == 10

def test_double_the_difference_large_numbers():
    assert double_the_difference([101, 203, 305]) == 101**2 + 203**2 + 305**2

def test_double_the_difference_all_even():
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_double_the_difference_all_negative():
    assert double_the_difference([-1, -3, -5]) == 0

def test_double_the_difference_mixed_types():
    assert double_the_difference([1, "a", 3, 2.5, 5]) == 35