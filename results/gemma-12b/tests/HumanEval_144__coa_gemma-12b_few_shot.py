
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """

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