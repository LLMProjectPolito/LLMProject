
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
    ("1/2", "2/1", True),
    ("2/3", "3/2", True),
    ("2/3", "6/1", True),
    ("1/3", "1/3", False),
    ("10/1", "1/10", True),
    ("10/1", "1/5", True),
    ("1/10", "5/1", False),
    ("3/4", "8/3", True),
    ("3/4", "4/3", True),
    ("3/4", "1/3", False),
    ("100/1", "1/100", True),
    ("1/100", "1/100", False),
    ("1/1", "1/1", True),
    ("5/2", "4/5", True),
    ("5/2", "2/5", True),
    ("11/13", "13/11", True),
    ("11/13", "26/11", True),
    ("11/13", "1/11", False),
])
def test_simplify(x, n, expected):
    assert simplify(x, n) == expected