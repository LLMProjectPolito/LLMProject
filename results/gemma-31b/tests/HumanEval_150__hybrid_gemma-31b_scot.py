
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

# The function x_or_y is assumed to be defined in the environment.
# Logic: return x if n is prime, else y.

@pytest.mark.parametrize("n, x, y, expected", [
    (7, 34, 12, 34),  # Docstring example 1: 7 is prime
    (15, 8, 5, 5),    # Docstring example 2: 15 is composite
])
def test_x_or_y_docstring_examples(n, x, y, expected):
    """Verify the specific examples provided in the docstring."""
    assert x_or_y(n, x, y) == expected

@pytest.mark.parametrize("n", [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 97, 101, 997, 104729
])
def test_x_or_y_primes(n):
    """Test a wide variety of prime numbers, including the smallest prime (2) and large primes."""
    x_val, y_val = "is_prime", "not_prime"
    assert x_or_y(n, x_val, y_val) == x_val

@pytest.mark.parametrize("n", [
    0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 21, 25, 100, 1000, 104730
])
def test_x_or_y_non_primes(n):
    """Test composite numbers, 0, and 1 to ensure y is returned."""
    x_val, y_val = "is_prime", "not_prime"
    assert x_or_y(n, x_val, y_val) == y_val

@pytest.mark.parametrize("n", [-1, -2, -3, -7, -10, -101])
def test_x_or_y_negative_numbers(n):
    """Verify that negative numbers are never considered prime."""
    x_val, y_val = "is_prime", "not_prime"
    assert x_or_y(n, x_val, y_val) == y_val

def test_x_or_y_return_types():
    """Ensure the function handles diverse data types for x and y."""
    # Case: x is a list, y is a dictionary
    assert x_or_y(7, [1, 2], {"key": "val"}) == [1, 2]
    assert x_or_y(8, [1, 2], {"key": "val"}) == {"key": "val"}
    
    # Case: returning floats
    assert x_or_y(4, 1.1, 2.2) == 2.2
    
    # Case: returning None
    assert x_or_y(7, None, "Not None") is None
    assert x_or_y(8, "Not None", None) is None

def test_x_or_y_identical_returns():
    """Test behavior when x and y are the same value."""
    # Regardless of primality, if x == y, the result should be that value
    assert x_or_y(7, 100, 100) == 100
    assert x_or_y(8, 100, 100) == 100