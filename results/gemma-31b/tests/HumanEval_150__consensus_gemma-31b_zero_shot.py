
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
    (2, 10, 20, 10),          # Smallest prime
    (3, 100, 200, 100),       # Small odd prime
    (5, 10, 20, 10),
    (7, 34, 12, 34),          # Example 1
    (11, "yes", "no", "yes"), # Prime with string values
    (13, 10, 20, 10),
    (17, 5.5, 2.2, 5.5),      # Prime with float values
    (19, 10, 20, 10),
    (23, 10, 20, 10),
    (97, "prime", "not", "prime"), # Larger prime
    (101, 1.1, 2.2, 1.1),     # Prime with float return values
    
    # Non-prime numbers (should return y)
    (0, 10, 20, 20),          # 0 is not prime
    (1, 10, 20, 20),          # 1 is not prime
    (4, 10, 20, 20),          # Composite number
    (6, 10, 20, 20),
    (8, 10, 20, 20),
    (9, 10, 20, 20),          # Composite odd number
    (10, 10, 20, 20),
    (12, "Prime", "Not", "Not"),
    (15, 8, 5, 5),            # Example 2
    (21, 10, 20, 20),
    (25, 5.5, 2.2, 2.2),      # Non-prime with float values
    (100, "prime", "not", "not"), # Larger composite
    (102, 1.1, 2.2, 2.2),     # Composite with float return values
    
    # Negative numbers (not prime, should return y)
    (-1, 10, 20, 20),
    (-2, 10, 20, 20),
    (-7, 10, 20, 20),
])
def test_x_or_y_logic(n, x, y, expected):
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("x, y", [
    ("apple", "banana"),
    (1.5, 2.5),
    ([1, 2], [3, 4]),
    (None, "Something"),
    (True, False),
])
def test_x_or_y_types(x, y):
    # Test with a prime (7)
    assert x_or_y(7, x, y) == x
    # Test with a non-prime (4)
    assert x_or_y(4, x, y) == y

def test_x_or_y_large_prime():
    # 104729 is the 10,000th prime number
    assert x_or_y(104729, "prime", "not prime") == "prime"

def test_x_or_y_large_composite():
    # 104730 is clearly composite
    assert x_or_y(104730, "prime", "not prime") == "not prime"