
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
    def test_simplify_true(self):
        assert simplify("1/5", "5/1") == True
        assert simplify("2/2", "1/1") == True
        assert simplify("1/1", "1/1") == True
        assert simplify("4/2", "2/2") == True
        assert simplify("1/3", "3/1") == True
        assert simplify("2/4", "2/1") == True
        assert simplify("1/2", "2/2") == True

    def test_simplify_false(self):
        assert simplify("1/6", "2/1") == False
        assert simplify("7/10", "10/2") == False
        assert simplify("1/4", "1/2") == False
        assert simplify("1/5", "2/1") == False
        assert simplify("3/4", "1/2") == False
        assert simplify("1/7", "2/1") == False
        assert simplify("2/3", "1/2") == False

    def test_simplify_edge_cases(self):
        assert simplify("1/100", "100/1") == True
        assert simplify("1/101", "101/1") == True
        assert simplify("1/100", "1/2") == False
        assert simplify("100/1", "1/100") == False

    def test_simplify_large_numbers(self):
        assert simplify("1000/1000", "2000/2000") == True
        assert simplify("1000/1", "1/1000") == False

    def test_simplify_mixed_numbers(self):
        # While the problem states fractions are in the form numerator/denominator,
        # it's good to test if the function handles mixed numbers gracefully.
        # The current implementation doesn't explicitly handle mixed numbers,
        # but it should still work correctly if they are converted to improper fractions.
        assert simplify("1 1/2", "2/1") == False # This will fail with the current implementation
        assert simplify("1/2", "1 1/2") == False # This will fail with the current implementation

    def test_simplify_with_same_numerator_different_denominator(self):
        assert simplify("2/3", "4/3") == False
        assert simplify("4/3", "2/3") == False

    def test_simplify_with_different_numerator_same_denominator(self):
        assert simplify("2/5", "3/5") == False
        assert simplify("3/5", "2/5") == False