
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
def test_simplify_boundary_minimum():
    # Smallest possible positive whole numbers for numerators and denominators
    assert simplify("1/1", "1/1") is True

def test_simplify_boundary_just_below_whole():
    # Product is the smallest possible positive non-whole number (1/2)
    assert simplify("1/2", "1/1") is False

def test_simplify_boundary_large_values():
    # Large values that simplify exactly to a whole number
    assert simplify("1000000/1", "1/1000000") is True

# Focus: Logic Branches
import pytest

def test_simplify_returns_true_for_whole_number():
    # Case where result is exactly 1
    assert simplify("1/5", "5/1") is True
    # Case where result is a whole number greater than 1
    assert simplify("3/2", "4/1") is True
    # Case where result is a whole number via cross-simplification
    assert simplify("3/4", "8/3") is True

def test_simplify_returns_false_for_non_whole_number():
    # Case where result is a proper fraction
    assert simplify("1/6", "2/1") is False
    # Case where result is an improper fraction (not a whole number)
    assert simplify("7/10", "10/2") is False
    # Case where result is a very small fraction
    assert simplify("1/10", "1/10") is False

# Focus: Mathematical Edge Cases
import pytest

def test_simplify_reciprocals():
    # Product is exactly 1, which is a whole number
    assert simplify("123/456", "456/123") is True
    assert simplify("1/1", "1/1") is True

def test_simplify_large_whole_product():
    # Product results in a large whole number
    assert simplify("1000/1", "1000/1") is True
    assert simplify("50/3", "3/1") is True

def test_simplify_near_whole_number():
    # Product is very close to a whole number but is a fraction
    assert simplify("1/3", "10/3") is False  # 10/9
    assert simplify("99/100", "100/98") is False  # 99/98