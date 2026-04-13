
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

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 5, 1) == 5
    assert x_or_y(5, 100, 200) == 100
    assert x_or_y(11, 1, 2) == 1
    assert x_or_y(13, -5, 10) == -5
    assert x_or_y(17, 0, 1) == 0
    assert x_or_y(19, 10, -10) == 10

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 10, 5) == 5
    assert x_or_y(8, 20, 10) == 10
    assert x_or_y(9, 5, 1) == 1
    assert x_or_y(10, -1, -2) == -2
    assert x_or_y(12, 0, 1) == 1
    assert x_or_y(14, 10, -10) == -10

def test_x_or_y_edge_cases():
    assert x_or_y(1, 10, 20) == 20  # 1 is not prime
    assert x_or_y(2, 10, 20) == 10  # 2 is prime
    assert x_or_y(0, 10, 20) == 20  # 0 is not prime
    assert x_or_y(-1, 10, 20) == 20 # negative number is not prime
    assert x_or_y(100, 10, 20) == 20
    assert x_or_y(97, 5, 1) == 5 # large prime
    assert x_or_y(99, 5, 1) == 1 # large non-prime

def test_x_or_y_types():
    assert x_or_y(7, 34.5, 12) == 34.5
    assert x_or_y(15, 8, 5.5) == 5.5
    assert x_or_y(7, "hello", "world") == "hello"
    assert x_or_y(15, "a", "b") == "b"
    assert x_or_y(7, 10, "world") == 10
    assert x_or_y(15, "hello", 5) == 5