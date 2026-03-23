import pytest
import math

def is_prime(n):
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
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if is_prime(n):
        return x
    else:
        return y

def test_x_or_y_edge_case_one():
    """Test when n is 1 (not prime)."""
    assert x_or_y(1, 10, 20) == 20

def test_x_or_y_prime():
    """Test when n is a prime number."""
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_not_prime():
    """Test when n is not a prime number."""
    assert x_or_y(15, 8, 5) == 5

def test_x_or_y_two():
    """Test when n is 2 (prime)."""
    assert x_or_y(2, 100, 200) == 100

def test_x_or_y_four():
    """Test when n is 4 (not prime)."""
    assert x_or_y(4, 50, 75) == 75