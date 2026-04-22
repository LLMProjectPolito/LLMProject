
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def test_docstring_examples():
    """Verify the examples provided in the function docstring."""
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5

@pytest.mark.parametrize("n, x, y", [
    (2, "prime", "not_prime"),      # Smallest prime
    (3, 100, 200),                  # Small odd prime
    (7, 1.5, 0.5),                  # Float values
    (13, [1, 2], [3, 4]),           # List values
    (101, {"a": 1}, {"b": 2}),      # Dict values
    (7919, True, False),            # Boolean values
    (104729, None, "not_none"),     # None as x
    (1000000007, "large", "small"), # Large prime
])
def test_primes(n, x, y):
    """Tests that x is returned when n is a prime number, across various types."""
    assert x_or_y(n, x, y) == x

@pytest.mark.parametrize("n, x, y", [
    (1, "not_prime", "prime"),      # 1 is not prime
    (0, 0, 1),                      # 0 is not prime
    (-1, "neg", "pos"),             # Negative numbers are not prime
    (-7, 10, 20),                   # Negative odd is not prime
    (4, "even_comp", "odd_comp"),   # Small even composite
    (9, 5, 10),                     # Small odd composite
    (15, "composite", "prime"),    # Medium composite
    (100, "val", None),             # None as y
    (104728, [1], [2]),             # Large composite with lists
    (104727, True, False),          # Large odd composite (divisible by 3)
])
def test_non_primes(n, x, y):
    """Tests that y is returned when n is not a prime number (composite, 0, 1, or negative)."""
    assert x_or_y(n, x, y) == y

@pytest.mark.parametrize("n, x, y, expected", [
    (2, 3.14, 0, 3.14),             # Float integrity
    (4, "hello", "world", "world"), # String integrity
    (3, [1, 2], {"a": 1}, [1, 2]),  # Heterogeneous collection integrity
    (5, None, False, None),         # NoneType integrity
    (6, True, False, False),        # Boolean integrity
])
def test_type_integrity(n, x, y, expected):
    """Ensure the function returns the exact object/type provided without coercion."""
    result = x_or_y(n, x, y)
    assert result == expected
    assert type(result) is type(expected)

def test_large_scale_numbers():
    """Test with very large numbers to ensure logic remains robust and efficient."""
    large_prime = 1000000007
    large_composite = 1000000008
    assert x_or_y(large_prime, 1, 0) == 1
    assert x_or_y(large_composite, 1, 0) == 0

def test_identity_edge_cases():
    """Tests behavior when x and y are the same value."""
    assert x_or_y(7, 42, 42) == 42
    assert x_or_y(8, 42, 42) == 42
    assert x_or_y(13, [1], [1]) == [1]