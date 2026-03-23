import pytest

def test_empty_list():
    assert double_the_difference([]) == 0

def test_only_even_numbers():
    assert double_the_difference([2, 4, 6, 0]) == 0

def test_only_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 1 + 9 + 25

def test_mixed_odd_and_even():
    assert double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25

def test_negative_numbers():
    assert double_the_difference([-1, -3, 2, 5]) == 25

def test_float_numbers():
    assert double_the_difference([1.5, 2.0, 3.5]) == 0

def test_integers_and_floats():
    assert double_the_difference([1, 2.5, 3, 4.0, 5]) == 1 + 9 + 25

def test_with_zero():
    assert double_the_difference([0, 1, 2, 3]) == 1 + 9

def test_large_numbers():
    assert double_the_difference([1001, 2003]) == 1001**2 + 2003**2

def test_single_odd_number():
    assert double_the_difference([7]) == 49

def test_single_even_number():
    assert double_the_difference([4]) == 0