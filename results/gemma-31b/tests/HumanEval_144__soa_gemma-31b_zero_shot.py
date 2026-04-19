
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
    ("3/4", "4/3", True),
    
    # Basic non-whole number results
    ("1/2", "1/2", False),
    ("1/3", "1/3", False),
    ("2/3", "1/1", False),
    ("1/4", "2/1", False),
    
    # Complex fractions resulting in whole numbers
    ("3/4", "8/3", True),
    ("10/3", "3/10", True),
    ("5/2", "4/5", True),
    ("7/3", "6/7", True),
    ("12/5", "25/12", True),
    
    # Complex fractions resulting in non-whole numbers
    ("10/3", "1/10", False),
    ("5/2", "1/5", False),
    ("7/3", "1/7", False),
    ("12/5", "5/12", True), # This is 1, so True
    ("12/5", "1/12", False),
    
    # Large numbers
    ("100/1", "1/100", True),
    ("1000/3", "3/1000", True),
    ("1000/3", "1/1000", False),
    ("1000000/1", "1/1000000", True),
    
    # Cases where numerator/denominator are large but result is whole
    ("100/7", "7/1", True),
    ("1/100", "100/1", True),
    ("1/100", "200/1", True),
    ("1/100", "150/1", False),
])
def test_simplify(x, n, expected):
    assert simplify(x, n) == expected