import pytest
import math

def test_int_to_mini_roman_positive():
    assert int_to_mini_roman(19) == 'xix'

def test_int_to_mini_roman_minimum_value():
    """
    Test the minimum possible input value (1) to ensure the function handles it correctly.
    """
    assert int_to_mini_roman(1) == "i"

def test_invalid_boundary_zero():
    """Test that the function raises ValueError when input is zero."""
    try:
        int_to_mini_roman(0)
        assert False, "ValueError not raised for zero input"
    except ValueError as e:
        assert str(e) == "Number must be between 1 and 1000"

def test_invalid_boundary_negative():
    """Test that the function raises ValueError when input is negative."""
    try:
        int_to_mini_roman(-1)
        assert False, "ValueError not raised for negative input"
    except ValueError as e:
        assert str(e) == "Number must be between 1 and 1000"

def test_invalid_boundary_large():
    """Test that the function raises ValueError when input is greater than 1000."""
    try:
        int_to_mini_roman(1001)
        assert False, "ValueError not raised for input greater than 1000"
    except ValueError as e:
        assert str(e) == "Number must be between 1 and 1000"