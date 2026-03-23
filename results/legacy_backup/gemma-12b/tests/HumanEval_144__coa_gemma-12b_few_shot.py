import pytest
import math


# Focus: Boundary Values
import pytest

def test_simplify_boundary_numerator_denominator_equal():
    assert simplify("1/1", "1/1") == True

def test_simplify_boundary_numerator_one_denominator_one():
    assert simplify("1/1", "1/2") == False

def test_simplify_boundary_numerator_one_denominator_large():
    assert simplify("1/1", "100/1") == False

# Focus: Type Scenarios
def test_simplify_whole_number():
    assert simplify("1/5", "5/1") == True

def test_simplify_not_whole_number():
    assert simplify("1/6", "2/1") == False

def test_simplify_another_not_whole_number():
    assert simplify("7/10", "10/2") == False

# Focus: Logic Branches
def test_simplify_whole_number():
    assert simplify("1/5", "5/1") == True

def test_simplify_not_whole_number():
    assert simplify("1/6", "2/1") == False

def test_simplify_another_not_whole_number():
    assert simplify("7/10", "10/2") == False