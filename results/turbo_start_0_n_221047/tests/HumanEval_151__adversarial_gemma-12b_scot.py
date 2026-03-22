import pytest
from your_module import double_the_difference  # Replace your_module

def test_empty_list():
    assert double_the_difference([]) == 0

def test_only_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_only_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 1 + 9 + 25

def test_mixed_odd_and_even():
    assert double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25

def test_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_non_integer_numbers():
    assert double_the_difference([1.5, 2.0, 3.7]) == 0

def test_mixed_valid_and_invalid():
    assert double_the_difference([1, -2, 3.0, 5, -6]) == 1 + 25

def test_zero_in_list():
    assert double_the_difference([0, 1, 2, 3]) == 1 + 9

def test_large_numbers():
    assert double_the_difference([1, 999]) == 1 + 998001

def test_single_odd_number():
    assert double_the_difference([7]) == 49