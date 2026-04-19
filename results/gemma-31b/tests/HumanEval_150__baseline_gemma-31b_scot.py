
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

# The function x_or_y is assumed to be imported or defined in the environment.
# As per rules, I will not redefine it here.

@pytest.mark.parametrize("n, x, y", [
    (2, 10, 20),    # Smallest prime
    (3, 10, 20),    # Small prime
    (7, 34, 12),    # Example from docstring
    (13, "Prime", "Not Prime"),
    (17, 1.1, 2.2),
    (101, True, False),
])
def test_x_or_y_primes(n, x, y):
    """Test that prime numbers return the value of x."""
    assert x_or_y(n, x, y) == x

@pytest.mark.parametrize("n, x, y", [
    (4, 10, 20),    # Smallest composite
    (9, 10, 20),    # Odd composite
    (15, 8, 5),     # Example from docstring
    (25, "Prime", "Not Prime"),
    (100, 1.1, 2.2),
])
def test_x_or_y_composites(n, x, y):
    """Test that composite numbers return the value of y."""
    assert x_or_y(n, x, y) == y

@pytest.mark.parametrize("n, x, y", [
    (1, 10, 20),    # 1 is not prime
    (0, 10, 20),    # 0 is not prime
    (-1, 10, 20),   # Negative numbers are not prime
    (-7, 10, 20),   # Negative prime-like numbers are not prime
])
def test_x_or_y_edge_cases(n, x, y):
    """Test that 0, 1, and negative numbers return the value of y."""
    assert x_or_y(n, x, y) == y

def test_x_or_y_complex_types():
    """Test that the function handles complex return types for x and y."""
    x_val = {"key": "value"}
    y_val = [1, 2, 3]
    
    # 11 is prime -> return x
    assert x_or_y(11, x_val, y_val) == {"key": "value"}
    # 12 is not prime -> return y
    assert x_or_y(12, x_val, y_val) == [1, 2, 3]

def test_x_or_y_large_numbers():
    """Test with larger prime and composite numbers."""
    # 7919 is the 1000th prime number
    assert x_or_y(7919, "Prime", "Not Prime") == "Prime"
    # 7920 is clearly composite
    assert x_or_y(7920, "Prime", "Not Prime") == "Not Prime"