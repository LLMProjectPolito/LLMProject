
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

def test_simplify_complex_whole_number():
    # Case: (10/3) * (3/2) = 30/6 = 5, which is a whole number.
    assert simplify("10/3", "3/2") is True

def test_simplify_precision_loss():
    # This case tests whether the implementation uses exact integer arithmetic 
    # instead of floating point division. 
    # (10^16 + 1) / 10^16 is 1.0000000000000001, which is not a whole number.
    # Floating point division in Python would round this to 1.0.
    assert simplify("10000000000000001/1", "1/10000000000000000") is False

def test_simplify_cross_cancelation_whole_number():
    """
    Tests a case where neither fraction is a whole number, but their product is.
    This specifically checks if the implementation avoids floating point precision 
    errors (e.g., 20/7 is a repeating decimal).
    """
    assert simplify("7/10", "20/7") is True