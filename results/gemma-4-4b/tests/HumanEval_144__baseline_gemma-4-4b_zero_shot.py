
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
from typing import Tuple

def simplify(x: str, n: str) -> bool:
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    def fraction_to_float(fraction: str) -> float:
        numerator, denominator = map(int, fraction.split('/'))
        return numerator / denominator

    x_float = fraction_to_float(x)
    n_float = fraction_to_float(n)
    product = x_float * n_float
    return product.is_integer()

@pytest.mark.parametrize(
    "x, n, expected",
    [
        ("1/5", "5/1", True),
        ("1/6", "2/1", False),
        ("7/10", "10/2", False),
        ("1/2", "2/1", True),
        ("3/4", "4/3", True),
        ("2/3", "3/2", True),
        ("5/7", "7/5", True),
        ("1/3", "1/3", True),
        ("1/4", "2/4", False),
        ("1/1", "1/1", True),
        ("2/1", "1/2", True),
        ("1/2", "1/2", True),
        ("1/10", "10/1", True),
        ("10/1", "1/10", True),
        ("1/100", "100/1", True),
        ("100/1", "1/100", True),
        ("1/101", "101/1", True),
        ("101/1", "1/101", True),
        ("1/2", "3/4", False),
        ("2/5", "1/2", False),
        ("1/3", "1/4", False),
        ("1/5", "1/6", False),
        ("1/7", "1/8", False),
        ("1/9", "1/10", False),
    ],
)
def test_simplify_basic(x: str, n: str, expected: bool):
    assert simplify(x, n) == expected

@pytest.mark.parametrize(
    "x, n, expected",
    [
        ("1/1", "1/1", True),
        ("2/2", "2/2", True),
        ("3/3", "3/3", True),
        ("4/4", "4/4", True),
        ("5/5", "5/5", True),
        ("1/2", "1/2", True),
        ("2/1", "2/1", True),
        ("1/3", "3/1", True),
        ("1/4", "4/1", True),
        ("1/5", "5/1", True),
    ],
)
def test_simplify_equal_fractions(x: str, n: str, expected: bool):
    assert simplify(x, n) == expected

@pytest.mark.parametrize(
    "x, n, expected",
    [
        ("1/2", "2/3", False),
        ("3/4", "5/6", False),
        ("7/8", "9/10", False),
        ("11/12", "13/14", False),
    ],
)
def test_simplify_unequal_fractions(x: str, n: str, expected: bool):
    assert simplify(x, n) == expected