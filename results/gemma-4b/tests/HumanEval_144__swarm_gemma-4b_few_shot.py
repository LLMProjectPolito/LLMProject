
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

def simplify(frac1, frac2):
    """
    This function takes two fractions in the form 'a/b' and returns True if they are equivalent, False otherwise.
    """
    num1, den1 = map(int, frac1.split('/'))
    num2, den2 = map(int, frac2.split('/'))
    return math.gcd(num1, num2) == math.gcd(den1, den2)

def test_simplify_true():
    assert simplify("1/5", "5/1") == True

def test_simplify_true():
    assert simplify("1/5", "5/1") == True

def test_simplify_true():
    assert simplify("1/5", "5/1") == True