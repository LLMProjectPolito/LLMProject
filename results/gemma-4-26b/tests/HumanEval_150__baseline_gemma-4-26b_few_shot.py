
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def test_x_or_y_prime_numbers():
    """Tests that x is returned when n is a prime number."""
    # Docstring example
    assert x_or_y(7, 34, 12) == 34
    # Smallest prime
    assert x_or_y(2, "prime", "not") == "prime"
    # Other primes
    assert x_or_y(3, 100, 0) == 100
    assert x_or_y(13, True, False) == True
    assert x_or_y(19, [1, 2], [3, 4]) == [1, 2]

def test_x_or_y_non_prime_numbers():
    """Tests that y is returned when n is a composite number."""
    # Docstring example
    assert x_or_y(15, 8, 5) == 5
    # Smallest composite
    assert x_or_y(4, "prime", "not") == "not"
    # Other composites
    assert x_or_y(6, 1, 0) == 0
    assert x_or_y(9, 10, 20) == 20
    assert x_or_y(25, None, "none") == "none"

def test_x_or_y_edge_cases():
    """Tests edge cases: 0, 1, and negative numbers (none are prime)."""
    # 1 is not prime
    assert x_or_y(1, "x", "y") == "y"
    # 0 is not prime
    assert x_or_y(0, "x", "y") == "y"
    # Negative numbers are not prime
    assert x_or_y(-1, "x", "y") == "y"
    assert x_or_y(-7, 10, 20) == 20
    assert x_or_y(-13, "prime", "not") == "not"

def test_x_or_y_large_numbers():
    """Tests the function with larger integer values."""
    # 104729 is a known prime number
    assert x_or_y(104729, "is_prime", "not_prime") == "is_prime"
    # 104730 is even/composite
    assert x_or_y(104730, "is_prime", "not_prime") == "not_prime"

@pytest.mark.parametrize("n, x, y, expected", [
    (2, 1.5, 2.5, 1.5),      # Floats
    (5, "apple", "orange", "apple"), # Strings
    (11, None, 0, None),     # NoneType
    (12, {"a": 1}, {"b": 2}, {"b": 2}), # Dictionaries
])
def test_x_or_y_parameterized(n, x, y, expected):
    """Parametrized test to ensure various data types for x and y work correctly."""
    assert x_or_y(n, x, y) == expected