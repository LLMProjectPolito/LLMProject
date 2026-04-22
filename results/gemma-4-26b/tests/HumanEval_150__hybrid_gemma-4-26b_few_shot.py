
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

# Note: Assuming x_or_y is imported from your module
# from your_module import x_or_y

@pytest.mark.parametrize("n, x, y, expected", [
    # --- CATEGORY: PRIME NUMBERS (Should return x) ---
    (2, "prime", "not", "prime"),       # Smallest prime (even)
    (3, 10, 20, 10),                    # Small odd prime
    (7, 34, 12, 34),                    # Docstring example 1
    (13, True, False, True),            # Boolean return
    (101, [1], [2], [1]),               # List return
    (8191, "p", "c", "p"),              # Mersenne prime (2^13 - 1)
    (104729, "p", "c", "p"),            # Large prime

    # --- CATEGORY: COMPOSITE NUMBERS (Should return y) ---
    (4, 1, 2, 2),                       # Smallest composite
    (6, "yes", "no", "no"),             # Even composite
    (9, 10.5, 5.5, 5.5),                # Odd composite
    (15, 8, 5, 5),                      # Docstring example 2
    (100, "a", "b", "b"),               # Large composite
    (8192, "p", "c", "c"),              # Power of 2
    (104728, "p", "c", "c"),            # Large composite

    # --- CATEGORY: BOUNDARY CASES (Should return y) ---
    (1, "prime", "not", "not"),         # 1 is not prime
    (0, 10, 20, 20),                    # 0 is not prime
    (-7, "prime", "not", "not"),        # Negative odd is not prime
    (-2, 1, 0, 0),                      # Negative even is not prime
])
def test_x_or_y_core_logic(n, x, y, expected):
    """
    Tests the core mathematical logic: 
    Returns x if n is prime, otherwise returns y.
    Covers primes, composites, and non-prime boundaries (0, 1, negatives).
    """
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n, x, y, expected", [
    (17, {"key": "value"}, None, {"key": "value"}), # Dict and None
    (20, 3.14159, "not prime", "not prime"),       # Float and String
    (11, (1, 2, 3), 99, (1, 2, 3)),                # Tuple and Int
    (5, [1, 2], [3, 4], [1, 2]),                   # List and List
    (3, None, "fallback", None),                   # None and String
])
def test_x_or_y_type_flexibility(n, x, y, expected):
    """
    Ensures the function is type-agnostic regarding the values of x and y.
    """
    assert x_or_y(n, x, y) == expected

def test_x_or_y_performance_and_scale():
    """
    Tests the function with very large integers to ensure the 
    primality test is efficient and doesn't time out.
    """
    large_prime = 104729 
    large_composite = 104728
    
    assert x_or_y(large_prime, "yes", "no") == "yes"
    assert x_or_y(large_composite, "yes", "no") == "no"