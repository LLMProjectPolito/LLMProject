
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
    def test_whole_number_result(self):
        assert simplify("1/5", "5/1") == True

    def test_non_whole_number_result(self):
        assert simplify("1/6", "2/1") == False

    def test_another_non_whole_number_result(self):
        assert simplify("7/10", "10/2") == False

    def test_simple_whole_number(self):
        assert simplify("1/1", "1/1") == True

    def test_large_numbers_whole(self):
        assert simplify("100/2", "2/100") == True

    def test_large_numbers_non_whole(self):
        assert simplify("100/3", "3/100") == False

    def test_mixed_numbers_whole(self):
        assert simplify("2/1", "1/2") == False

    def test_mixed_numbers_non_whole(self):
        assert simplify("2/3", "3/2") == False

    def test_same_fraction(self):
        assert simplify("1/2", "1/2") == False

    def test_edge_case_1(self):
        assert simplify("1/100", "100/1") == True

    def test_edge_case_2(self):
        assert simplify("1/3", "6/1") == True

    def test_edge_case_3(self):
        assert simplify("2/5", "10/2") == False

    def test_edge_case_4(self):
        assert simplify("3/7", "14/1") == True

    def test_edge_case_5(self):
        assert simplify("4/9", "9/4") == False

    def test_basic_true(self):
        assert simplify("1/5", "5/1") == True

    def test_basic_false(self):
        assert simplify("1/6", "2/1") == False

    def test_another_false(self):
        assert simplify("7/10", "10/2") == False

    def test_whole_numbers(self):
        assert simplify("1/1", "1/1") == True

    def test_large_numbers_true(self):
        assert simplify("100/2", "2/100") == True

    def test_large_numbers_false(self):
        assert simplify("100/3", "3/100") == False

    def test_mixed_numbers_true(self):
        assert simplify("2/3", "3/2") == True

    def test_mixed_numbers_false(self):
        assert simplify("2/5", "5/3") == False

    def test_same_numerator_different_denominator_true(self):
        assert simplify("1/2", "2/1") == True

    def test_same_denominator_different_numerator_false(self):
        assert simplify("1/3", "2/1") == False

    def test_edge_case_1_suite2(self):
        assert simplify("1/1000", "1000/1") == True

    def test_edge_case_2_suite2(self):
        assert simplify("1/999", "999/1") == False

    def test_edge_case_3_suite2(self):
        assert simplify("2/7", "7/2") == True

    def test_edge_case_4_suite2(self):
        assert simplify("3/11", "11/3") == False

    def test_fraction_with_1_as_denominator(self):
        assert simplify("5/1", "1/5") == True

    def test_fraction_with_1_as_numerator(self):
        assert simplify("1/5", "5/1") == True

    def test_complex_true(self):
        assert simplify("3/4", "8/3") == True

    def test_complex_false(self):
        assert simplify("3/4", "7/3") == False