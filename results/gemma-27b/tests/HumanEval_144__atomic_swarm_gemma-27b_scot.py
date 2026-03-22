import pytest
import math

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
    result = (x_num * n_num) / (x_den * n_den)
    return result == int(result)

def test_basic():
    assert simplify("1/5", "5/1") == True

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
    result = (x_num * n_num) / (x_den * n_den)
    return result == int(result)

def test_edge():
    """Test case with fractions that result in a whole number."""
    assert simplify("1/1", "1/1") == True
    assert simplify("2/1", "1/2") == True
    assert simplify("1/5", "5/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("3/4", "4/3") == True
    assert simplify("1/10", "10/1") == True

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
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))

    result_num = x_num * n_num
    result_den = x_den * n_den

    common_divisor = gcd(result_num, result_den)
    simplified_num = result_num // common_divisor
    simplified_den = result_den // common_divisor

    return simplified_den == 1

@pytest.mark.parametrize("x, n, expected", [
    ("1/2", "2/1", True),
    ("1/3", "3/1", True),
    ("1/4", "4/1", True),
    ("1/5", "5/1", True),
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),
    ("2/3", "3/2", False),
    ("4/5", "5/4", True),
    ("1/1", "1/1", True),
    ("2/1", "1/2", True),
    ("3/1", "1/3", True),
    ("1/7", "7/1", True),
    ("5/2", "2/5", True),
    ("10/3", "3/10", True),
    ("1/100", "100/1", True),
    ("100/1", "1/100", True),
    ("1/2", "1/2", False),
    ("1/3", "1/3", False),
    ("2/4", "4/2", True),
])
def test_simplify(x, n, expected):
    assert simplify(x, n) == expected