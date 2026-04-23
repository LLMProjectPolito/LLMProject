
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_x_or_y_prime():
    """Test case where n is a prime number."""
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(5, 100, 200) == 100
    assert x_or_y(11, 5, 10) == 5

def test_x_or_y_not_prime():
    """Test case where n is not a prime number."""
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 10, 20) == 20
    assert x_or_y(6, 100, 200) == 200
    assert x_or_y(9, 5, 10) == 10
    assert x_or_y(1, 5, 10) == 10

def test_x_or_y_edge_cases():
    """Test case for edge cases like 0, 1, and negative numbers."""
    assert x_or_y(0, 5, 10) == 10
    assert x_or_y(1, 5, 10) == 10
    assert x_or_y(-5, 5, 10) == 10  # Negative numbers are not prime

def test_x_or_y_same_values():
    """Test case where x and y are the same."""
    assert x_or_y(7, 5, 5) == 5
    assert x_or_y(4, 5, 5) == 5

def test_x_or_y_large_numbers():
    """Test case with large numbers to ensure no overflow issues."""
    assert x_or_y(1000000007, 100, 200) == 100
    assert x_or_y(1000000008, 100, 200) == 200

def test_x_or_y_zero_values():
    """Test case where x or y is zero."""
    assert x_or_y(7, 0, 10) == 0
    assert x_or_y(4, 10, 0) == 0
    assert x_or_y(2, 0, 0) == 0