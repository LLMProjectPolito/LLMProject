
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
from sympy import Rational

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
    def fraction_to_rational(fraction_str):
        num, den = map(int, fraction_str.split('/'))
        return Rational(num, den)

    x_rational = fraction_to_rational(x)
    n_rational = fraction_to_rational(n)
    product = x_rational * n_rational
    return product.is_integer


@pytest.mark.parametrize(
    "x, n, expected",
    [
        ("1/5", "5/1", True),
        ("1/6", "2/1", False),
        ("7/10", "10/2", False),
        ("1/2", "2/1", True),
        ("3/4", "4/3", True),
        ("5/7", "7/5", True),
        ("2/3", "3/2", True),
        ("1/3", "1/3", True),
        ("1/4", "1/2", False),
        ("2/5", "3/7", False),
        ("1/1", "1/1", True),
        ("1/1", "2/1", False),
        ("2/1", "1/1", True),
        ("1/2", "1/4", False),
        ("4/6", "6/4", True),  # Simplification case
        ("10/20", "20/10", True), # Simplification case
        ("1/100", "100/1", True), #Large numbers
        ("1/100", "101/1", False), #Large numbers
        ("101/100", "1/1", False),
        ("1/1000", "1000/1", True),
        ("1/1000", "1001/1", False),
        ("1001/1000", "1/1", False),
        ("1/2", "1/2", True),
        ("1/3", "2/3", True),
        ("1/4", "3/4", True),
        ("1/5", "4/5", True),
        ("2/3", "4/5", False),

    ],
)
def test_simplify_basic(x, n, expected):
    assert simplify(x, n) == expected


@pytest.mark.parametrize(
    "x, n, expected",
    [
        ("1/5", "5/1", True),
        ("1/6", "2/1", False),
        ("7/10", "10/2", False),
        ("1/2", "2/1", True),
    ],
)
def test_simplify_examples(x, n, expected):
    assert simplify(x, n) == expected


@pytest.mark.parametrize(
    "x, n, expected",
    [
        ("1/1", "1/1", True),
        ("1/1", "2/1", False),
        ("2/1", "1/1", True),
    ],
)
def test_simplify_unity(x, n, expected):
    assert simplify(x, n) == expected

@pytest.mark.parametrize(
    "x, n, expected",
    [
         ("1/1", "1/2", False),
         ("1/2", "1/1", False)
    ]
)
def test_simplify_denominator_one(x,n,expected):
    assert simplify(x,n) == expected

@pytest.mark.parametrize(
    "x, n, expected",
    [
        ("2/3", "4/6", True)
    ]
)
def test_simplify_simplification(x,n,expected):
    assert simplify(x,n) == expected