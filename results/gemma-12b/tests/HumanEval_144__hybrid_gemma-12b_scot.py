
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
    simplify("7/10", "10/2") == False
    """
    x_frac = Fraction(x)
    n_frac = Fraction(n)
    product = x_frac * n_frac
    return product.numerator % product.denominator == 0

class TestSimplify:
    def test_simplify_whole_number(self):
        assert simplify("1/2", "2/1") == True
        assert simplify("1/3", "3/1") == True
        assert simplify("2/4", "2/1") == True

    def test_simplify_not_whole_number(self):
        assert simplify("1/6", "2/1") == False
        assert simplify("7/10", "10/2") == False
        assert simplify("1/5", "2/3") == False

    def test_simplify_fraction_equal_to_one(self):
        assert simplify("1/1", "1/1") == True
        assert simplify("2/2", "1/1") == True
        assert simplify("1/1", "3/3") == True

    def test_simplify_fraction_equal_to_zero(self):
        assert simplify("0/1", "1/1") == True
        assert simplify("1/1", "0/1") == True
        assert simplify("0/2", "5/1") == True

    def test_simplify_large_numbers(self):
        assert simplify("100/2", "2/1") == True
        assert simplify("100/3", "3/1") == True
        assert simplify("1000/10", "10/1") == True

    def test_simplify_same_fraction(self):
        assert simplify("1/2", "1/2") == False
        assert simplify("2/3", "2/3") == False
        assert simplify("1/1", "1/1") == True

    def test_simplify_edge_case_1(self):
        assert simplify("3/4", "8/3") == False

    def test_simplify_edge_case_2(self):
        assert simplify("5/7", "14/5") == False

    def test_simplify_negative_result(self):
        assert simplify("-1/2", "2/1") == True
        assert simplify("1/2", "-2/1") == True

    def test_simplify_denominator_one(self):
        assert simplify("1/5", "5/1") == True
        assert simplify("2/3", "3/1") == True
        assert simplify("1/2", "4/1") == True

    def test_simplify_numerator_one(self):
        assert simplify("1/4", "2/5") == False
        assert simplify("1/5", "3/7") == False

    def test_simplify_complex_fractions(self):
        assert simplify("2/3", "3/4") == False
        assert simplify("3/5", "10/3") == True
        assert simplify("1/2", "4/7") == False

    def test_simplify_x_equals_one(self):
        assert simplify("1/1", "2/3") == False

    def test_simplify_n_equals_one(self):
        assert simplify("3/4", "1/1") == False

    def test_simplify_x_and_n_equal_one(self):
        assert simplify("1/1", "1/1") == True