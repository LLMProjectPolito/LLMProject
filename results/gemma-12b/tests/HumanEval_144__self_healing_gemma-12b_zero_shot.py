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

class TestSimplify:
    def test_simplify_true(self):
        assert simplify("1/5", "5/1") == True
        assert simplify("2/2", "1/1") == True
        assert simplify("1/1", "1/1") == True
        assert simplify("3/3", "2/2") == True
        assert simplify("4/4", "1/1") == True
        assert simplify("1/2", "2/1") == True
        assert simplify("1/3", "3/1") == True
        assert simplify("1/4", "4/1") == True
        assert simplify("1/5", "5/1") == True
        assert simplify("1/6", "6/1") == True
        assert simplify("1/7", "7/1") == True
        assert simplify("1/8", "8/1") == True
        assert simplify("1/9", "9/1") == True
        assert simplify("1/10", "10/1") == True

    def test_simplify_false(self):
        assert simplify("1/6", "2/1") == False
        assert simplify("7/10", "10/2") == False
        assert simplify("1/2", "3/1") == False
        assert simplify("1/3", "2/1") == False
        assert simplify("1/4", "3/1") == False
        assert simplify("1/5", "2/1") == False
        assert simplify("1/6", "3/1") == False
        assert simplify("1/7", "2/1") == False
        assert simplify("1/8", "3/1") == False
        assert simplify("1/9", "2/1") == False
        assert simplify("1/10", "3/1") == False
        assert simplify("2/3", "1/2") == False
        assert simplify("3/4", "1/2") == False
        assert simplify("4/5", "1/2") == False
        assert simplify("5/6", "1/2") == False
        assert simplify("6/7", "1/2") == False
        assert simplify("7/8", "1/2") == False
        assert simplify("8/9", "1/2") == False
        assert simplify("9/10", "1/2") == False
        assert simplify("1/2", "1/3") == False
        assert simplify("1/3", "1/4") == False
        assert simplify("1/4", "1/5") == False
        assert simplify("1/5", "1/6") == False
        assert simplify("1/6", "1/7") == False
        assert simplify("1/7", "1/8") == False
        assert simplify("1/8", "1/9") == False
        assert simplify("1/9", "1/10") == False

    def test_edge_cases(self):
        assert simplify("1/1", "2/2") == True
        assert simplify("2/2", "1/1") == True
        assert simplify("100/1", "1/100") == False
        assert simplify("100/1", "100/1") == True
        assert simplify("1/100", "100/1") == False
        assert simplify("100/100", "1/1") == True
        assert simplify("1/100", "1/1") == False
        assert simplify("100/1", "1/1") == False