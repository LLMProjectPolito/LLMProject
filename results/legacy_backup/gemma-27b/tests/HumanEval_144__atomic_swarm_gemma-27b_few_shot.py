import pytest
import math

def test_simplify_positive():
    assert simplify("1/5", "5/1") == True

def test_simplify_edge_zero_numerator():
    assert simplify("0/1", "1/1") == True
    assert simplify("1/2", "0/1") == True

def test_simplify_invalid_fraction_format():
    assert simplify("1/5a", "5/1") == False
    assert simplify("1/5", "5/1b") == False