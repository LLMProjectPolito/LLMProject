
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
    
    # Identity cases (product = 1)
    ("1/1", "1/1", True),
    ("2/3", "3/2", True),
    ("5/7", "7/5", True),
    ("100/1", "1/100", True),
    
    # Product is a whole number > 1
    ("1/2", "4/1", True),
    ("2/3", "9/1", True),
    ("3/4", "8/1", True),
    ("10/1", "10/1", True),
    ("2/5", "10/1", True),
    ("1/10", "100/1", True),
    
    # Product is a fraction (not a whole number)
    ("1/2", "1/1", False),
    ("1/3", "1/1", False),
    ("2/3", "1/1", False),
    ("1/2", "3/1", False),
    ("3/4", "2/1", False),
    ("1/10", "1/10", False),
    ("5/6", "5/6", False),
    
    # Large numbers
    ("1000/1", "1/1000", True),
    ("1000/3", "3/1", True),
    ("1000/3", "1/1", False),
    ("123456/789", "789/123456", True),
])
def test_simplify_parameterized(x, n, expected):
    """Tests various fraction combinations using parameterization."""
    assert simplify(x, n) == expected

def test_simplify_basic_true():
    """Explicitly tests basic true scenarios."""
    assert simplify("1/2", "2/1") is True
    assert simplify("1/1", "1/1") is True

def test_simplify_basic_false():
    """Explicitly tests basic false scenarios."""
    assert simplify("1/2", "1/2") is False
    assert simplify("2/1", "1/3") is False

def test_simplify_large_integers():
    """Tests the function with larger integer values to ensure no overflow/precision issues."""
    assert simplify("1000000/1", "1/1000000", True)
    assert simplify("1/1000000", "1/1000000", False)