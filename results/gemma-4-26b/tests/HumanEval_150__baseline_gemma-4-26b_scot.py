
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

# Note: x_or_y is assumed to be defined in the environment as per instructions.

@pytest.mark.parametrize("n, x, y, expected", [
    (7, 34, 12, 34),   # Docstring example 1
    (15, 8, 5, 5),     # Docstring example 2
])
def test_docstring_examples(n, x, y, expected):
    """Verify the specific examples provided in the function docstring."""
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 97])
def test_prime_numbers(n):
    """Verify that prime numbers correctly return the value of x."""
    x, y = "prime_val", "not_prime_val"
    assert x_or_y(n, x, y) == x

@pytest.mark.parametrize("n", [4, 6, 8, 9, 10, 12, 14, 15, 21, 25, 100])
def test_composite_numbers(n):
    """Verify that composite numbers correctly return the value of y."""
    x, y = "prime_val", "not_prime_val"
    assert x_or_y(n, x, y) == y

@pytest.mark.parametrize("n", [0, 1, -1, -2, -7, -10])
def test_non_prime_edge_cases(n):
    """Verify that 0, 1, and negative numbers are treated as non-prime."""
    x, y = "prime_val", "not_prime_val"
    assert x_or_y(n, x, y) == y

@pytest.mark.parametrize("n, x, y, expected", [
    (7, "hello", "world", "hello"),      # String types
    (10, 3.14, 2.71, 2.71),              # Float types
    (13, [1, 2], {"a": 1}, [1, 2]),      # Collection types
    (4, None, True, True),               # None and Boolean types
])
def test_type_agnosticism(n, x, y, expected):
    """Verify that the function returns x or y regardless of their data types."""
    assert x_or_y(n, x, y) == expected

def test_large_prime_and_composite():
    """Test with larger integer values to ensure stability."""
    large_prime = 104729  # The 10,000th prime
    large_composite = 104728
    assert x_or_y(large_prime, "is_prime", "is_not") == "is_prime"
    assert x_or_y(large_composite, "is_prime", "is_not") == "is_not"