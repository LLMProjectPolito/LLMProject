import pytest
import math

def test_simplify_basic():
    assert simplify("1/5", "5/1") == True

def test_simplify_edge_case_zero_numerator():
    assert simplify("0/1", "1/1") == True

def test_simplify_invalid_input():
    assert simplify("1/5", "0/1") == False