
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
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))

    result_num = x_num * n_num
    result_den = x_den * n_den

    return result_num % result_den == 0

# Pytest Suite
def test_simplify_whole_number():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("4/1", "1/4") == True

def test_simplify_not_whole_number():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "1/3") == False
    assert simplify("2/5", "1/2") == False

def test_simplify_large_numbers():
    assert simplify("100/1", "1/100") == True
    assert simplify("12345/10", "10/12345") == False

def test_simplify_different_denominators():
    assert simplify("2/4", "4/2") == True
    assert simplify("3/6", "6/3") == True
    assert simplify("1/2", "2/4") == True

def test_simplify_edge_cases():
    assert simplify("1/1", "2/1") == True
    assert simplify("2/1", "1/1") == True
    assert simplify("1/2", "1/1") == False
    assert simplify("1/1", "1/2") == False

def test_simplify_complex_fractions():
    assert simplify("15/4", "8/3") == False
    assert simplify("21/5", "5/3") == True
    assert simplify("11/7", "7/11") == True