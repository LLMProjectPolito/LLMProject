import pytest
import math

def test_string_sequence_zero():
    """Edge case test: string_sequence(0) returns an empty string"""
    assert string_sequence(0) == ''

def test_string_sequence_single_digit():
    """Test that the function returns a string with a single digit when n == 9"""
    assert string_sequence(9) == '0 1 2 3 4 5 6 7 8 9'