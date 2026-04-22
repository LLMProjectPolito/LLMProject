
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
    def fraction_to_float(fraction):
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
        ("1/1", "1/1", True),
        ("1/100", "100/1", True),
        ("100/1", "1/100", True),
        ("1/2", "1", True),
        ("1", "1/2", True),
    ],
)
def test_simplify_basic(x, n, expected):
    assert simplify(x, n) == expected


@pytest.mark.parametrize(
    "x, n, expected",
    [
        ("2/5", "5/2", True),
        ("4/7", "7/4", True),
        ("11/3", "3/11", True),
        ("100/3", "3/100", True),
    ],
    ids=["test_simplify_more_fractions"],
)
def test_simplify_more_fractions(x, n, expected):
    assert simplify(x, n) == expected


@pytest.mark.parametrize(
    "x, n, expected",
    [
        ("1/10", "10/1", True),
        ("10/1", "1/10", True),
    ],
    ids=["test_simplify_large_numbers"],
)
def test_simplify_large_numbers(x, n, expected):
    assert simplify(x, n) == expected

@pytest.mark.parametrize(
    "x, n, expected",
    [
        ("1/1", "1/1", True),
    ],
    ids=["test_simplify_unit_fractions"],
)
def test_simplify_unit_fractions(x, n, expected):
    assert simplify(x, n) == expected

@pytest.mark.parametrize(
    "x, n, expected",
    [
        ("1/2", "1/2", True),
    ],
    ids=["test_simplify_equal_fractions"],
)
def test_simplify_equal_fractions(x, n, expected):
    assert simplify(x, n) == expected

@pytest.mark.parametrize(
    "x, n, expected",
    [
        ("1/2", "1", True),
        ("1", "1/2", True),
    ],
    ids=["test_simplify_fraction_and_integer"],
)
def test_simplify_fraction_and_integer(x, n, expected):
    assert simplify(x, n) == expected

@pytest.mark.parametrize(
    "x, n, expected",
    [
        ("1/100", "100/1", True),
        ("100/1", "1/100", True),
    ],
    ids=["test_simplify_large_denominator"],
)
def test_simplify_large_denominator(x, n, expected):
    assert simplify(x, n) == expected

@pytest.mark.parametrize(
    "x, n, expected",
    [
        ("1/1", "1/1", True),
    ],
    ids=["test_simplify_one_over_one"],
)
def test_simplify_one_over_one(x, n, expected):
    assert simplify(x, n) == expected