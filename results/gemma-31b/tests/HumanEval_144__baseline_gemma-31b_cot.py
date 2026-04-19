
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
    ("1/2", "2/1", True),   # 1/1 = 1
    ("1/2", "4/1", True),   # 4/2 = 2
    ("2/3", "6/1", True),   # 12/3 = 4
    ("3/4", "8/3", True),   # 24/12 = 2
    ("5/2", "4/5", True),   # 20/10 = 2
    
    # Basic non-whole number results
    ("1/3", "1/3", False),  # 1/9
    ("2/3", "3/4", False),  # 6/12 = 0.5
    ("1/10", "1/10", False),# 1/100
    ("3/5", "2/3", False),  # 6/15 = 0.4
    
    # Edge cases: Denominators of 1
    ("1/1", "1/1", True),   # 1/1 = 1
    ("2/1", "3/1", True),   # 6/1 = 6
    ("5/1", "1/1", True),   # 5/1 = 5
    
    # Edge cases: Large numbers
    ("1000000/1", "1/1000000", True), # 1/1 = 1
    ("1000000/1", "1/1", True),       # 1000000/1 = 1000000
    ("1/1000000", "1/1000000", False),# 1/10^12
    
    # Case where numerator is larger than denominator
    ("10/3", "3/10", True), # 30/30 = 1
    ("10/3", "1/1", False), # 10/3 = 3.33...
    ("10/3", "6/1", True),  # 60/3 = 20
])
def test_simplify(x, n, expected):
    """
    Tests the simplify function with various fractions to ensure it correctly
    identifies if the product of two fractions is a whole number.
    """
    assert simplify(x, n) == expected