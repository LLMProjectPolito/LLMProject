import pytest
import math


# Focus: Boundary Values
def test_simplify_boundary_numerator_denominator_equal():
    assert simplify("1/1", "1/1") == True

def test_simplify_boundary_numerator_one_denominator_large():
    assert simplify("1/1000", "1000/1") == True

def test_simplify_boundary_denominator_one_numerator_large():
    assert simplify("1000/1", "1/1000") == True

# Focus: Type Scenarios
def test_simplify_whole_number_result():
    assert simplify("1/5", "5/1") == True

def test_simplify_non_whole_number_result():
    assert simplify("1/6", "2/1") == False

def test_simplify_another_non_whole_number_result():
    assert simplify("7/10", "10/2") == False

# Focus: Logic Branches
def test_simplify_whole_number_result():
    assert simplify("1/5", "5/1") == True

def test_simplify_non_whole_number_result():
    assert simplify("1/6", "2/1") == False

def test_simplify_another_non_whole_number_result():
    assert simplify("7/10", "10/2") == False