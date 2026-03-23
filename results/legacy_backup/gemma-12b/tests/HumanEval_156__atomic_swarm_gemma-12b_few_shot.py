import pytest
import math

def test_int_to_mini_roman_basic():
    assert int_to_mini_roman(19) == 'xix'

def test_int_to_mini_roman_max():
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_invalid_input():
    assert int_to_mini_roman(0) == None