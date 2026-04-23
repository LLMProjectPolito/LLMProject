
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

def test_whole_number_result():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("4/6", "3/2") == True

def test_non_whole_number_result():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/3", "2/5") == False

def test_fractions_equal_to_one():
    assert simplify("1/1", "5/1") == True
    assert simplify("2/2", "3/3") == True
    assert simplify("1/1", "1/1") == True

def test_fractions_with_common_factors():
    assert simplify("2/4", "3/6") == True
    assert simplify("4/8", "2/4") == True
    assert simplify("6/9", "3/3") == True

def test_edge_case_numerator_one():
    assert simplify("1/2", "3/4") == False
    assert simplify("1/5", "1/1") == False

def test_edge_case_denominator_one():
    assert simplify("2/1", "3/1") == True
    assert simplify("5/1", "1/1") == True