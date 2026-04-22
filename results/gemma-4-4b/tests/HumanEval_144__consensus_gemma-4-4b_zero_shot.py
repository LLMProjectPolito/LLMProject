
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

def test_simplify_positive_whole_number():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("3/4", "4/3") == True

def test_simplify_large_numbers():
    assert simplify("1000/100", "100/1") == True
    assert simplify("100/100", "100/1") == True
    assert simplify("12345/67890", "67890/12345") == True

def test_simplify_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("2/1", "1/2") == True

def test_simplify_same_numerator_denominator():
    assert simplify("1/1", "1/1") == True
    assert simplify("5/5", "5/5") == True
    assert simplify("10/10", "10/10") == True

def test_simplify_valid_fractions():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("3/4", "4/3") == True
    assert simplify("5/7", "7/5") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("4/6", "6/4") == True

def test_simplify_invalid_fractions():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("2/5", "1/2") == False
    assert simplify("3/7", "4/8") == False
    assert simplify("5/9", "6/10") == False
    assert simplify("1/4", "2/3") == False
    assert simplify("1/2", "3/4") == False
    assert simplify("1/3", "4/5") == False