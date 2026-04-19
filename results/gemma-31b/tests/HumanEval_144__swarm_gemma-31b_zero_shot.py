
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

def test_simplify_large_precision():
    # Tests precision for very large numbers to ensure the implementation 
    # uses integer arithmetic rather than floating point division.
    # (2/3) * (30000000000000003/2) = 60000000000000006 / 6 = 10000000000000001
    assert simplify("2/3", "30000000000000003/2") is True

def test_simplify_precision():
    # This case tests if the implementation avoids floating point precision errors.
    # (1/3) * 30000000000000001 is not a whole number, but using float division 
    # (1/3) * 30000000000000001.0 would evaluate to 10000000000000000.0 in Python.
    assert simplify("1/3", "30000000000000001/1") == False