import pytest
import math

def test_simplify_edge_case_numerator_zero_1():
    """Test case where the numerator of x is zero."""
    assert simplify("0/1", "1/1") == True

def test_simplify_edge_case_numerator_zero_2():
    """Test case where the numerator of x is zero."""
    assert simplify("0/5", "5/1") == True

def test_simplify_edge_case_numerator_zero_3():
    """Test case where the numerator of x is zero."""
    assert simplify("0/5", "5/1") == True