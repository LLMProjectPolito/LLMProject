
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
    (7, 34, 12, 34),        # Example case 1
    (11, "prime", "not", "prime"), 
    (13, True, False, True),
    (17, [1], [2], [1]),
    (19, {"a": 1}, {"b": 2}, {"a": 1}), # Dictionary type
    (97, 100, 200, 100),    # Larger prime
    (104729, "x", "y", "x"), # Large prime
    (2147483647, "large_p", "large_c", "large_p"), # Boundary: Large Mersenne prime (2^31 - 1)
    
    # Non-prime numbers (should return y)
    (15, 8, 5, 5),          # Example case 2
    (4, 10, 20, 20),        # Smallest composite
    (9, 10, 20, 20),        # Odd composite
    (1, 10, 20, 20),        # 1 is not prime
    (0, 10, 20, 20),        # 0 is not prime
    (-1, 10, 20, 20),       # Negative numbers are not prime
    (-7, 10, 20, 20),       # Negative prime-like numbers are not prime
    (100, "x", "y", "y"),   # Even composite
    (104730, "x", "y", "y"), # Large composite
    (2147483648, "large_p", "large_c", "large_c"), # Boundary: Large composite (2^31)
])
def test_x_or_y(n, x, y, expected):
    """Test x_or_y with various prime and non-prime inputs, including different types for x and y."""
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n", [
    7.5,        # Float
    "7",        # String
    None,       # NoneType
    [7],        # List
    {"n": 7},   # Dict
])
def test_x_or_y_invalid_n_type(n):
    """Test that non-integer values for n raise a TypeError."""
    with pytest.raises(TypeError):
        x_or_y(n, 10, 20)