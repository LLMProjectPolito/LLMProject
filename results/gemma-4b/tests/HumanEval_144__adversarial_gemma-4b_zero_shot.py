
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

# Tests (Pytest):
def test_simplify_valid():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "6/1") == True
    assert simplify("10/2", "2/1") == True
    assert simplify("1/1", "1/1") == True

def test_simplify_invalid():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "3/1") == False
    assert simplify("5/4", "2/1") == False

def test_simplify_large_numbers():
    assert simplify("100/10", "10/1") == True
    assert simplify("100/10", "11/1") == False

def test_simplify_equal_fractions():
    assert simplify("1/2", "1/2") == True
    assert simplify("5/7", "5/7") == True

def test_simplify_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        simplify("1/0", "5/1")
    with pytest.raises(ZeroDivisionError):
        simplify("1/5", "0/1")