import pytest
import math

def test_simplify_positive():
    assert simplify("1/5", "5/1") == True

def test_simplify_edge_case_zero_numerator():
    """Test case with zero numerator in both fractions."""
    assert simplify("0/1", "0/1") == True

def test_simplify_invalid_fraction_format():
    """Tests the simplify function with an invalid fraction format."""
    assert simplify("1/5a", "5/1") == False
    assert simplify("1/5", "5/1b") == False
    assert simplify("1", "5/1") == False
    assert simplify("1/5", "1") == False
    assert simplify("1/-5", "5/1") == False
    assert simplify("1/5", "-5/1") == False
    assert simplify("1/0", "5/1") == False
    assert simplify("1/5", "0/1") == False