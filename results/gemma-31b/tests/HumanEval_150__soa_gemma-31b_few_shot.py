
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

@pytest.mark.parametrize("n, x, y, expected", [
    (7, 34, 12, 34),      # Prime: 7
    (15, 8, 5, 5),        # Composite: 15
    (2, 100, 200, 100),   # Smallest prime: 2
    (3, "Prime", "Not", "Prime"), # Small prime: 3
    (4, "Prime", "Not", "Not"),   # Smallest composite: 4
    (1, "Prime", "Not", "Not"),   # 1 is not prime
    (0, "Prime", "Not", "Not"),   # 0 is not prime
    (-7, "Prime", "Not", "Not"),  # Negative numbers are not prime
    (11, 1.1, 2.2, 1.1),  # Prime: 11
    (9, 1.1, 2.2, 2.2),   # Composite: 9
    (101, "A", "B", "A"), # Larger prime: 101
    (100, "A", "B", "B"), # Larger composite: 100
])
def test_x_or_y(n, x, y, expected):
    assert x_or_y(n, x, y) == expected