
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
from your_module import simplify  # Replace your_module

def test_simplify_whole_number():
    assert simplify("1/5", "5/1") == True

def test_simplify_not_whole_number():
    assert simplify("1/6", "2/1") == False

def test_simplify_another_not_whole_number():
    assert simplify("7/10", "10/2") == False

def test_simplify_one_whole():
    assert simplify("1/1", "2/3") == True

def test_simplify_other_whole():
    assert simplify("3/1", "1/1") == True

def test_simplify_both_whole():
    assert simplify("1/1", "1/1") == True

def test_simplify_large_numbers_whole():
    assert simplify("100/1", "1/100") == True

def test_simplify_large_numbers_not_whole():
    assert simplify("100/3", "3/100") == False

def test_simplify_same_numerator_denominator():
    assert simplify("1/1", "2/2") == True

def test_simplify_complex_fraction():
    assert simplify("2/3", "3/4") == False

def test_simplify_another_complex_fraction():
    assert simplify("1/2", "4/5") == False

def test_simplify_fraction_with_larger_denominator():
    assert simplify("1/1000", "1000/1") == True

def test_simplify_fraction_with_larger_numerator():
    assert simplify("1000/1", "1/1000") == True

def test_simplify_fraction_with_same_numerator():
    assert simplify("2/3", "4/6") == True

def test_simplify_fraction_with_same_denominator():
    assert simplify("2/4", "4/2") == False

def test_simplify_fraction_with_one_as_numerator():
    assert simplify("1/2", "2/1") == False

def test_simplify_fraction_with_one_as_denominator():
    assert simplify("2/1", "1/2") == False

def test_simplify_fraction_with_zero_numerator():
    assert simplify("0/1", "1/1") == True

def test_simplify_fraction_with_decimal_result():
    assert simplify("1/3", "2/1") == False