
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def is_prime(n):
    """Helper function to determine if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def x_or_y(n, x, y):
    """
    This function takes an integer n and two numbers x and y.
    If n is a prime number, it returns x. Otherwise, it returns y.
    """
    if is_prime(n):
        return x
    else:
        return y

def test_x_or_y_prime_number():
    """Test when n is a prime number."""
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 5, 1) == 5
    assert x_or_y(5, 100, 0) == 100
    assert x_or_y(11, -1, 1) == -1
    assert x_or_y(13, -1, 1) == -1
    assert x_or_y(17, 1000000, 2000000) == 1000000
    assert x_or_y(1000000007, 100, 200) == 100

def test_x_or_y_non_prime_number():
    """Test when n is not a prime number."""
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 7, 8) == 8
    assert x_or_y(9, 0, -1) == -1
    assert x_or_y(10, 1000, 1) == 1
    assert x_or_y(1000000008, 300, 400) == 400

def test_x_or_y_edge_cases():
    """Test edge cases like 0, 1, and negative numbers."""
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(1, 3, 4) == 4
    assert x_or_y(-1, 1, 2) == 2
    assert x_or_y(-5, 5, 6) == 6  # Negative input for n
    assert x_or_y(2, 0, 0) == 0
    assert x_or_y(1, 0, 0) == 0

def test_x_or_y_large_numbers():
    """Test with large numbers to check for potential overflow issues."""
    assert x_or_y(17, 1000000, 2000000) == 1000000
    assert x_or_y(100, 1000, 2000) == 2000
    assert x_or_y(1000000007, 100, 200) == 100
    assert x_or_y(1000000008, 300, 400) == 400

def test_x_or_y_same_values():
    """Test when x and y are the same."""
    assert x_or_y(7, 5, 5) == 5
    assert x_or_y(4, 10, 10) == 10

def test_x_or_y_float_values():
    """Test with float values for x and y."""
    assert x_or_y(7, 3.14, 2.71) == 3.14
    assert x_or_y(4, 1.0, 2.0) == 2.0

def test_x_or_y_mixed_types():
    """Test with mixed types for x and y (int and float)."""
    assert x_or_y(7, 10, 3.14) == 10
    assert x_or_y(4, 2.71, 5) == 5

def test_x_or_y_negative_x_and_y():
    """Test with negative values for x and y."""
    assert x_or_y(7, -10, -20) == -10
    assert x_or_y(4, -5, -6) == -6

def test_x_or_y_mixed_signs():
    """Test with mixed signs for x and y."""
    assert x_or_y(7, -10, 20) == -10
    assert x_or_y(4, 5, -6) == -6