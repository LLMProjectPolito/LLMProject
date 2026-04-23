
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

# The function signature for reference:
# def x_or_y(n, x, y): ...

@pytest.mark.parametrize("n, x, y, expected", [
    # --- Happy Path: Prime Numbers ---
    (2, 10, 20, 10),      # Smallest prime
    (3, 10, 20, 10),      # Small odd prime
    (7, 34, 12, 34),      # Example from docstring
    (13, 1, 0, 1),        # Prime returning x
    (104729, 100, 200, 100), # Large prime
    
    # --- Happy Path: Composite Numbers ---
    (4, 10, 20, 20),      # Smallest even composite
    (9, 10, 20, 20),      # Small odd composite
    (15, 8, 5, 5),        # Example from docstring
    (104728, 100, 200, 200), # Large composite
    
    # --- Boundary Cases: Non-Primes < 2 ---
    (1, 10, 20, 20),      # 1 is NOT prime
    (0, 10, 20, 20),      # 0 is NOT prime
    (-1, 10, 20, 20),     # Negative numbers are NOT prime
    (-7, 10, 20, 20),     # Negative odd numbers are NOT prime
    (-4, 10, 20, 20),     # Negative even numbers are NOT prime
])
def test_x_or_y_logic(n, x, y, expected):
    """Tests the core logic for primes, composites, and numbers < 2."""
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("x, y, expected_x, expected_y", [
    # Testing different types for x and y to ensure the function 
    # doesn't perform unexpected type casting on the return value.
    (0, 1, 0, 1),             # Integers
    (1.5, 2.5, 1.5, 2.5),     # Floats
    ("prime", "not_prime", "prime", "not_prime"), # Strings
    (None, False, None, False), # Mixed types
])
def test_x_or_y_value_types(x, y, expected_x, expected_y):
    """Ensures the function returns the exact value/type of x or y."""
    # Test with a known prime
    assert x_or_y(7, x, y) == expected_x
    # Test with a known composite
    assert x_or_y(8, x, y) == expected_y

def test_x_or_y_identical_values():
    """Tests behavior when x and y are the same value."""
    assert x_or_y(7, 10, 10) == 10
    assert x_or_y(8, 10, 10) == 10

def test_x_or_y_large_input_performance():
    """
    Tests if the function can handle a relatively large prime 
    without timing out (checks for inefficient primality algorithms).
    """
    import time
    start_time = time.time()
    # 104729 is the 10,000th prime
    result = x_or_y(104729, 1, 0)
    end_time = time.time()
    
    assert result == 1
    assert (end_time - start_time) < 0.1  # Should be near-instant