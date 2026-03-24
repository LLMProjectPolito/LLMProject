
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n < 2:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 5, 1) == 5
    assert x_or_y(5, 100, 1) == 100
    assert x_or_y(11, 1, 2) == 1
    assert x_or_y(13, 99, 0) == 99

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 3, 4) == 4
    assert x_or_y(8, 7, 6) == 6
    assert x_or_y(9, 10, 11) == 11
    assert x_or_y(10, 12, 13) == 13
    assert x_or_y(12, 14, 15) == 15

def test_x_or_y_edge_cases():
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(1, 3, 4) == 4
    assert x_or_y(2, 5, 6) == 5
    assert x_or_y(-1, 7, 8) == 8 # Negative numbers are not prime
    assert x_or_y(-5, 9, 10) == 10 # Negative numbers are not prime
    assert x_or_y(100, 1000, 1) == 1
    assert x_or_y(101, 1000, 1) == 1000 # Test a larger prime