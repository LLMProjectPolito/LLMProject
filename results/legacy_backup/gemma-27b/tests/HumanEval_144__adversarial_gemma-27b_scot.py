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

    product_num = x_num * n_num
    product_den = x_den * n_den

    return product_den == 1


def test_simplify_whole_number():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("4/1", "1/4") == True
    assert simplify("1/1", "1/1") == True

def test_simplify_not_whole_number():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "1/3") == False
    assert simplify("2/5", "1/2") == False

def test_simplify_one_as_numerator():
    assert simplify("1/2", "2/1") == True
    assert simplify("1/3", "3/4") == False
    assert simplify("1/1", "1/2") == False

def test_simplify_one_as_denominator():
    assert simplify("2/1", "1/2") == True
    assert simplify("3/1", "1/4") == False
    assert simplify("1/2", "2/1") == True

def test_simplify_fractions_that_simplify_before_multiplication():
    assert simplify("2/4", "4/2") == True
    assert simplify("3/6", "6/3") == True
    assert simplify("4/8", "2/1") == True

def test_simplify_large_numbers():
    assert simplify("100/20", "2/1") == True
    assert simplify("1000/50", "5/10") == True
    assert simplify("100/3", "1/2") == False

def test_simplify_equal_fractions():
    assert simplify("2/2", "2/2") == True
    assert simplify("5/5", "5/5") == True
    assert simplify("10/10", "10/10") == True