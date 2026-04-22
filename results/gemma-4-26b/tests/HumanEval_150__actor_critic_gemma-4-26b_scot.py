
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

@pytest.mark.parametrize("n, x, y", [
    (2, "prime", "not_prime"),
    (3, 100, 200),
    (7, True, False),
    (11, [1], [2]),
    (13, {"a": 1}, {"b": 2}),
    (17, None, "NoneType"),
    (19, 999999, 0),
    (97, "large_prime", "not_large"),
])
def test_prime_numbers(n, x, y):
    """Tests that prime numbers correctly return the value of x."""
    assert x_or_y(n, x, y) == x

@pytest.mark.parametrize("n, x, y", [
    (4, "prime", "not_prime"),
    (6, 100, 200),
    (8, True, False),
    (9, [1], [2]),
    (15, {"a": 1}, {"b": 2}),
    (21, None, "NoneType"),
    (25, 999999, 0),
    (100, "is_prime", "is_not_prime"),
])
def test_non_prime_numbers(n, x, y):
    """Tests that composite numbers correctly return the value of y."""
    assert x_or_y(n, x, y) == y

@pytest.mark.parametrize("n, x, y", [
    (1, "a", "b"),               # Boundary: 1 is not prime
    (0, [1], [2]),               # Boundary: 0 is not prime
    (-1, {"key": "val"}, None),  # Boundary: Negative numbers
    (-7, "neg", "val"),          # Boundary: Negative numbers
    (True, "x_val", "y_val"),    # Boolean: True is 1 (not prime)
    (False, 10, 20),             # Boolean: False is 0 (not prime)
])
def test_boundary_and_non_positive_numbers(n, x, y):
    """Tests that 1, 0, negatives, and booleans return y using diverse x/y types."""
    assert x_or_y(n, x, y) == y

@pytest.mark.parametrize("n", [
    "7",        # String
    2.5,        # Non-integer float
    [2],        # List
    None,       # NoneType
    2.0,        # Integer-valued float (tests strictness)
])
def test_invalid_n_types(n):
    """Tests that non-integer types for n raise a TypeError."""
    with pytest.raises(TypeError):
        x_or_y(n, "x", "y")

@pytest.mark.parametrize("n, expected", [
    (1000000000039, "is_prime"),           # Large prime
    (1000000000000, "is_not_prime"),       # Large composite
    (1000036000099, "is_not_prime"),       # Large semi-prime (1000003 * 1000033)
])
def test_large_integers(n, expected):
    """Tests the function with large numerical values, including semi-primes."""
    x, y = "is_prime", "is_not_prime"
    assert x_or_y(n, x, y) == expected