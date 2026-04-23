
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
import math

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

    def gcd(a, b):
        while(b):
            a, b = b, a % b
        return a

    common_divisor = gcd(result_num, result_den)
    simplified_den = result_den // common_divisor

    return simplified_den == 1


def test_simplify_whole_number():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("4/1", "1/4") == True
    assert simplify("100/2", "2/1") == True
    assert simplify("1000/3", "3/1") == True

def test_simplify_not_whole_number():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "1/3") == False
    assert simplify("100/3", "3/1") == False
    assert simplify("1000/7", "7/1") == False

def test_simplify_numerator_is_one():
    assert simplify("1/2", "4/1") == True
    assert simplify("1/3", "5/2") == False

def test_simplify_denominator_is_one():
    assert simplify("2/1", "3/1") == True
    assert simplify("4/1", "1/2") == True

def test_simplify_large_numbers():
    assert simplify("12345/6789", "6789/12345") == True
    assert simplify("98765/4321", "4321/98765") == True
    assert simplify("1000000/3", "3/1") == True

def test_simplify_zero_numerator():
    assert simplify("0/5", "5/1") == True
    assert simplify("0/2", "1/3") == True

def test_simplify_gcd_greater_than_one():
    assert simplify("4/6", "3/2") == True
    assert simplify("6/4", "2/3") == True
    assert simplify("9/12", "4/3") == True
    assert simplify("12/18", "3/2") == True # GCD is 6

def test_simplify_invalid_format():
    with pytest.raises(ValueError):
        simplify("1.5/2", "2/1")