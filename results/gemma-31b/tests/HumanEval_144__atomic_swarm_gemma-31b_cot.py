
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

def test_simplify():
    assert simplify("1/5", "5/1") == True

def test_minimal_input():
    assert simplify("1/1", "1/1") == True

def test_simplify_precision():
    # This case tests for floating point precision errors (e.g., 0.333... * 3 might not equal 1.0)
    assert simplify("1/3", "3/1") is True