
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest
from your_module import x_or_y  # Replace your_module

def test_x_or_y_prime_number():
    """Test when n is a prime number."""
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 1, 5) == 1
    assert x_or_y(13, 2, 8) == 2
    assert x_or_y(17, 10, 1) == 10
    assert x_or_y(23, 5, 2) == 5

def test_x_or_y_not_prime_number():
    """Test when n is not a prime number."""
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(9, 1, 5) == 5
    assert x_or_y(10, 2, 8) == 8
    assert x_or_y(12, 10, 1) == 10
    assert x_or_y(14, 5, 2) == 2

def test_x_or_y_edge_cases():
    """Test edge cases like n=2 (prime) and n=1 (not prime)."""
    assert x_or_y(2, 34, 12) == 34
    assert x_or_y(1, 8, 5) == 5
    assert x_or_y(1, 1, 5) == 1
    assert x_or_y(1, 2, 8) == 8
    assert x_or_y(1, 5, 2) == 2

def test_x_or_y_large_numbers():
    """Test with larger numbers to check for potential overflow issues."""
    assert x_or_y(1000000007, 1000000, 500000) == 1000000
    assert x_or_y(1000000007, 1, 500000) == 500000

def test_x_or_y_zero_n():
    """Test when n is zero."""
    assert x_or_y(0, 34, 12) == 12
    assert x_or_y(0, 1, 5) == 5
    assert x_or_y(0, 2, 8) == 8
    assert x_or_y(0, 10, 1) == 10
    assert x_or_y(0, 5, 2) == 2