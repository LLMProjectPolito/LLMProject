
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
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if (n % i) == 0:
                return y
        return x
    return y

def test_x_or_y_prime(n, x, y):
    assert x_or_y(n, x, y) == x

def test_x_or_y_not_prime(n, x, y):
    assert x_or_y(n, x, y) == y

def test_edge_cases():
    assert x_or_y(1, 34, 12) == 12
    assert x_or_y(0, 34, 12) == 12
    assert x_or_y(-1, 34, 12) == 12

def test_large_prime():
    assert x_or_y(7919, 100, 200) == 100

def test_large_non_prime():
    assert x_or_y(100, 100, 200) == 200

def test_x_equals_y():
    assert x_or_y(7, 7, 12) == 7
    assert x_or_y(15, 8, 8) == 8