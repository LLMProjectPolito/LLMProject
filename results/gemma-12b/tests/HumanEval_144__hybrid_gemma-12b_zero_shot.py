
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
    """
    Pytest class for testing the simplify function.
    """

    def test_whole_number_result(self):
        """Test cases where the result is a whole number."""
        assert simplify("1/5", "5/1") == True
        assert simplify("2/3", "3/2") == True
        assert simplify("1/1", "1/1") == True
        assert simplify("4/2", "2/4") == True
        assert simplify("1/2", "2/1") == True
        assert simplify("3/7", "7/3") == True
        assert simplify("1/10", "10/1") == True
        assert simplify("1/11", "11/1") == True
        assert simplify("1/12", "12/1") == True
        assert simplify("1/13", "13/1") == True
        assert simplify("1/14", "14/1") == True
        assert simplify("1/15", "15/1") == True

    def test_non_whole_number_result(self):
        """Test cases where the result is not a whole number."""
        assert simplify("1/6", "2/1") == False
        assert simplify("7/10", "10/2") == False
        assert simplify("1/3", "2/1") == False
        assert simplify("1/4", "3/1") == False
        assert simplify("2/5", "3/4") == False
        assert simplify("1/7", "2/3") == False
        assert simplify("1/8", "3/5") == False
        assert simplify("1/9", "2/7") == False
        assert simplify("1/10", "3/2") == False
        assert simplify("1/11", "4/3") == False
        assert simplify("1/12", "5/2") == False
        assert simplify("1/13", "6/5") == False
        assert simplify("1/14", "7/3") == False
        assert simplify("1/15", "8/5") == False

    def test_large_numbers(self):
        """Test cases with larger numbers to ensure no overflow issues."""
        assert simplify("100/2", "2/100") == True
        assert simplify("1000/10", "10/1000") == True
        assert simplify("1000000/1000", "1000/1000000") == True
        assert simplify("100/3", "3/100") == False

    def test_edge_cases(self):
        """Test edge cases like 1/1 and 1/2."""
        assert simplify("1/1", "1/1") == True
        assert simplify("1/2", "2/1") == True
        assert simplify("2/1", "1/2") == False

    def test_different_denominators(self):
        """Test cases with different denominators."""
        assert simplify("1/2", "1/3") == False
        assert simplify("1/3", "1/2") == False
        assert simplify("2/3", "1/4") == False
        assert simplify("3/4", "2/3") == False

    def test_same_numerator_different_denominator(self):
        """Test cases with same numerator but different denominators."""
        assert simplify("1/2", "1/3") == False
        assert simplify("2/3", "2/5") == False

    def test_same_denominator_different_numerator(self):
        """Test cases with same denominator but different numerators."""
        assert simplify("1/2", "3/2") == False
        assert simplify("2/3", "4/3") == False

    def test_fraction_simplification(self):
        """Test cases where the fractions simplify to whole numbers after multiplication."""
        assert simplify("2/4", "2/1") == True
        assert simplify("3/6", "2/1") == True
        assert simplify("4/8", "1/1") == True
        assert simplify("5/10", "2/1") == True
        assert simplify("6/12", "1/1") == True
        assert simplify("7/14", "2/1") == True
        assert simplify("8/16", "1/1") == True
        assert simplify("9/18", "2/1") == True
        assert simplify("10/20", "1/1") == True
        assert simplify("11/22", "2/1") == True
        assert simplify("12/24", "1/1") == True
        assert simplify("13/26", "2/1") == True
        assert simplify("14/28", "1/1") == True
        assert simplify("15/30", "2/1") == True