import pytest
import math

def test_simplify_basic():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False

def test_simplify_true():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("10/2", "2/1") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("10/1", "1/1") == False

def test_simplify_false():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/3", "2/1") == False
    assert simplify("1/2", "3/1") == False

def test_simplify_true():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("10/2", "2/1") == True
    assert simplify("1/1", "1/1") == True