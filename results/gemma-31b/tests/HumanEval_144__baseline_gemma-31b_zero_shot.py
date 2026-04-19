
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
    ("1/2", "4/1", True),
    ("3/4", "8/3", True),
    ("5/2", "2/5", True),
    
    # Non-whole number results
    ("1/3", "1/3", False),
    ("2/3", "1/2", False),
    ("1/4", "1/4", False),
    ("10/3", "1/10", False),
    
    # Complex fractions resulting in whole numbers
    ("10/3", "6/10", True),   # (10*6)/(3*10) = 60/30 = 2
    ("15/4", "8/5", True),    # (15*8)/(4*5) = 120/20 = 6
    ("100/7", "7/100", True), # 1
    ("100/7", "14/100", True),# (100*14)/(7*100) = 14/7 = 2
    
    # Complex fractions resulting in non-whole numbers
    ("15/4", "2/5", False),   # (15*2)/(4*5) = 30/20 = 1.5
    ("100/7", "1/100", False),# 1/7
    
    # Edge cases: Large numbers
    ("1000000/1", "1/1000000", True),
    ("1000000/3", "3/1000000", True),
    ("1000000/3", "1/1000000", False),
])
def test_simplify(x, n, expected):
    assert simplify(x, n) == expected