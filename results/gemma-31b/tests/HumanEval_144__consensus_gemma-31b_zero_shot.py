
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
    ("10/3", "3/10", True),
    ("10/3", "3/5", True),
    ("10/3", "1/5", False),
    ("100/1", "1/100", True),
    ("1/100", "1/100", False),
    ("3/4", "8/1", True),
    ("3/4", "4/3", True),
    ("1/3", "1/3", False),
    ("5/2", "4/5", True),
    ("5/2", "2/5", True),
    ("5/2", "1/5", False),
    ("10/7", "7/10", True),
    ("10/7", "14/10", True),
    ("10/7", "1/7", False),
    ("1000/1", "1/1000", True),
    ("1/1000", "1/1000", False),
    ("2/1", "3/1", True),
    ("1/2", "2/1", True),
    ("1/2", "4/1", True),
    ("2/3", "3/4", False),
    ("1/10", "1/10", False),
    ("3/4", "8/3", True),
    ("7/10", "20/7", True),
    ("5/6", "12/5", True),
    ("2/5", "10/4", True),
    ("9/2", "4/9", True),
    ("2/5", "15/4", False),
    ("3/7", "14/3", True),
    ("3/7", "7/2", False),
    ("1000000/1", "1/1000000", True),
    ("1000000/3", "3/1000000", True),
    ("1234567/1", "1/1234567", True),
    ("11/3", "9/11", True),
    ("11/3", "6/11", True),
    ("11/3", "5/11", False),
    ("10/1", "5/1", True),
    ("3/2", "3/2", False),
    ("5/2", "4/1", True),
    ("100/3", "3/100", True),
    ("2/3", "9/2", True),
    ("11/13", "13/11", True),
    ("4/5", "5/8", False),
    ("1000/1", "1/3", False),
])
def test_simplify(x, n, expected):
    assert simplify(x, n) == expected