
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

    product_num = num_x * num_n
    product_den = den_x * den_n

    if product_num % product_den == 0:
        return True
    else:
        return False

def test_simplify_positive_whole_numbers():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "6/1") == True
    assert simplify("4/7", "14/1") == False

def test_simplify_with_larger_numbers():
    assert simplify("10/2", "2/1") == True
    assert simplify("12/3", "3/1") == True
    assert simplify("15/4", "4/1") == False

def test_simplify_with_different_denominators():
    assert simplify("1/2", "2/3") == False
    assert simplify("3/4", "4/5") == False
    assert simplify("5/6", "6/7") == False

def test_simplify_with_equal_denominators():
    assert simplify("1/2", "2/2") == False
    assert simplify("3/4", "4/4") == False

def test_simplify_with_one_as_numerator():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "6/1") == True
    assert simplify("1/7", "7/1") == True

def test_simplify_with_one_as_denominator():
    assert simplify("5/1", "1/5") == True
    assert simplify("6/1", "1/6") == True
    assert simplify("7/1", "1/7") == True

def test_simplify_with_complex_fractions():
    assert simplify("12/18", "18/3") == True
    assert simplify("24/36", "36/3") == True
    assert simplify("30/45", "45/3") == True
    assert simplify("12/18", "18/6") == False

def test_simplify_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/1", "1/2") == True
    assert simplify("1/2", "1/2") == False
    assert simplify("0/1", "1/1") == True
    assert simplify("1/0", "1/1") == False
    assert simplify("1/1", "0/1") == False