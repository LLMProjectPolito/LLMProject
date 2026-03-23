import pytest
import math


# Focus: Boundary Values
def test_simplify_true():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("10/2", "2/1") == True

def test_simplify_false():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/3", "2/1") == False

# Focus: Type Scenarios
def test_simplify_true():
    assert simplify("1/5", "5/1") == True

def test_simplify_false_1():
    assert simplify("1/6", "2/1") == False

def test_simplify_false_2():
    assert simplify("7/10", "10/2") == False

# Focus: Logic Branches
def test_simplify_true():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("10/2", "2/1") == True

def test_simplify_false():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/3", "2/1") == False