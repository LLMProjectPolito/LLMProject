import pytest

def test_simplify_edge_case_large_numbers():
    """Test case for large numerator and denominator values to check for potential overflow or precision issues."""
    assert simplify("999999999999999/1000000000000000", "1000000000000000/999999999999999") == True