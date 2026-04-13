
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
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))

    product = (num_x * num_n) / (den_x * den_n)

    return product.is_integer()


def test_basic_positive_integers():
    assert simplify("1/5", "5/1") == True
    assert simplify("5/1", "1/5") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("2/1", "1/2") == True

def test_result_is_integer():
    assert simplify("1/2", "2/1") == True
    assert simplify("2/1", "1/2") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("10/2", "2/1") == True

def test_result_is_not_integer():
    assert simplify("1/3", "3/1") == False
    assert simplify("3/1", "1/3") == False
    assert simplify("1/4", "4/1") == False
    assert simplify("2/3", "3/1") == False

def test_larger_numbers():
    assert simplify("10/2", "2/1") == True
    assert simplify("5/1", "1/5") == True
    assert simplify("100/10", "10/1") == True
    assert simplify("10/10", "10/1") == True

def test_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/2", "1/1") == True
    assert simplify("1/1", "2/1") == False
    assert simplify("2/2", "1/1") == True

def test_common_factors():
    assert simplify("4/6", "2/3") == True
    assert simplify("6/4", "3/2") == True
    assert simplify("12/18", "2/3") == True
    assert simplify("18/12", "3/2") == True