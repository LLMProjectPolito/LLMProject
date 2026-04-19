
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
    ("10/3", "3/10", True),
    
    # Non-whole number results
    ("1/3", "1/3", False),
    ("2/3", "1/2", False),
    ("5/2", "3/5", False),
    ("1/100", "10/1", False),
    ("11/7", "1/1", False),
    
    # Edge cases with large numbers
    ("1000/1", "1/1000", True),
    ("1000/1", "1/100", True),
    ("1/1000", "100/1", False),
    ("123456/1", "1/123456", True),
    
    # Cases where product is a whole number > 1
    ("5/2", "4/1", True), # 20/2 = 10
    ("7/3", "6/1", True), # 42/3 = 14
    ("15/4", "2/3", False), # 30/12 = 2.5
])
def test_simplify(x, n, expected):
    assert simplify(x, n) == expected