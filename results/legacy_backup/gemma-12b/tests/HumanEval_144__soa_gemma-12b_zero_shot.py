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
    def test_simplify_true_case_1(self):
        assert simplify("1/5", "5/1") == True

    def test_simplify_false_case_1(self):
        assert simplify("1/6", "2/1") == False

    def test_simplify_false_case_2(self):
        assert simplify("7/10", "10/2") == False

    def test_simplify_true_case_2(self):
        assert simplify("1/2", "2/1") == True

    def test_simplify_true_case_3(self):
        assert simplify("3/4", "4/3") == True

    def test_simplify_false_case_3(self):
        assert simplify("1/3", "2/5") == False

    def test_simplify_true_case_4(self):
        assert simplify("2/7", "7/2") == True

    def test_simplify_false_case_4(self):
        assert simplify("1/4", "3/5") == False

    def test_simplify_true_case_5(self):
        assert simplify("5/8", "8/5") == True

    def test_simplify_false_case_5(self):
        assert simplify("1/7", "3/4") == False

    def test_simplify_large_numbers_true(self):
        assert simplify("100/200", "200/100") == True

    def test_simplify_large_numbers_false(self):
        assert simplify("100/201", "201/100") == False

    def test_simplify_same_number_true(self):
        assert simplify("1/1", "1/1") == True

    def test_simplify_zero_numerator_true(self):
        assert simplify("0/1", "1/1") == True

    def test_simplify_zero_numerator_false(self):
        assert simplify("0/1", "1/2") == False

    def test_simplify_complex_true(self):
        assert simplify("2/3", "3/2") == True

    def test_simplify_complex_false(self):
        assert simplify("2/5", "3/7") == False