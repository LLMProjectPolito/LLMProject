
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

import pytest

def test_x_or_y_prime_n():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(13, 8, 5) == 8
    assert x_or_y(2, 34, 12) == 34
    assert x_or_y(3, 34, 12) == 34
    assert x_or_y(5, 34, 12) == 34
    assert x_or_y(17, 8, 5) == 8
    assert x_or_y(23, 8, 5) == 8
    assert x_or_y(29, 8, 5) == 8

def test_x_or_y_not_prime_n():
    assert x_or_y(4, 34, 12) == 12
    assert x_or_y(6, 34, 12) == 12
    assert x_or_y(8, 34, 12) == 12
    assert x_or_y(9, 34, 12) == 12
    assert x_or_y(10, 34, 12) == 12
    assert x_or_y(12, 34, 12) == 12
    assert x_or_y(14, 34, 12) == 12
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(16, 8, 5) == 5
    assert x_or_y(18, 8, 5) == 5
    assert x_or_y(20, 8, 5) == 5
    assert x_or_y(21, 8, 5) == 5
    assert x_or_y(22, 8, 5) == 5
    assert x_or_y(24, 8, 5) == 5
    assert x_or_y(25, 8, 5) == 5
    assert x_or_y(26, 8, 5) == 5
    assert x_or_y(27, 8, 5) == 5
    assert x_or_y(28, 8, 5) == 5
    assert x_or_y(30, 8, 5) == 5

def test_x_or_y_edge_cases():
    assert x_or_y(1, 34, 12) == 12
    assert x_or_y(0, 34, 12) == 12
    assert x_or_y(-1, 34, 12) == 12