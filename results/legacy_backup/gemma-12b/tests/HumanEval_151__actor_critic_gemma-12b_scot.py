import pytest
from your_module import double_the_difference  # Replace your_module

def test_empty_list():
    assert double_the_difference([]) == 0

def test_positive_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 35

def test_mixed_numbers():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_negative_and_positive():
    assert double_the_difference([9, -2]) == 81

def test_non_integer_numbers():
    assert double_the_difference([1.5, 2.0, 3.7]) == 0

def test_mixed_types():
    assert double_the_difference([1, 2.5, "a", 3]) == 10

def test_only_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_large_list():
    result = 1 + 9 + 25 + 49 + 81 + 121
    assert double_the_difference([1, 3, 5, 7, 9, 11]) == result

def test_large_numbers():
    assert double_the_difference([1001, 1003]) == 2008010

def test_single_odd_number():
    assert double_the_difference([7]) == 49

def test_single_even_number():
    assert double_the_difference([4]) == 0

def test_zero_only():
    assert double_the_difference([0]) == 0

def test_empty_with_non_numeric():
    assert double_the_difference(["a", "b", "c"]) == 0

def test_single_non_numeric():
    assert double_the_difference([1, "a", 2]) == 0