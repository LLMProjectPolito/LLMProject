
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
    (2, "prime", "not prime", "prime"),
    (3, "prime", "not prime", "prime"),
    (5, "prime", "not prime", "prime"),
    (7, 34, 12, 34),
    (11, "prime", "not prime", "prime"),
    (13, "prime", "not prime", "prime"),
    (17, "prime", "not prime", "prime"),
    (19, "prime", "not prime", "prime"),
    (23, "prime", "not prime", "prime"),
    (97, "prime", "not prime", "prime"),
    
    # Non-prime numbers (should return y)
    (4, "prime", "not prime", "not prime"),
    (6, "prime", "not prime", "not prime"),
    (8, "prime", "not prime", "not prime"),
    (9, "prime", "not prime", "not prime"),
    (10, "prime", "not prime", "not prime"),
    (15, 8, 5, 5),
    (21, "prime", "not prime", "not prime"),
    (25, "prime", "not prime", "not prime"),
    (100, "prime", "not prime", "not prime"),
    
    # Edge cases for n (not prime)
    (1, "prime", "not prime", "not prime"),
    (0, "prime", "not prime", "not prime"),
    (-1, "prime", "not prime", "not prime"),
    (-2, "prime", "not prime", "not prime"),
    (-7, "prime", "not prime", "not prime"),
    (-11, "prime", "not prime", "not prime"),
])
def test_x_or_y_logic(n, x, y, expected):
    """Test the core logic for prime and non-prime identification."""
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("x, y", [
    (10.5, 20.5),
    ([1, 2], [3, 4]),
    ({"a": 1}, {"b": 2}),
    (None, "something"),
    ("something", None),
])
def test_x_or_y_return_types(x, y):
    """Ensure the function returns the exact objects passed as x or y regardless of type."""
    # 7 is prime -> returns x
    assert x_or_y(7, x, y) is x
    # 4 is not prime -> returns y
    assert x_or_y(4, x, y) is y

def test_x_or_y_large_prime():
    """Test with a relatively large prime number."""
    # 104729 is the 10,000th prime number
    assert x_or_y(104729, "prime", "not prime") == "prime"

def test_x_or_y_large_composite():
    """Test with a large composite number."""
    # 104728 is even and > 2, so not prime
    assert x_or_y(104728, "prime", "not prime") == "not prime"