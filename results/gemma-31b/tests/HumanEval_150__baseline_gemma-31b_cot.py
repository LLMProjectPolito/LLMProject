
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
    (5, 10, 20, 10),
    (7, 34, 12, 34),
    (11, 10, 20, 10),
    (13, 10, 20, 10),
    (17, 10, 20, 10),
    (19, 10, 20, 10),
    (101, "Prime", "Not Prime", "Prime"),
    (104729, "Prime", "Not Prime", "Prime"), # Large prime
    
    # Non-prime numbers (should return y)
    (4, 10, 20, 20),
    (6, 10, 20, 20),
    (8, 10, 20, 20),
    (9, 10, 20, 20),
    (10, 10, 20, 20),
    (15, 8, 5, 5),
    (21, 10, 20, 20),
    (25, 10, 20, 20),
    (100, "Prime", "Not Prime", "Not Prime"),
    (104730, "Prime", "Not Prime", "Not Prime"), # Large composite
    
    # Edge cases for n (numbers < 2 are not prime)
    (1, 10, 20, 20),
    (0, 10, 20, 20),
    (-1, 10, 20, 20),
    (-7, 10, 20, 20),
    (-2, 10, 20, 20),
])
def test_x_or_y_logic(n, x, y, expected):
    """Test the core logic of x_or_y for various prime and non-prime inputs."""
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("x, y", [
    (None, "Value"),
    ("Value", None),
    ([1, 2], [3, 4]),
    ({"key": "val"}, {"other": "val"}),
    (1.5, 2.5),
])
def test_x_or_y_types(x, y):
    """Test that x and y can be of any data type."""
    # 7 is prime -> should return x
    assert x_or_y(7, x, y) == x
    # 4 is not prime -> should return y
    assert x_or_y(4, x, y) == y

def test_x_or_y_large_prime():
    """Explicit test for a known large prime to ensure efficiency/correctness."""
    # 7919 is the 1000th prime number
    assert x_or_y(7919, "Yes", "No") == "Yes"

def test_x_or_y_large_composite():
    """Explicit test for a large composite number."""
    # 7920 is clearly not prime
    assert x_or_y(7920, "Yes", "No") == "No"