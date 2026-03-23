import pytest
import math

def test_get_max_triples_positive():
    """Test with a positive integer n = 5."""
    assert get_max_triples(5) == 1

def test_get_max_triples_empty_input():
    """Test with n = 0, which results in an empty array."""
    assert get_max_triples(0) == 0

def test_get_max_triples_negative_input():
    """Test with a negative input value for n."""
    try:
        from solution import get_max_triples
        get_max_triples(-1)
        assert False, "Should have raised ValueError for negative input"
    except ValueError as e:
        assert str(e) == "Input must be a positive integer."