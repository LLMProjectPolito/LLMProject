import pytest
import math

def test_truncate_number_edge_cases():
    # Test the truncation of a number that is exactly halfway between two integers
    assert truncate_number(10.5) == 0.0
    # Test the function with a zero input to catch any potential edge cases
    assert truncate_number(0) == 0.0

def test_truncate_number_truncates_at_zero():
    """
    Test truncating a number that is less than 1.
    """
    assert truncate_number(0.5) == 0.5