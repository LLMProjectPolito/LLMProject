
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    """
    if n < 2:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

@pytest.mark.parametrize("n, x, y, expected", [
    # Basic Primes
    (2, "prime", "not_prime", "prime"),
    (3, "prime", "not_prime", "prime"),
    (5, "prime", "not_prime", "prime"),
    (7, 34, 12, 34),
    (11, "prime", "not_prime", "prime"),
    (13, "prime", "not_prime", "prime"),
    (17, "prime", "not_prime", "prime"),
    (19, "prime", "not_prime", "prime"),
    
    # Basic Composites
    (4, "prime", "not_prime", "not_prime"),
    (6, "prime", "not_prime", "not_prime"),
    (8, "prime", "not_prime", "not_prime"),
    (9, "prime", "not_prime", "not_prime"),
    (10, "prime", "not_prime", "not_prime"),
    (15, 8, 5, 5),
    (21, "prime", "not_prime", "not_prime"),
    (25, "prime", "not_prime", "not_prime"),
    
    # Edge Cases: n < 2
    (1, "prime", "not_prime", "not_prime"),
    (0, "prime", "not_prime", "not_prime"),
    (-1, "prime", "not_prime", "not_prime"),
    (-7, "prime", "not_prime", "not_prime"),
    
    # Large Numbers
    (104729, "prime", "not_prime", "prime"), # 10,000th prime
    (104730, "prime", "not_prime", "not_prime"),
    (1000000, "prime", "not_prime", "not_prime"),
])
def test_x_or_y_logic(n, x, y, expected):
    """Test the core prime detection logic across various ranges."""
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("x, y", [
    (None, False),
    ([1, 2], {"a": 1}),
    (3.14, 2.71),
    ("Hello", "World"),
])
def test_x_or_y_return_types(x, y):
    """Ensure the function returns the exact objects passed as x or y regardless of type."""
    # n=7 is prime -> should return x
    assert x_or_y(7, x, y) is x
    # n=4 is not prime -> should return y
    assert x_or_y(4, x, y) is y

def test_x_or_y_large_prime_performance():
    """Check if the function handles a moderately large prime efficiently."""
    # 1000003 is prime
    assert x_or_y(1000003, "prime", "not_prime") == "prime"