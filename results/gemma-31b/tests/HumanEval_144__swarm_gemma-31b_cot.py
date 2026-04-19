
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
import math

def test_simplify_non_integer_fractions_product_is_integer():
    # Tests a case where neither x nor n are whole numbers, but their product is.
    # (3/4) * (8/3) = 24/12 = 2
    assert simplify("3/4", "8/3") is True

def test_simplify_float_precision():
    # This test case checks if the function avoids floating-point precision errors.
    # (1/3) * 30000000000000001 is mathematically 10000000000000000.333...,
    # but float multiplication in Python often evaluates it as 10000000000000000.0.
    assert simplify("1/3", "30000000000000001/1") is False

def test_simplify_large_numbers_whole_result():
    # Tests potential float precision issues and results that are whole numbers > 1
    # (1000000000/7) * (14/1000000000) = 14/7 = 2
    assert simplify("1000000000/7", "14/1000000000") is True