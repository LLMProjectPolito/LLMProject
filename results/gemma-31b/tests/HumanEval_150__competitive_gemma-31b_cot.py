
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

@pytest.mark.parametrize("n, x, y, expected", [
    # Primes
    (2, 10, 20, 10),
    (3, 10, 20, 10),
    (5, 10, 20, 10),
    (7, 34, 12, 34),
    (11, 10, 20, 10),
    (13, 10, 20, 10),
    (17, 10, 20, 10),
    (19, 10, 20, 10),
    (97, 10, 20, 10),
    
    # Non-primes (Composites)
    (4, 10, 20, 20),
    (6, 10, 20, 20),
    (8, 10, 20, 20),
    (9, 10, 20, 20),
    (10, 10, 20, 20),
    (15, 8, 5, 5),
    (21, 10, 20, 20),
    (25, 10, 20, 20),
    (100, 10, 20, 20),
    
    # Edge cases for primality
    (1, 10, 20, 20),
    (0, 10, 20, 20),
    (-1, 10, 20, 20),
    (-7, 10, 20, 20),
    
    # Different types for x and y
    (7, "prime", "not prime", "prime"),
    (15, "prime", "not prime", "not prime"),
    (2, [1, 2], [3, 4], [1, 2]),
    (4, [1, 2], [3, 4], [3, 4]),
    (3, None, "value", None),
    (6, None, "value", "value"),
])
def test_x_or_y(n, x, y, expected):
    assert x_or_y(n, x, y) == expected