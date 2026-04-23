
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
# Replace 'your_module' with the actual name of your file
from your_module import simplify 

@pytest.mark.parametrize("x, n, expected", [
    # --- Group 1: Problem Statement Examples ---
    ("1/5", "5/1", True),
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),

    # --- Group 2: Identity & Reciprocals (Product = 1) ---
    ("1/1", "1/1", True),
    ("2/3", "3/2", True),
    ("123/456", "456/123", True),
    ("1000/1", "1/1000", True),

    # --- Group 3: Whole Number Products (> 1) ---
    ("2/1", "3/1", True),    # 6
    ("3/2", "4/1", True),    # 6
    ("1/3", "9/1", True),    # 3
    ("10/3", "3/1", True),   # 10
    ("5/2", "4/5", True),    # 2
    ("1/2", "4/1", True),    # 2
    ("3/4", "8/3", True),    # 2
    ("12/5", "5/4", True),   # 3
    ("5/7", "14/5", True),   # 2
    ("3/11", "22/3", True),  # 2
    ("10/1", "5/1", True),   # 50

    # --- Group 4: Non-Whole Number Products (< 1 or Decimals) ---
    ("1/2", "1/2", False),   # 1/4
    ("2/3", "2/3", False),   # 4/9
    ("3/4", "1/2", False),   # 3/8
    ("1/10", "1/10", False), # 1/100
    ("5/6", "5/6", False),   # 25/36
    ("3/2", "3/2", False),   # 2.25
    ("5/3", "2/1", False),   # 3.33...
    ("10/7", "1/1", False),  # 1.42...
    ("1/3", "1/3", False),   # 1/9
    ("2/5", "1/2", False),   # 0.2
    ("5/2", "1/2", False),   # 1.25
    ("9/7", "7/2", False),   # 4.5

    # --- Group 5: Large Number Boundaries ---
    ("1000000/1", "1/1", True),
    ("1/1000000", "1/1", False),
    ("999999/1000000", "1000000/1", True),
    ("123456/789", "789/123456", True),
])
def test_simplify_parametrized(x, n, expected):
    """Tests a vast range of fraction combinations categorized by mathematical outcome."""
    assert simplify(x, n) == expected


def test_simplify_reciprocal_property():
    """
    Property-based test: Ensures that any valid fraction multiplied 
    by its reciprocal always returns True.
    """
    test_fractions = ["1/2", "3/4", "10/3", "123/456", "1/1000", "99/100"]
    for f in test_fractions:
        num, den = f.split('/')
        reciprocal = f"{den}/{num}"
        assert simplify(f, reciprocal) is True, f"Failed reciprocal property for {f}"


def test_simplify_large_prime_precision():
    """
    Stress test: Uses large prime numbers to ensure the implementation 
    doesn't fall victim to floating-point precision errors.
    """
    # (10^9 + 7) is a prime number. 
    # If the function uses floats, (1/prime) * (prime/1) might not exactly equal 1.0
    large_prime = "1000000007"
    assert simplify(f"1/{large_prime}", f"{large_prime}/1") is True
    assert simplify(f"{large_prime}/1", f"1/{large_prime}") is True


def test_simplify_large_integer_product():
    """Ensures very large products (beyond standard float precision) are handled."""
    large_num = "1000000000"
    large_den = "1000000001"
    # (large_num/large_den) * (large_den/large_num) = 1 (True)
    assert simplify(f"{large_num}/{large_den}", f"{large_den}/{large_num}") is True