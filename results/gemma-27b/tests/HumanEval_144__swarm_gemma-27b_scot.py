
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

def test_simplify_edge_case_common_denominator_factor():
    assert simplify("1/2", "2/4") == False

def test_simplify_common_denominator_factor():
    assert simplify("2/4", "4/2") == True

def test_simplify_large_numbers_with_common_factor():
    assert simplify("1000/4", "4/1") == True