import pytest
import math

def test_basic():
    assert simplify("1/5", "5/1") == True

def test_edge():
    assert simplify("1/1", "1/1") == True

def test_simplify_invalid_fraction_format():
    assert simplify("1/5", "5/0") == False