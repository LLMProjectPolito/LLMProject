
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
    (2, 10, 20, 10),
    (3, 10, 20, 10),
    (5, "Prime", "Not Prime", "Prime"),
    (7, 34, 12, 34),
    (11, 100, 200, 100),
    (13, True, False, True),
    (17, [1], [2], [1]),
    (19, 0, 1, 0),
    (97, "large_prime", "composite", "large_prime"),
    (101, "A", "B", "A"),
    (104729, "BigPrime", "Not", "BigPrime"), # 10,000th prime
    
    # Non-prime numbers (should return y)
    (0, 10, 20, 20),
    (1, 10, 20, 20),
    (4, 10, 20, 20),
    (6, "Prime", "Not Prime", "Not Prime"),
    (8, 100, 200, 200),
    (9, True, False, False),
    (10, 0, 1, 1),
    (15, 8, 5, 5),
    (21, "A", "B", "B"),
    (25, 1, 2, 2),
    (100, "X", "Y", "Y"),
    (104728, "yes", "no", "no"),
    (1000000, 1, 2, 2),
    
    # Negative numbers (not prime, should return y)
    (-1, 10, 20, 20),
    (-2, 10, 20, 20),
    (-3, 10, 20, 20),
    (-7, 10, 20, 20),
    (-11, 10, 20, 20),
])
def test_x_or_y(n, x, y, expected):
    """Tests x_or_y with prime, non-prime, and edge case values of n."""
    assert x_or_y(n, x, y) == expected

def test_x_or_y_with_none():
    """Tests that None is handled correctly as x or y."""
    assert x_or_y(7, None, 10) is None
    assert x_or_y(4, None, 10) == 10
    assert x_or_y(7, 10, None) == 10
    assert x_or_y(4, 10, None) is None

def test_x_or_y_complex_types():
    """Tests that complex objects (dicts, lists) are returned correctly."""
    x_val = {"key": "value"}
    y_val = [1, 2, 3]
    assert x_or_y(2, x_val, y_val) == x_val
    assert x_or_y(4, x_val, y_val) == y_val