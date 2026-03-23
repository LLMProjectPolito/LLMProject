import pytest

def test_double_the_difference_basic():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_double_the_difference_negative():
    assert double_the_difference([-1, -2, 0]) == 0

def test_double_the_difference_single_positive():
    assert double_the_difference([9, -2]) == 81

def test_double_the_difference_single_zero():
    assert double_the_difference([0]) == 0

def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_mixed():
    assert double_the_difference([1, -2, 3, 4, -5]) == 1 + 9 + 25

def test_double_the_difference_floats():
    assert double_the_difference([1.5, 2, 3.0]) == 0

def test_double_the_difference_strings():
    assert double_the_difference([1, "a", 3]) == 1 + 9

def test_double_the_difference_all_even():
    assert double_the_difference([2, 4, 6]) == 0

def test_double_the_difference_all_negative():
    assert double_the_difference([-1, -3, -5]) == 0

def test_double_the_difference_large_numbers():
    assert double_the_difference([1001, 2002, 3003]) == 1001*1001 + 3003*3003