
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
    result = x_frac * n_frac
    return result.denominator == 1

class TestSimplify:
    def test_simplify_true(self):
        assert simplify("1/5", "5/1") == True
        assert simplify("2/2", "1/1") == True
        assert simplify("1/1", "1/1") == True
        assert simplify("4/2", "2/2") == True
        assert simplify("3/3", "2/2") == True
        assert simplify("1/3", "3/1") == True
        assert simplify("2/4", "4/2") == True

    def test_simplify_false(self):
        assert simplify("1/6", "2/1") == False
        assert simplify("7/10", "10/2") == False
        assert simplify("1/2", "1/3") == False
        assert simplify("1/4", "1/2") == False
        assert simplify("2/3", "1/2") == False
        assert simplify("1/5", "2/1") == False
        assert simplify("3/4", "1/3") == False

    def test_simplify_large_numbers(self):
        assert simplify("100/200", "200/100") == True
        assert simplify("1000/2000", "2000/1000") == True
        assert simplify("100/300", "300/100") == False

    def test_simplify_edge_cases(self):
        assert simplify("1/1", "2/1") == False
        assert simplify("2/1", "1/1") == False
        assert simplify("1/2", "2/2") == False
        assert simplify("2/2", "1/2") == False

    def test_simplify_same_fraction(self):
        assert simplify("1/2", "1/2") == False
        assert simplify("2/3", "2/3") == False
        assert simplify("3/4", "3/4") == False

    def test_simplify_with_one(self):
        assert simplify("1/1", "5/1") == True
        assert simplify("5/1", "1/1") == True
        assert simplify("1/2", "1/1") == False
        assert simplify("1/1", "1/2") == False