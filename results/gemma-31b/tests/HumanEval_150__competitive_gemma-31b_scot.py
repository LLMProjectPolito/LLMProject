
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

@pytest.mark.parametrize("n, x, y, expected", [
    (7, 34, 12, 34),    # Prime number
    (15, 8, 5, 5),      # Composite number
    (2, 100, 200, 100), # Smallest prime
    (3, 100, 200, 100), # Prime number
    (4, 100, 200, 200), # Composite number
    (1, 100, 200, 200), # 1 is not prime
    (0, 100, 200, 200), # 0 is not prime
    (-7, 100, 200, 200),# Negative numbers are not prime
    (101, 50, 60, 50),  # Larger prime
    (100, 50, 60, 60),  # Larger composite
])
def test_x_or_y(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

def test_x_or_y_with_different_types():
    # Testing with strings to ensure it returns the object regardless of type
    assert x_or_y(2, "prime", "not prime") == "prime"
    assert x_or_y(4, "prime", "not prime") == "not prime"