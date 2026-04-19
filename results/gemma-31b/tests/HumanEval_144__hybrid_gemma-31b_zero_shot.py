
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

def simplify(x, n):
    """
    Simplifies the expression x * n and returns True if the result is a whole number.
    """
    # Split the strings to get numerators and denominators
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    
    # Calculate resulting numerator and denominator of the product
    res_num = x_num * n_num
    res_den = x_den * n_den
    
    # A fraction is a whole number if the numerator is divisible by the denominator
    return res_num % res_den == 0

@pytest.mark.parametrize("x, n, expected", [
    # --- Docstring / Problem Description Examples ---
    ("1/5", "5/1", True),
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),
    
    # --- Identity and Simple Whole Numbers ---
    ("1/1", "1/1", True),
    ("2/1", "3/1", True),
    ("1/1", "4/1", True),
    ("5/1", "1/1", True),
    ("1/5", "1/1", False),
    
    # --- Reciprocals (Inverse) ---
    ("1/2", "2/1", True),
    ("3/4", "4/3", True),
    ("7/8", "8/7", True),
    ("123/456", "456/123", True),
    
    # --- Products resulting in whole numbers > 1 ---
    ("2/3", "6/1", True),     # 12/3 = 4
    ("5/2", "4/5", True),     # 20/10 = 2
    ("10/3", "3/2", True),    # 30/6 = 5
    ("1/10", "100/1", True),  # 100/10 = 10
    ("3/2", "4/3", True),     # 12/6 = 2
    ("7/3", "9/7", True),     # 63/21 = 3
    ("10/3", "6/5", True),    # 60/15 = 4
    ("5/2", "4/1", True),     # 20/2 = 10
    ("15/4", "8/5", True),    # 120/20 = 6
    ("11/7", "14/11", True),  # 154/77 = 2
    
    # --- Products resulting in non-whole numbers ---
    ("1/2", "1/2", False),    # 1/4
    ("3/4", "1/2", False),    # 3/8
    ("2/3", "1/3", False),    # 2/9
    ("7/8", "7/8", False),    # 49/64
    ("1/3", "1/3", False),    # 1/9
    ("1/10", "5/1", False),   # 5/10 = 0.5
    ("2/3", "2/3", False),    # 4/9
    ("100/1", "1/200", False),# 100/200 = 0.5
    ("15/4", "2/5", False),   # 30/20 = 1.5
    ("2/3", "3/4", False),    # 6/12 = 0.5
    
    # --- Unsimplified Input Fractions ---
    ("2/4", "2/1", True),     # (1/2) * 2 = 1
    ("2/4", "1/1", False),    # (1/2) * 1 = 0.5
    ("10/20", "20/10", True), # (1/2) * 2 = 1
    ("10/20", "10/20", False),# (1/2) * (1/2) = 1/4
    ("50/10", "20/10", True), # 5 * 2 = 10
    
    # --- Large Numbers (Precision/Integer Overflow Checks) ---
    ("1000/1", "1/1000", True),
    ("1000/1", "1/2000", False),
    ("123456/1", "1/123456", True),
    ("1000000/1", "1/1000000", True),
    ("1000000/1", "1/2000000", False),
    ("999999/1", "1/999999", True),
])
def test_simplify_parametrized(x, n, expected):
    """Comprehensive test suite for the simplify function covering various edge cases."""
    assert simplify(x, n) == expected

def test_simplify_extreme_large_product():
    """Test specifically for very large products to ensure Python's arbitrary precision integers handle it."""
    x = "1000000/1"
    n = "1000000/1"
    assert simplify(x, n) is True

def test_simplify_minimal_fraction():
    """Test with the smallest possible positive whole number fractions."""
    assert simplify("1/1", "1/1") is True