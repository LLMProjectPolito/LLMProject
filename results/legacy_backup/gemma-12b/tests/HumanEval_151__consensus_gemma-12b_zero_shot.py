import pytest
from your_module import double_the_difference  # Replace your_module

def test_empty_list():
    assert double_the_difference([]) == 0

def test_positive_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 1 + 9 + 25

def test_mixed_positive_and_even_numbers():
    assert double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25

def test_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_negative_and_positive_numbers():
    assert double_the_difference([-1, 2, 3, -4, 5]) == 1 + 9 + 25

def test_zero_and_odd_numbers():
    assert double_the_difference([0, 1, 3]) == 1 + 9

def test_zero_only():
    assert double_the_difference([0]) == 0

def test_single_odd_number():
    assert double_the_difference([7]) == 49

def test_single_even_number():
    assert double_the_difference([2]) == 0

def test_single_negative_number():
    assert double_the_difference([-5]) == 0

def test_mixed_numbers_with_zero():
    assert double_the_difference([1, -2, 0, 3, -4, 5]) == 1 + 9 + 25

def test_all_even_numbers():
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_large_numbers():
    assert double_the_difference([11, 21, 31]) == 121 + 441 + 961

def test_decimal_numbers():
    assert double_the_difference([1.5, 2.0, 3.5]) == 0

def test_string_numbers():
    assert double_the_difference(['1', '2', '3']) == 0

def test_mixed_data_types():
    assert double_the_difference([1, 2.5, '3', -4, 5]) == 1 + 25

def test_complex_list():
    assert double_the_difference([1, 3, 2, 0, -1, -2, 5, 7, 4]) == 1 + 9 + 0 + 25 + 49