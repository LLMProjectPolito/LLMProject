import pytest
import math

def test_int_to_mini_roman_max_value():
    """Test the function with the maximum allowed input value (1000)."""
    assert int_to_mini_roman(1000) == 'm'

def test_edge_case_max_value():
    """Test the maximum allowed value (1000) to ensure correct roman numeral conversion."""
    assert int_to_mini_roman(1000) == 'm'