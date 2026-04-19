
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
    # Provided examples
    ("1/5", "5/1", True),
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),
    
    # Basic whole number results
    ("1/1", "1/1", True),
    ("2/1", "3/1", True),
    ("1/2", "2/1", True),
    ("1/2", "4/1", True),
    ("3/4", "8/3", True),
    ("5/2", "4/5", True),
    
    # Non-whole number results
    ("1/3", "1/3", False),
    ("2/3", "1/2", False),
    ("1/4", "1/4", False),
    ("3/5", "2/3", False),
    
    # Edge cases with larger numbers
    ("100/1", "1/100", True),
    ("100/3", "3/100", True),
    ("100/3", "6/100", True), # (100/3) * (6/100) = 6/3 = 2
    ("100/3", "1/100", False), # (100/3) * (1/100) = 1/3
    
    # Fractions that result in a whole number but aren't simple reciprocals
    ("10/7", "14/5", True), # (10*14)/(7*5) = 140/35 = 4
    ("11/13", "26/11", True), # (11*26)/(13*11) = 26/13 = 2
    ("11/13", "25/11", False), # (11*25)/(13*11) = 25/13
])
def test_simplify(x, n, expected):
    assert simplify(x, n) == expected