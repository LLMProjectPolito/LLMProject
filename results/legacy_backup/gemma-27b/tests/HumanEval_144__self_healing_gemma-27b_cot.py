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

def test_simplify_larger_numbers():
    assert simplify("10/25", "5/1") == True
    assert simplify("12/15", "5/1") == False
    assert simplify("100/20", "5/1") == True
    assert simplify("100/21", "21/1") == False

def test_simplify_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/2", "1/1") == False
    assert simplify("2/1", "1/1") == True
    assert simplify("1/100", "100/1") == True
    assert simplify("100/1", "1/100") == True

def test_simplify_different_denominators():
    assert simplify("2/3", "4/6") == True
    assert simplify("1/2", "3/6") == True
    assert simplify("4/5", "8/10") == True
    assert simplify("1/4", "1/2") == False
    assert simplify("2/5", "4/10") == True