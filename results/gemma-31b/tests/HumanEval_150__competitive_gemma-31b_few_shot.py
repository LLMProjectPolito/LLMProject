
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

@pytest.mark.parametrize("n, x, y, expected", [
    (7, 34, 12, 34),    # Prime
    (15, 8, 5, 5),      # Composite
    (2, 10, 20, 10),    # Smallest prime
    (3, 100, 200, 100), # Prime
    (4, 100, 200, 200), # Composite
    (1, 50, 60, 60),    # 1 is not prime
    (0, 50, 60, 60),    # 0 is not prime
    (-7, 50, 60, 60),   # Negative numbers are not prime
    (11, "apple", "banana", "apple"), # Prime with strings
    (9, "apple", "banana", "banana"), # Composite with strings
    (13, None, False, None),          # Prime with None
    (14, None, False, False),         # Composite with False
])
def test_x_or_y(n, x, y, expected):
    assert x_or_y(n, x, y) == expected