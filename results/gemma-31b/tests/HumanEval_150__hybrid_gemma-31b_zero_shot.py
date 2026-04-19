
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.
    """
    if n < 2:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

# --- Superior Pytest Suite ---

@pytest.mark.parametrize("n, x, y, expected", [
    (2, "prime", "not prime", "prime"),      # Smallest prime
    (3, "prime", "not prime", "prime"),      # Smallest odd prime
    (5, "prime", "not prime", "prime"),      # Basic prime
    (7, 34, 12, 34),                         # Example from docstring
    (11, True, False, True),                 # Mid-range prime
    (13, 100, 200, 100),                     # Prime
    (17, "A", "B", "A"),                     # Prime
    (19, 1.1, 2.2, 1.1),                     # Prime
    (101, "X", "Y", "X"),                    # Larger prime
    (104729, "Prime", "Not Prime", "Prime"), # 10,000th prime
])
def test_x_or_y_prime_cases(n, x, y, expected):
    """Tests cases where n is a prime number, expecting x to be returned."""
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n, x, y, expected", [
    (4, "prime", "not prime", "not prime"),  # Smallest composite (even)
    (6, "prime", "not prime", "not prime"),  # Composite
    (8, "prime", "not prime", "not prime"),  # Composite
    (9, "prime", "not prime", "not prime"),  # Smallest composite (odd/square)
    (10, True, False, False),                # Composite
    (15, 8, 5, 5),                           # Example from docstring
    (21, 100, 200, 200),                     # Composite
    (25, "A", "B", "B"),                     # Square of a prime
    (100, 1.1, 2.2, 2.2),                    # Large composite
    (104730, "Prime", "Not Prime", "Not Prime"), # Large composite
    (1000000, "Prime", "Not Prime", "Not Prime"), # Efficiency check
])
def test_x_or_y_composite_cases(n, x, y, expected):
    """Tests cases where n is a composite number, expecting y to be returned."""
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n, x, y, expected", [
    (1, "prime", "not prime", "not prime"),  # 1 is not prime
    (0, "prime", "not prime", "not prime"),  # 0 is not prime
    (-1, "prime", "not prime", "not prime"), # Negative integers are not prime
    (-7, "prime", "not prime", "not prime"), # Negative prime-looking integers
])
def test_x_or_y_edge_cases(n, x, y, expected):
    """Tests boundary cases where n < 2, which are by definition not prime."""
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("x, y", [
    (100, 200),                # Integers
    (1.5, 2.5),                # Floats
    ([1, 2], [3, 4]),          # Lists
    ({"key": "val"}, None),    # Dict and None
    ("Hello", "World"),        # Strings
])
def test_x_or_y_type_flexibility(x, y):
    """Tests that the function handles various data types and returns the exact object."""
    # n=2 is prime, should return x (identity check)
    assert x_or_y(2, x, y) is x
    # n=4 is not prime, should return y (identity check)
    assert x_or_y(4, x, y) is y

def test_x_or_y_identity():
    """Test behavior when x and y are the same value."""
    assert x_or_y(7, 10, 10) == 10
    assert x_or_y(8, 10, 10) == 10