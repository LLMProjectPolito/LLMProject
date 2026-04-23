
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

# The function 'simplify' is assumed to be available in the namespace.

@pytest.mark.parametrize("x, n, expected", [
    # --- Provided Examples ---
    ("1/5", "5/1", True),
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),

    # --- Basic Whole Number Results ---
    ("1/1", "1/1", True),
    ("2/1", "3/1", True),
    ("1/2", "2/1", True),
    ("2/3", "3/2", True),
    ("4/5", "5/4", True),
    ("10/1", "1/10", True),
    ("100/1", "1/100", True),

    # --- Basic Non-Whole Number Results ---
    ("1/2", "1/2", False),
    ("2/3", "1/2", False),
    ("3/4", "1/2", False),
    ("1/3", "1/3", False),
    ("1/10", "1/10", False),
    ("2/7", "1/1", False),

    # --- Large Numbers & Precision (The "Blue Team" Killer Tests) ---
    # These tests target implementations that incorrectly use floating-point math.
    # In float64, 1000000000000000001 / 1000000000000000000 is rounded to 1.0.
    # A correct implementation must use integer math to distinguish these.
    ("1000000000000000001/1", "1/1000000000000000000", False),
    ("1/1000000000000000000", "1000000000000000001/1", False),
    ("1000000000000000001/1000000000000000001", "1/1", True),
    
    # Testing extremely large integers that exceed float64 precision limits
    ("100000000000000000000000000000000000001/1", "1/100000000000000000000000000000000000000", False),

    # --- Prime Numbers and Identity ---
    ("1/7", "7/1", True),
    ("1/7", "1/7", False),
    ("7/1", "7/1", True),
    ("7/1", "1/7", True),
    ("13/17", "17/13", True),
    ("13/17", "1/13", False),
])
def test_simplify(x, n, expected):
    """
    Tests the simplify function for correctness across standard, 
    edge, and precision-sensitive cases.
    """
    assert simplify(x, n) == expected