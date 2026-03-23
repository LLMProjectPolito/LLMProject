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
    return product.numerator % product.denominator == 0


class TestSimplify:
    def test_whole_number_product(self):
        assert simplify("1/5", "5/1") == True
        assert simplify("2/3", "3/2") == True
        assert simplify("4/7", "7/4") == True

    def test_non_whole_number_product(self):
        assert simplify("1/6", "2/1") == False
        assert simplify("7/10", "10/2") == False
        assert simplify("1/2", "1/3") == False

    def test_denominator_one(self):
        assert simplify("1/1", "2/1") == True
        assert simplify("3/1", "1/1") == True
        assert simplify("2/1", "1/1") == True
        assert simplify("1/1", "1/1") == True

    def test_numerator_one(self):
        assert simplify("1/5", "5/1") == True
        assert simplify("1/2", "3/4") == False
        assert simplify("1/3", "6/1") == True

    def test_large_numbers(self):
        assert simplify("123/456", "456/123") == True
        assert simplify("100/200", "300/100") == True
        assert simplify("101/202", "202/101") == True
        assert simplify("10/11", "11/10") == False

    def test_edge_case_one(self):
        assert simplify("1/1", "1/1") == True

    def test_edge_case_zero_product(self):
        assert simplify("0/1", "1/1") == True # Technically not allowed by prompt, but good to test
        assert simplify("1/1", "0/1") == True

    def test_simplify_fraction_equal_to_one(self):
        assert simplify("1/1", "2/2") == True
        assert simplify("3/3", "4/4") == True
        assert simplify("1/2", "1/1") == False

    def test_simplify_fraction_equal_to_zero(self):
        assert simplify("0/1", "1/1") == True
        assert simplify("1/1", "0/1") == True
        assert simplify("0/2", "2/3") == False

    def test_simplify_large_numbers(self):
        assert simplify("12345/67890", "67890/12345") == True
        assert simplify("1000/1001", "1001/1000") == False

    def test_simplify_same_fraction(self):
        assert simplify("1/2", "1/2") == False
        assert simplify("2/3", "2/3") == False
        assert simplify("1/1", "1/1") == True

    def test_simplify_edge_case_1(self):
        assert simplify("2/4", "4/2") == True

    def test_simplify_edge_case_2(self):
        assert simplify("3/7", "14/3") == False