
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

def test_simplify_whole_number_fractions():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/1", "5/1") == True
    assert simplify("100/2", "2/1") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("1000/2", "2/1") == True

def test_simplify_non_whole_number_fractions():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("100/3", "3/1") == False

def test_simplify_numerator_one():
    assert simplify("1/2", "3/4") == False
    assert simplify("1/1", "2/1") == True
    assert simplify("1/3", "1/1") == False

def test_simplify_denominator_one():
    assert simplify("2/1", "5/1") == True
    assert simplify("1/1", "2/1") == True

def test_simplify_large_numbers():
    assert simplify("1000000/2", "2/1") == True
    assert simplify("1000000/3", "3/1") == False

def test_simplify_equal_fractions():
    assert simplify("1/2", "2/1") == True
    assert simplify("2/3", "3/2") == True