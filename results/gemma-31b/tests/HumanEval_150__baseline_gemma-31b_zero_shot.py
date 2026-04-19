
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

@pytest.mark.parametrize("n, x, y, expected", [
    # Prime numbers (should return x)
    (2, 10, 20, 10),        # Smallest prime
    (3, 10, 20, 10),        # Small prime
    (7, 34, 12, 34),        # Example case 1
    (11, 100, 200, 100),    # Medium prime
    (101, "Prime", "Not", "Prime"), # Larger prime with string values
    
    # Non-prime numbers (should return y)
    (4, 10, 20, 20),        # Smallest composite
    (15, 8, 5, 5),          # Example case 2
    (9, 100, 200, 200),     # Odd composite
    (100, "Prime", "Not", "Not"), # Large composite
    
    # Edge cases (should return y)
    (1, 10, 20, 20),        # 1 is not prime
    (0, 10, 20, 20),        # 0 is not prime
    (-1, 10, 20, 20),       # Negative numbers are not prime
    (-7, 10, 20, 20),       # Negative prime-like number is not prime
])
def test_x_or_y(n, x, y, expected):
    """
    Tests x_or_y to ensure it returns x for prime n and y otherwise.
    """
    assert x_or_y(n, x, y) == expected