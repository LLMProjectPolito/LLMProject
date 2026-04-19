
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
    (3, 10, 20, 10),        # Small odd prime
    (7, 34, 12, 34),        # Example from docstring
    (11, 100, 200, 100),    # Medium prime
    (13, "Prime", "Not", "Prime"), # Testing with strings
    (97, 1, 0, 1),          # Largest 2-digit prime
    (101, True, False, True), # Smallest 3-digit prime
    
    # Non-prime numbers (should return y)
    (0, 10, 20, 20),        # Zero
    (1, 10, 20, 20),        # One
    (-1, 10, 20, 20),       # Negative odd
    (-2, 10, 20, 20),       # Negative even
    (-7, 10, 20, 20),       # Negative prime-like
    (4, 10, 20, 20),        # Smallest composite
    (15, 8, 5, 5),          # Example from docstring
    (25, 10, 20, 20),       # Square of a prime
    (100, 10, 20, 20),      # Large composite
])
def test_x_or_y(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

def test_x_or_y_large_prime():
    # Testing a larger known prime: 7919
    assert x_or_y(7919, "Yes", "No") == "Yes"

def test_x_or_y_large_composite():
    # Testing a larger known composite: 7920
    assert x_or_y(7920, "Yes", "No") == "No"