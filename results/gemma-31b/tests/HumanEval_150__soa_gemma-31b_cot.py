
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
    (13, "prime", "not", "prime"), # Different types for x, y
    (17, 1.1, 2.2, 1.1),    # Float values
    (97, 5, 6, 5),          # Largest 2-digit prime
    
    # Non-prime numbers (should return y)
    (15, 8, 5, 5),          # Example from docstring (composite)
    (4, 10, 20, 20),        # Smallest composite
    (1, 10, 20, 20),        # 1 is not prime
    (0, 10, 20, 20),        # 0 is not prime
    (-1, 10, 20, 20),       # Negative numbers are not prime
    (-7, 10, 20, 20),       # Negative prime-like numbers are not prime
    (9, 10, 20, 20),        # Odd composite
    (100, 10, 20, 20),      # Large composite
    (21, 10, 20, 20),       # Composite
    (25, 10, 20, 20),       # Perfect square composite
])
def test_x_or_y(n, x, y, expected):
    """Test x_or_y with various prime and non-prime inputs."""
    assert x_or_y(n, x, y) == expected

def test_x_or_y_large_prime():
    """Test with a larger prime number."""
    # 104729 is the 10,000th prime number
    assert x_or_y(104729, "X", "Y") == "X"

def test_x_or_y_large_composite():
    """Test with a larger composite number."""
    assert x_or_y(104730, "X", "Y") == "Y"