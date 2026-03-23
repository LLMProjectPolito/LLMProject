import pytest
import math

def test_basic():
    assert simplify("1/5", "5/1") == True

def test_edge_zero_numerator():
    assert simplify("0/1", "1/1") == True

def test_simplify_invalid_type():
    """Test with invalid input types."""
    try:
        simplify(1, "2/3")
        assert False, "Should have raised a TypeError"
    except TypeError:
        pass
    try:
        simplify("1/2", 2)
        assert False, "Should have raised a TypeError"
    except TypeError:
        pass