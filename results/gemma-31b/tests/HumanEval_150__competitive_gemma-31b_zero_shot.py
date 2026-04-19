
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

@pytest.mark.parametrize("n, x, y, expected", [
    # Primes (should return x)
    (2, 10, 20, 10),
    (3, 10, 20, 10),
    (5, 10, 20, 10),
    (7, 34, 12, 34),
    (11, 10, 20, 10),
    (13, 10, 20, 10),
    (17, 10, 20, 10),
    (19, 10, 20, 10),
    (97, 10, 20, 10),
    
    # Non-primes (should return y)
    (0, 10, 20, 20),
    (1, 10, 20, 20),
    (4, 10, 20, 20),
    (6, 10, 20, 20),
    (8, 10, 20, 20),
    (9, 10, 20, 20),
    (10, 10, 20, 20),
    (15, 8, 5, 5),
    (21, 10, 20, 20),
    (25, 10, 20, 20),
    
    # Negative numbers (not prime, should return y)
    (-1, 10, 20, 20),
    (-2, 10, 20, 20),
    (-3, 10, 20, 20),
    (-7, 10, 20, 20),
    
    # Different data types for x and y
    (7, "Prime", "Not Prime", "Prime"),
    (8, "Prime", "Not Prime", "Not Prime"),
    (2, [1, 2], [3, 4], [1, 2]),
    (4, [1, 2], [3, 4], [3, 4]),
])
def test_x_or_y(n, x, y, expected):
    assert x_or_y(n, x, y) == expected