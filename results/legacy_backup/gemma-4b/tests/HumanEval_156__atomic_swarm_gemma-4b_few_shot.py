import pytest
import math

def test_int_to_mini_roman_basic():
    assert int_to_mini_roman(19) == 'xix'

def test_int_to_mini_roman_edge_case():
    assert int_to_mini_roman(1) == 'i'

def test_int_to_mini_roman_invalid_input():
    assert int_to_mini_roman(0) == None
    assert int_to_mini_roman(1001) == None