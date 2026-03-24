
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

def test_simplify_both_whole():
    assert simplify("1/1", "1/1") == True

def test_simplify_large_numbers_whole():
    assert simplify("100/2", "2/1") == True

def test_simplify_large_numbers_not_whole():
    assert simplify("100/3", "2/1") == False

def test_simplify_same_fraction():
    assert simplify("1/2", "1/2") == True

def test_simplify_different_denominators_whole():
    assert simplify("3/4", "4/3") == True

def test_simplify_different_denominators_not_whole():
    assert simplify("3/5", "2/7") == False

def test_simplify_numerator_one():
    assert simplify("1/7", "14/1") == True

def test_simplify_denominator_one():
    assert simplify("5/1", "1/1") == True

def test_simplify_complex_fractions_whole():
    assert simplify("2/3", "6/1") == True

def test_simplify_complex_fractions_not_whole():
    assert simplify("2/3", "5/1") == False

def test_simplify_edge_case_1():
    assert simplify("1/2", "3/2") == False

def test_simplify_edge_case_2():
    assert simplify("1/3", "4/3") == False

def test_simplify_edge_case_3():
    assert simplify("1/4", "5/4") == False

def test_simplify_edge_case_4():
    assert simplify("1/5", "6/5") == False