
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

# The function x_or_y is assumed to be defined in the environment.
# We are testing its logic based on the provided docstring.

@pytest.mark.parametrize("n, x, y", [
    (2, "prime", "not prime"),
    (3, "prime", "not prime"),
    (5, "prime", "not prime"),
    (7, "prime", "not prime"),
    (11, "prime", "not prime"),
    (13, "prime", "not prime"),
    (17, "prime", "not prime"),
    (19, "prime", "not prime"),
    (23, "prime", "not prime"),
    (29, "prime", "not prime"),
])
def test_prime_cases(n, x, y):
    """Verify that known prime numbers return the value of x."""
    assert x_or_y(n, x, y) == x

@pytest.mark.parametrize("n, x, y", [
    (4, "prime", "not prime"),
    (6, "prime", "not prime"),
    (8, "prime", "not prime"),
    (9, "prime", "not prime"),
    (10, "prime", "not prime"),
    (15, "prime", "not prime"),
    (21, "prime", "not prime"),
    (25, "prime", "not prime"),
    (27, "prime", "not prime"),
])
def test_composite_cases(n, x, y):
    """Verify that composite numbers return the value of y."""
    assert x_or_y(n, x, y) == y

@pytest.mark.parametrize("n, x, y", [
    (1, "prime", "not prime"),
    (0, "prime", "not prime"),
    (-1, "prime", "not prime"),
    (-2, "prime", "not prime"),
    (-7, "prime", "not prime"),
    (-11, "prime", "not prime"),
])
def test_non_prime_low_values(n, x, y):
    """Verify that numbers less than 2 (including negatives) return the value of y."""
    assert x_or_y(n, x, y) == y

def test_large_values():
    """Verify correctness with larger integers."""
    # 104729 is the 10,000th prime number
    assert x_or_y(104729, "prime", "not prime") == "prime"
    # 104728 is clearly even and > 2, so not prime
    assert x_or_y(104728, "prime", "not prime") == "not prime"

def test_type_agnosticism():
    """Verify that x and y can be of any data type."""
    # Testing with lists
    assert x_or_y(7, [1, 2], [3, 4]) == [1, 2]
    # Testing with None
    assert x_or_y(10, "something", None) is None
    # Testing with dictionaries
    assert x_or_y(13, {"key": "prime"}, {"key": "not prime"}) == {"key": "prime"}

def test_provided_examples():
    """Verify the examples provided in the docstring."""
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5