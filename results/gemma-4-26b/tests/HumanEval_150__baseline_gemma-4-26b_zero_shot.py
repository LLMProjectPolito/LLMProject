
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

@pytest.mark.parametrize("n, x, y, expected", [
    # --- Prime Numbers (Should return x) ---
    (2, "x", "y", "x"),           # Smallest prime
    (3, "x", "y", "x"),
    (5, "x", "y", "x"),
    (7, 34, 12, 34),              # Provided Example 1
    (11, 100, 5, 100),
    (13, 1, 0, 1),
    (7919, "large_prime", "not", "large_prime"), # Large prime
    
    # --- Non-Prime Numbers (Should return y) ---
    (4, "x", "y", "y"),           # Smallest composite
    (6, "x", "y", "y"),
    (8, "x", "y", "y"),
    (9, "x", "y", "y"),
    (15, 8, 5, 5),                # Provided Example 2
    (100, 1, 0, 0),
    (7920, "x", "y", "y"),        # Large composite
    
    # --- Edge Cases: 1, 0, and Negative Numbers (Should return y) ---
    (1, "x", "y", "y"),           # 1 is not prime
    (0, "x", "y", "y"),           # 0 is not prime
    (-1, "x", "y", "y"),          # Negative numbers are not prime
    (-2, "x", "y", "y"),
    (-7, "x", "y", "y"),
    
    # --- Type Flexibility (x and y can be various types) ---
    (2, 3.14, 2.71, 3.14),        # Floats
    (4, [1, 2], [3, 4], [3, 4]),  # Lists
    (7, {"a": 1}, {"b": 2}, {"a": 1}), # Dicts
    (11, None, "not_none", None), # NoneType
])
def test_x_or_y(n, x, y, expected):
    """
    Comprehensive test suite for x_or_y.
    Tests prime logic, non-prime logic, edge cases (0, 1, negatives),
    and ensures the function handles various data types for x and y.
    """
    assert x_or_y(n, x, y) == expected