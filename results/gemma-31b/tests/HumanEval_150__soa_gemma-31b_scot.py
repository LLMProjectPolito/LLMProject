
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
    (2, 10, 20, 10),        # Smallest prime
    (3, 10, 20, 10),        # Small odd prime
    (7, 34, 12, 34),        # Example from docstring
    (11, 100, 200, 100),    # Medium prime
    (13, "Prime", "Not", "Prime"), # Testing different return types
    (101, 1, 0, 1),         # Larger prime
    
    # Non-prime numbers (should return y)
    (1, 10, 20, 20),        # 1 is not prime
    (0, 10, 20, 20),        # 0 is not prime
    (4, 10, 20, 20),        # Smallest composite
    (15, 8, 5, 5),          # Example from docstring (odd composite)
    (9, 100, 200, 200),     # Odd composite
    (100, 1, 0, 0),         # Large composite
    (-1, 10, 20, 20),       # Negative number
    (-7, 10, 20, 20),       # Negative prime-like number
    (-11, "Prime", "Not", "Not"),
])
def test_x_or_y(n, x, y, expected):
    """Tests the x_or_y function with various prime and non-prime inputs."""
    assert x_or_y(n, x, y) == expected

def test_x_or_y_type_consistency():
    """Ensure the function returns the exact object passed as x or y."""
    x_obj = {"key": "value"}
    y_obj = [1, 2, 3]
    
    # 7 is prime -> return x_obj
    assert x_or_y(7, x_obj, y_obj) is x_obj
    # 8 is not prime -> return y_obj
    assert x_or_y(8, x_obj, y_obj) is y_obj