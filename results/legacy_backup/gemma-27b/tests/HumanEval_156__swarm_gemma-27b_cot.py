import pytest

def test_int_to_mini_roman_edge_case_900():
    assert int_to_mini_roman(900) == 'cm'

def test_int_to_mini_roman_edge_case_999():
    assert int_to_mini_roman(999) == 'cmxcix'