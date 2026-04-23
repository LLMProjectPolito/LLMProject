
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
    def test_simplify_true_case_1(self):
        assert simplify("1/5", "5/1") == True

    def test_simplify_true_case_2(self):
        assert simplify("2/4", "2/1") == True

    def test_simplify_true_case_3(self):
        assert simplify("3/6", "2/1") == True

    def test_simplify_false_case_1(self):
        assert simplify("1/6", "2/1") == False

    def test_simplify_false_case_2(self):
        assert simplify("7/10", "10/2") == False

    def test_simplify_false_case_3(self):
        assert simplify("1/2", "1/3") == False

    def test_simplify_with_larger_numbers_true(self):
        assert simplify("12/4", "2/1") == True

    def test_simplify_with_larger_numbers_false(self):
        assert simplify("12/5", "5/2") == False

    def test_simplify_with_same_numerator_and_denominator_true(self):
        assert simplify("1/1", "1/1") == True

    def test_simplify_with_one_as_denominator_true(self):
        assert simplify("1/1", "2/1") == True

    def test_simplify_with_one_as_denominator_false(self):
        assert simplify("1/2", "1/1") == False

    def test_simplify_edge_case_1(self):
        assert simplify("1/100", "100/1") == True

    def test_simplify_edge_case_2(self):
        assert simplify("1/101", "101/1") == True

    def test_simplify_edge_case_3(self):
        assert simplify("1/102", "102/1") == True

    def test_simplify_complex_true(self):
        assert simplify("4/8", "6/3") == True

    def test_simplify_complex_false(self):
        assert simplify("4/9", "6/3") == False