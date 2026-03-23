import pytest

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

def test_zero():
    assert double_the_difference([0]) == 0

def test_zero_and_odd():
    assert double_the_difference([0, 1, 3]) == 1 + 9

def test_zero_and_even():
    assert double_the_difference([0, 2, 4]) == 0

def test_floats():
    assert double_the_difference([1.5, 2.0, 3.5]) == 0

def test_mixed_types():
    assert double_the_difference([1, 2.0, "a", 3]) == 1 + 9

def test_large_numbers():
    assert double_the_difference([1001, 3003]) == 1001**2 + 3003**2

def test_single_odd_number():
    assert double_the_difference([7]) == 49

def test_single_even_number():
    assert double_the_difference([4]) == 0

def test_multiple_odd_numbers_with_zeros():
    assert double_the_difference([1, 0, 3, 0, 5]) == 1 + 9 + 25

def test_all_negative_and_non_integer():
    assert double_the_difference([-1.5, -2, "a"]) == 0