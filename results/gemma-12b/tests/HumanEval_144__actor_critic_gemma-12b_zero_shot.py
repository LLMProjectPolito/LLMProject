
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
    def test_basic_true(self):
        assert simplify("1/5", "5/1") == True

    def test_basic_false(self):
        assert simplify("1/6", "2/1") == False

    def test_another_false(self):
        assert simplify("7/10", "10/2") == False

    def test_whole_number_x(self):
        assert simplify("1/1", "2/1") == True

    def test_whole_number_n(self):
        assert simplify("2/1", "1/1") == True

    def test_both_whole_numbers(self):
        assert simplify("1/1", "1/1") == True

    def test_large_numbers_true(self):
        assert simplify("100/2", "2/100") == True

    def test_large_numbers_false(self):
        assert simplify("100/3", "3/100") == False

    def test_edge_case_1(self):
        assert simplify("1/2", "1/2") == False

    def test_edge_case_2(self):
        assert simplify("1/3", "3/1") == True

    def test_edge_case_3(self):
        assert simplify("2/3", "3/2") == False

    def test_edge_case_4(self):
        assert simplify("1/7", "7/1") == True

    def test_edge_case_5(self):
        assert simplify("1/8", "8/1") == True

    def test_edge_case_6(self):
        assert simplify("1/9", "9/1") == True

    def test_edge_case_7(self):
        assert simplify("1/10", "10/1") == True

    def test_edge_case_8(self):
        assert simplify("1/11", "11/1") == True

    def test_edge_case_9(self):
        assert simplify("1/12", "12/1") == False

    def test_edge_case_10(self):
        assert simplify("1/13", "13/1") == True