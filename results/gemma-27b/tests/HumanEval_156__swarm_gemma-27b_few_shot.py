import pytest

def test_int_to_mini_roman_edge_999():
    assert int_to_mini_roman(999) == 'cmxcix'

def test_int_to_mini_roman_edge_case():
    assert int_to_mini_roman(1000) == 'm'