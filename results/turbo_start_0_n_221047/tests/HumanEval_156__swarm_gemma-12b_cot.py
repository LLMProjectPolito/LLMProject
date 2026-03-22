import pytest
import math

def test_edge_case_max_value():
    """Test the maximum allowed value (1000) to ensure correct roman numeral conversion."""
    assert int_to_mini_roman(1000) == 'm'