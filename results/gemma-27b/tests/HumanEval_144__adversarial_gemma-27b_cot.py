
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

def test_simplify_valid_fractions_whole_number():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/1") == True
    assert simplify("4/7", "7/1") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("5/2", "2/1") == True

def test_simplify_valid_fractions_not_whole_number():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/3", "2/1") == False
    assert simplify("2/5", "3/1") == False
    assert simplify("3/4", "5/1") == False

def test_simplify_fractions_with_common_factors():
    assert simplify("2/4", "4/1") == True
    assert simplify("3/6", "2/1") == True
    assert simplify("4/8", "2/1") == True
    assert simplify("6/9", "3/1") == True

def test_simplify_large_numbers():
    assert simplify("100/25", "5/1") == True
    assert simplify("1000/8", "125/1") == True
    assert simplify("1234/2", "617/1") == True

def test_simplify_fractions_with_same_numerator():
    assert simplify("5/2", "5/1") == False
    assert simplify("10/3", "10/1") == False

def test_simplify_fractions_with_same_denominator():
    assert simplify("2/5", "3/5") == False
    assert simplify("7/10", "1/10") == False

def test_simplify_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/2", "1/1") == False
    assert simplify("2/1", "1/2") == False