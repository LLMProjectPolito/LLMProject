
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
    >>> x_or_y(7, 34, 12)
    34
    >>> x_or_y(15, 8, 5)
    5
    
    """
    if n <= 1:
        return y
    if n < 0:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 100, 200) == 100
    assert x_or_y(5, 1, 0) == 1
    assert x_or_y(-7, 1, 2) == 2  # Test for negative number (not prime)
    assert x_or_y(7919, 10, 11) == 10 # Large prime

def test_x_or_y_composite():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 10, 20) == 20
    assert x_or_y(9, 50, 60) == 60

def test_x_or_y_edge_cases():
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(1, 3, 4) == 4
    assert x_or_y(2, 5, 6) == 5

def test_x_or_y_negative():
    assert x_or_y(-5, 7, 8) == 8
    assert x_or_y(-1, 9, 10) == 10

def test_x_or_y_large_prime():
    assert x_or_y(104729, 1000, 2000) == 1000