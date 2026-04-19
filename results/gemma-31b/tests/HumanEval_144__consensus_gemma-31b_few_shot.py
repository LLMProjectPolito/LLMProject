
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
    ("1/2", "4/1", True),
    ("3/4", "8/3", True),
    ("3/4", "1/1", False),
    ("10/1", "1/10", True),
    ("10/1", "2/1", True),
    ("1/3", "1/3", False),
    ("5/2", "4/5", True),
    ("5/2", "2/5", True),
    ("1/100", "100/1", True),
    ("1/100", "50/1", False),
    ("2/3", "3/2", True),
    ("2/3", "9/2", True),
    ("2/3", "5/2", False),
    ("100/1", "100/1", True),
    ("1/1", "1/1", True),
    ("7/3", "3/7", True),
    ("7/3", "6/7", True),
    ("7/3", "1/7", False),
    ("2/1", "2/1", True),
    ("1/2", "1/2", False),
    ("10/3", "3/10", True),
    ("10/3", "1/10", False),
    ("100/1", "1/100", True),
    ("1/100", "1/100", False),
    ("4/5", "5/4", True),
    ("4/5", "10/4", True),
    ("4/5", "5/8", False),
    ("10/2", "1/5", True),
    ("10/2", "1/2", False),
    ("1000/1", "1000/1", True),
    ("1/1000", "1000/1", True),
    ("1/1000", "1/1000", False),
    ("7/3", "9/7", True),
    ("1/3", "3/1", True),
    ("1/3", "6/1", True),
    ("1/3", "9/1", True),
    ("5/7", "14/5", True),
    ("10/3", "3/5", True),
    ("2/3", "1/2", False),
    ("3/4", "1/2", False),
    ("5/6", "1/5", False),
    ("7/8", "4/7", False),
    ("1/1", "2/1", True),
    ("1/1", "1/2", False),
    ("100/200", "2/1", True),
    ("100/200", "3/1", False),
    ("1000/1", "1/1000", True),
    ("1000/3", "3/1000", True),
    ("1000/3", "3/500", True),
    ("1000/3", "3/2000", False),
])
def test_simplify(x, n, expected):
    assert simplify(x, n) == expected

def test_simplify_large_numbers():
    # Testing potential integer overflow or precision issues
    assert simplify("1000000/1", "1/1000000") is True
    assert simplify("1000000/1", "1/1000001") is False
    assert simplify("1000000/3", "3/1000000") is True
    assert simplify("1000000000000/1", "1/1000000000000") is True
    assert simplify("1000000000000/1", "1/1000000000001") is False