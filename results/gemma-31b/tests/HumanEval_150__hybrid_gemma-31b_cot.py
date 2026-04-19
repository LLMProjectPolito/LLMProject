
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

@pytest.mark.parametrize("n, x, y, expected", [
    # --- Prime Numbers (should return x) ---
    (2, "prime", "not prime", "prime"),       # Smallest prime, only even prime
    (3, 100, 200, 100),                       # Small odd prime
    (5, "Prime", "Not Prime", "Prime"),       # Basic prime
    (7, 34, 12, 34),                          # Example case
    (11, True, False, True),                  # Basic prime
    (13, 1.1, 2.2, 1.1),                      # Moderate prime
    (17, [1], [2], [1]),                      # Prime with list as x
    (19, {"a": 1}, {"b": 2}, {"a": 1}),       # Prime with dict as x
    (101, "A", "B", "A"),                     # Three-digit prime
    (7919, "large", "small", "large"),        # Large prime
    (104729, 1, 0, 1),                        # 10,000th prime
    
    # --- Non-Prime Numbers (should return y) ---
    # Negative numbers and zero
    (-7, "X", "Y", "Y"),                      # Negative prime-like
    (-3, "X", "Y", "Y"),                      # Negative odd
    (-2, "X", "Y", "Y"),                      # Negative even
    (-1, "X", "Y", "Y"),                      # Negative boundary
    (0, 10, 20, 20),                          # Zero
    (1, "prime", "not prime", "not prime"),   # One is not prime
    
    # Small composites
    (4, 100, 200, 200),                       # Smallest composite
    (6, 10, 20, 20),                          # Even composite
    (8, "Prime", "Not Prime", "Not Prime"),   # Even composite
    (9, "Yes", "No", "No"),                   # Odd composite (square)
    (10, 1.1, 2.2, 2.2),                      # Even composite
    (12, [1], [2], [2]),                      # Even composite
    (14, {"a": 1}, {"b": 2}, {"b": 2}),       # Even composite
    (15, 8, 5, 5),                            # Odd composite
    
    # Larger composites and edge cases
    (100, "Yes", "No", "No"),                 # Even composite
    (121, "Yes", "No", "No"),                 # Square of a prime (11*11)
    (1000, None, "Value", "Value"),           # Large composite
    (104730, 1, 0, 0),                        # Large composite (next to prime)
    (1000000, "prime", "not prime", "not prime"), # Very large composite
])
def test_x_or_y_logic(n, x, y, expected):
    """Test the core logic of x_or_y for a comprehensive set of primes and non-primes."""
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("x, y", [
    (None, None),
    (1.5, 2.5),
    ({"key": "val"}, {"other": "val"}),
    ([1, 2], [3, 4]),
    (lambda x: x, lambda x: x + 1),
])
def test_x_or_y_identity_and_types(x, y):
    """
    Test that x and y can be of any arbitrary data type and that 
    the function returns the exact object reference (identity).
    """
    # n=2 is prime -> should return the exact object x
    assert x_or_y(2, x, y) is x
    # n=4 is not prime -> should return the exact object y
    assert x_or_y(4, x, y) is y

def test_x_or_y_none_handling():
    """Explicitly verify behavior when one of the return values is None."""
    assert x_or_y(7, None, 10) is None
    assert x_or_y(8, 10, None) is None