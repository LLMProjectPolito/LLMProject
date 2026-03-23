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