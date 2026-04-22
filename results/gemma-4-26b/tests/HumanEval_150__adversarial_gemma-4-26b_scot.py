
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

# The function x_or_y is assumed to be imported or defined in the environment.

@pytest.mark.parametrize("n, x, y", [
    (2, "prime", "not_prime"),
    (3, 100, 200),
    (5, 1.5, 0.5),
    (7, [1], [2]),
    (11, {"a": 1}, {"b": 2}),
    (13, True, False),
    (17, "apple", "orange"),
    (19, 999, 0),
    (23, None, "fallback"),
    (97, "large_prime", "not_prime"),
])
def test_prime_numbers(n, x, y):
    """Tests that prime numbers correctly return the value of x."""
    assert x_or_y(n, x, y) == x

@pytest.mark.parametrize("n, x, y", [
    (4, "prime", "not_prime"),
    (6, 100, 200),
    (8, 1.5, 0.5),
    (9, [1], [2]),
    (10, {"a": 1}, {"b": 2}),
    (12, True, False),
    (14, "apple", "orange"),
    (15, 999, 0),
    (21, None, "fallback"),
    (25, "large_composite", "not_prime"),
])
def test_non_prime_numbers(n, x, y):
    """Tests that composite numbers correctly return the value of y."""
    assert x_or_y(n, x, y) == y

@pytest.mark.parametrize("n", [0, 1])
def test_edge_case_one_and_zero(n):
    """Tests that 0 and 1 are correctly identified as NOT prime."""
    # Using arbitrary x and y to check return value
    assert x_or_y(n, "prime", "not_prime") == "not_prime"

@pytest.mark.parametrize("n", [-1, -2, -3, -7, -10, -100])
def test_negative_numbers(n):
    """Tests that negative numbers are correctly identified as NOT prime."""
    assert x_or_y(n, "prime", "not_prime") == "not_prime"

def test_type_flexibility():
    """Ensures the function handles various data types for x and y without error."""
    # Test with strings
    assert x_or_y(7, "is_prime", "is_not_prime") == "is_prime"
    # Test with floats
    assert x_or_y(4, 1.1, 2.2) == 2.2
    # Test with complex objects (lists)
    assert x_or_y(11, [1, 2], [3, 4]) == [1, 2]
    # Test with None
    assert x_or_y(15, None, None) is None

def test_large_prime_performance_and_correctness():
    """Tests a larger prime number to ensure logic holds."""
    large_prime = 104729  # The 10,000th prime number
    assert x_or_y(large_prime, "yes", "no") == "yes"

def test_large_composite_number():
    """Tests a large composite number."""
    large_composite = 104728
    assert x_or_y(large_composite, "yes", "no") == "no"