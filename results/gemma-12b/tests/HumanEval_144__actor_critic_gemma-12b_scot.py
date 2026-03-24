
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
from fractions import Fraction

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
    x_frac = Fraction(x)
    n_frac = Fraction(n)
    product = x_frac * n_frac
    return product.denominator == 1

def test_simplify_true():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("2/1", "1/2") == True
    assert simplify("3/4", "4/3") == True
    assert simplify("2/2", "4/4") == True
    assert simplify("3/3", "4/4") == True
    assert simplify("5/5", "1/1") == True
    assert simplify("123456789/1", "1/123456789") == True
    assert simplify("987654321/1", "1/987654321") == True

def test_simplify_false():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "1/3") == False
    assert simplify("2/5", "3/7") == False
    assert simplify("1/4", "2/3") == False
    assert simplify("2/1", "3/1") == False
    assert simplify("1/1", "2/1") == False

def test_simplify_zero_numerator():
    assert simplify("0/1", "1/1") == True
    assert simplify("1/1", "0/1") == True
    assert simplify("0/1", "1/2") == True
    assert simplify("1/2", "0/1") == True
    assert simplify("0/1", "0/1") == True

def test_simplify_fractions_with_denominator_one():
    assert simplify("5/1", "1/5") == True
    assert simplify("1/1", "5/1") == True
    assert simplify("5/1", "1/1") == True
    assert simplify("2/1", "3/1") == False
    assert simplify("1/1", "2/1") == True
    assert simplify("2/2", "1/1") == True
    assert simplify("1/1", "2/2") == True
    assert simplify("3/3", "4/4") == True
    assert simplify("5/5", "1/1") == True

def test_simplify_large_numbers():
    assert simplify("1000/2", "2/1000") == True
    assert simplify("1000/3", "3/1000") == True
    assert simplify("1000000/7", "7/1000000") == True
    assert simplify("1000/5", "11/1000") == False