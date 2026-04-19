
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

@pytest.mark.parametrize("x, n, expected", [
    ("1/5", "5/1", True),
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),
    ("1/1", "1/1", True),
    ("2/1", "2/1", True),
    ("1/2", "1/2", False),
    ("3/4", "8/3", True),
    ("3/4", "4/3", True),
    ("2/3", "3/2", True),
    ("2/3", "1/2", False),
    ("10/1", "10/1", True),
    ("1/100", "100/1", True),
    ("1/100", "50/1", False),
    ("10/3", "3/10", True),
    ("10/3", "1/10", False),
    ("5/2", "4/5", True),
    ("5/2", "2/5", True),
    ("5/2", "1/5", False),
    ("100/7", "7/100", True),
    ("100/7", "14/100", True),
    ("100/7", "1/7", False),
])
def test_simplify(x, n, expected):
    assert simplify(x, n) == expected