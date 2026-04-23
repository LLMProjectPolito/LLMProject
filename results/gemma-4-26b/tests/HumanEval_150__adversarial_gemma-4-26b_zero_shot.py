
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

# The function is assumed to be defined in the same module or imported.
# For the purpose of this test suite, we assume the function signature:
# def x_or_y(n, x, y): ...

@pytest.mark.parametrize("n, x, y, expected", [
    # --- Standard Cases (from docstring) ---
    (7, 34, 12, 34),    # 7 is prime
    (15, 8, 5, 5),      # 15 is composite

    # --- Edge Cases: Smallest Primes ---
    (2, "prime", "not", "prime"),   # 2 is the smallest prime
    (3, 100, 0, 100),               # 3 is prime

    # --- Edge Cases: Non-Primes (Boundary of Primality) ---
    (1, "prime", "not", "not"),     # 1 is NOT prime
    (0, 10, 20, 20),                # 0 is NOT prime
    (-1, 10, 20, 20),               # Negative numbers are NOT prime
    (-7, 10, 20, 20),               # Negative primes are NOT prime
    (4, 1, 0, 0),                   # Smallest composite number

    # --- Edge Cases: Large Numbers ---
    (104729, "yes", "no", "yes"),   # 104729 is the 10,000th prime
    (104728, "yes", "no", "no"),    # Large even number
    (104727, "yes", "no", "no"),    # Large odd composite (divisible by 3)

    # --- Edge Cases: Type Consistency ---
    (7, [1, 2], {3}, [1, 2]),       # x is a list
    (10, None, "fallback", "fallback"), # x is None
    (7, 3.14, 2.71, 3.14),          # x and y are floats
    (7, "A", "B", "A"),             # x and y are strings
])
def test_x_or_y_logic(n, x, y, expected):
    """Tests the core logic of primality detection and value return."""
    from __main__ import x_or_y  # Adjust import based on actual file structure
    assert x_or_y(n, x, y) == expected

def test_x_or_y_identity():
    """Ensures the function returns the exact object (identity) for complex types."""
    from __main__ import x_or_y
    complex_obj = {"key": "value"}
    # If n is prime, it should return the exact same object reference
    assert x_or_y(13, complex_obj, "not_prime") is complex_obj

@pytest.mark.parametrize("n", [
    1.5,    # Float input for n
    "7",    # String input for n
    None,   # None input for n
])
def test_x_or_y_invalid_n_types(n):
    """
    Tests how the function handles non-integer inputs for n.
    Depending on requirements, this should either raise a TypeError 
    or handle it gracefully. A robust function should be tested for this.
    """
    from __main__ import x_or_y
    with pytest.raises((TypeError, ValueError)):
        x_or_y(n, 1, 0)

def test_x_or_y_large_scale_performance():
    """
    A 'Blue Team' check for performance/timeout bugs.
    Checks if the function can handle a moderately large prime without hanging.
    """
    from __main__ import x_or_y
    # 10^6 + 3 is a prime number
    large_prime = 1000003
    assert x_or_y(large_prime, True, False) is True