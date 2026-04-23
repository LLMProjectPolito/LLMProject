
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

# Assuming the function is imported from your module
# from your_module import x_or_y

@pytest.mark.parametrize("n, x, y, expected", [
    # --- Core Logic: Prime Numbers (should return x) ---
    (2, 10, 20, 10),          # Smallest prime
    (3, 10, 20, 10),
    (7, 34, 12, 34),          # Docstring example
    (13, "apple", "orange", "apple"),
    (17, "prime", "not prime", "prime"),
    (104729, "large", "small", "large"), # 10,000th prime
    
    # --- Core Logic: Non-Prime Numbers (should return y) ---
    (4, 10, 20, 20),          # Smallest composite
    (9, 10, 20, 20),
    (15, 8, 5, 5),            # Docstring example
    (20, "prime", "not prime", "not prime"),
    
    # --- Edge Cases for n: 0, 1, and Negatives (none are prime) ---
    (1, 10, 20, 20),
    (0, 10, 20, 20),
    (-7, 10, 20, 20),
    (-2, 10, 20, 20),
])
def test_x_or_y_logic(n, x, y, expected):
    """Tests standard prime, composite, and non-prime edge cases for n."""
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n, x, y, expected", [
    # These tests ensure the function returns the object itself 
    # and doesn't rely on truthiness (e.g., 'return x or y')
    (2, 0, 10, 0),            # x is falsy (int)
    (4, 10, None, None),      # y is falsy (None)
    (2, "", "something", ""), # x is falsy (str)
    (4, "something", [], []), # y is falsy (list)
    (2, False, True, False),  # x is falsy (bool)
    (4, True, 0, 0),          # y is falsy (int)
])
def test_x_or_y_falsy_values(n, x, y, expected):
    """Ensures the function returns the actual object even if it is falsy."""
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("invalid_n", [2.0, "3", None, [2], {"n": 2}])
def test_x_or_y_invalid_n_types(invalid_n):
    """Ensures that non-integer inputs for n raise a TypeError."""
    with pytest.raises(TypeError):
        x_or_y(invalid_n, 1, 2)

def test_x_or_y_large_primes():
    """Tests efficiency and correctness with a large Mersenne prime."""
    large_prime = 2147483647  # 2^31 - 1
    assert x_or_y(large_prime, "is_prime", "is_not_prime") == "is_prime"