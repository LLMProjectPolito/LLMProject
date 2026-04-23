
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest
from your_module import x_or_y  # Replace your_module

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_x_or_y_prime():
    """Test cases where n is a prime number."""
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 100, 200) == 100
    assert x_or_y(5, 50, 60) == 50
    assert x_or_y(11, 1, 2) == 1
    assert x_or_y(13, "a", "b") == "a"
    assert x_or_y(17, 17, 17) == 17

def test_x_or_y_not_prime():
    """Test cases where n is not a prime number."""
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 20, 30) == 30
    assert x_or_y(6, 10, 20) == 20
    assert x_or_y(8, 30, 40) == 40
    assert x_or_y(9, "x", "y") == "y"
    assert x_or_y(10, 100, 200) == 200

def test_x_or_y_edge_cases():
    """Test cases for edge cases like 0, 1, and negative numbers."""
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(1, 3, 4) == 4
    assert x_or_y(-5, 5, 6) == 6
    assert x_or_y(-2, -1, 0) == 0

def test_x_or_y_with_different_types():
    """Test cases with different data types for x and y."""
    assert x_or_y(7, 3.14, 2.71) == 3.14
    assert x_or_y(10, [1, 2], (3, 4)) == (3, 4)
    assert x_or_y(11, True, False) == True
    assert x_or_y(12, None, "hello") == "hello"

def test_x_or_y_large_numbers():
    """Test cases with large numbers to ensure no overflow issues."""
    assert x_or_y(997, 1000000, 2000000) == 1000000
    assert x_or_y(1000, 1000000, 2000000) == 2000000

def test_x_or_y_prime_n_equal_x():
    """Test when n is prime and equal to x."""
    assert x_or_y(5, 5, 10) == 5

def test_x_or_y_not_prime_n_equal_y():
    """Test when n is not prime and equal to y."""
    assert x_or_y(4, 10, 4) == 4