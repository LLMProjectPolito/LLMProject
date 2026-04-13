
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

class TestSimplify:
    def test_simplify_true_1(self):
        assert simplify("1/5", "5/1") == True

    def test_simplify_false_1(self):
        assert simplify("1/6", "2/1") == False

    def test_simplify_false_2(self):
        assert simplify("7/10", "10/2") == False

    def test_simplify_true_2(self):
        assert simplify("1/2", "2/1") == True

    def test_simplify_true_3(self):
        assert simplify("3/4", "4/3") == True

    def test_simplify_false_3(self):
        assert simplify("1/3", "2/5") == False

    def test_simplify_large_numbers_true(self):
        assert simplify("100/200", "200/100") == True

    def test_simplify_large_numbers_false(self):
        assert simplify("100/201", "201/100") == False

    def test_simplify_same_fraction(self):
        assert simplify("1/1", "1/1") == True

    def test_simplify_one_is_one(self):
        assert simplify("1/2", "1/1") == False

    def test_simplify_one_is_one_true(self):
        assert simplify("1/1", "2/1") == True

    def test_simplify_zero_numerator(self):
        assert simplify("0/1", "1/1") == True

    def test_simplify_zero_numerator_false(self):
        assert simplify("0/1", "1/2") == False

    def test_simplify_complex_fractions_true(self):
        assert simplify("2/3", "3/2") == True

    def test_simplify_complex_fractions_false(self):
        assert simplify("2/3", "5/7") == False