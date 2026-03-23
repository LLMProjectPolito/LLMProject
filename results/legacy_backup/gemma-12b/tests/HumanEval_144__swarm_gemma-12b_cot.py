import pytest
import math

def test_simplify_edge_case_large_numbers():
    """Tests the simplify function with large numerator and denominator values to check for potential overflow issues."""
    assert simplify("1000000000/1", "1/1000000000") == True