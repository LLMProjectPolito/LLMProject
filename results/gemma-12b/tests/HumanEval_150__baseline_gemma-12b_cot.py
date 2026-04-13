
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
    assert x_or_y(6, 1, 2) == 2
    assert x_or_y(9, 100, 200) == 200
    assert x_or_y(10, 5, 10) == 10

def test_x_or_y_n_is_1():
    """Test case where n is 1 (not prime)."""
    assert x_or_y(1, 5, 10) == 10

def test_x_or_y_n_is_0():
    """Test case where n is 0 (not prime)."""
    assert x_or_y(0, 5, 10) == 10

def test_x_or_y_x_equals_y():
    """Test case where x and y are equal."""
    assert x_or_y(7, 5, 5) == 5
    assert x_or_y(4, 5, 5) == 5

def test_x_or_y_negative_n():
    """Test case where n is negative (not prime)."""
    assert x_or_y(-5, 1, 2) == 2

def test_x_or_y_large_prime():
    """Test case with a large prime number."""
    assert x_or_y(997, 100, 200) == 100

def test_x_or_y_large_non_prime():
    """Test case with a large non-prime number."""
    assert x_or_y(1000, 100, 200) == 200