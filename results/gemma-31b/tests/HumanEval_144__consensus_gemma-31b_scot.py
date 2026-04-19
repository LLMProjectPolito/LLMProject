
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
    
    # Identity and Simple Whole Numbers
    ("1/1", "1/1", True),
    ("2/1", "3/1", True),
    ("1/1", "5/1", True),
    ("1/1", "1/5", False),
    ("10/1", "10/1", True),
    
    # Reciprocals (Product is 1)
    ("2/1", "1/2", True),
    ("4/3", "3/4", True),
    ("10/7", "7/10", True),
    ("100/1", "1/100", True),
    ("10/3", "3/10", True),
    ("11/13", "13/11", True),
    ("123456/789", "789/123456", True),
    
    # Simplification to Integer (Cross-Cancellation)
    ("3/4", "8/1", True),
    ("4/5", "5/2", True),
    ("7/3", "6/1", True),
    ("11/13", "26/11", True),
    ("11/13", "26/22", True),
    ("1/2", "4/1", True),
    ("3/4", "8/3", True),
    ("5/3", "6/5", True),
    ("2/3", "9/2", True),
    ("5/12", "24/5", True),
    ("8/15", "45/4", True),
    ("1/3", "9/1", True),
    ("1/3", "6/1", True),
    ("2/3", "3/2", True),
    ("5/2", "4/5", True),
    
    # Simplification to non-integer
    ("3/4", "2/1", False),
    ("1/3", "1/3", False),
    ("10/3", "1/10", False),
    ("1/100", "1/100", False),
    ("1/2", "1/2", False),
    ("2/5", "1/2", False),
    ("3/7", "7/2", False),
    ("1/10", "1/10", False),
    ("4/5", "1/1", False),
    ("3/2", "5/3", False),
    ("7/3", "2/1", False),
    ("1/100", "50/1", False),
    ("1/3", "2/1", False),
    ("5/2", "1/2", False),
    ("2/3", "1/1", False),
    ("1/1000", "999/1", False),
    
    # Large numbers
    ("1000/1", "1000/1", True),
    ("100/1", "100/1", True),
    ("1/100", "100/1", True),
    ("123456/1", "1/123456", True),
    ("1000000/3", "3/1000000", True),
    ("1/1000", "1000/1", True),
    
    # Edge cases with 1 as numerator or denominator
    ("1/10", "10/1", True),
    ("10/1", "1/10", True),
])
def test_simplify(x, n, expected):
    assert simplify(x, n) == expected