import pytest
import math

def test_int_to_mini_roman_positive_case():
    assert int_to_mini_roman(19) == 'xix'

def test_int_to_mini_roman_edge_case_minimum():
    """Test the minimum possible input value (1)."""
    assert int_to_mini_roman(1) == "i"

def test_invalid_input_type():
    """Test with a non-integer input."""
    try:
        int_to_mini_roman("abc")
    except TypeError as e:
        assert str(e) == "int_to_mini_roman() argument must be an integer, not str"
    else:
        assert False, "TypeError not raised for string input"

def test_input_less_than_one():
    """Test with an input less than 1."""
    try:
        int_to_mini_roman(0)
    except ValueError as e:
        assert str(e) == "Input must be between 1 and 1000"
    else:
        assert False, "ValueError not raised for input 0"

def test_input_greater_than_1000():
    """Test with an input greater than 1000."""
    try:
        int_to_mini_roman(1001)
    except ValueError as e:
        assert str(e) == "Input must be between 1 and 1000"
    else:
        assert False, "ValueError not raised for input 1001"