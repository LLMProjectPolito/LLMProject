
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
    if n == 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if (n % i) == 0:
            return y
    return x

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 5, 10) == 5
    assert x_or_y(13, 20, 1) == 20
    assert x_or_y(17, 100, 5) == 100
    assert x_or_y(19, 1, 2) == 1

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(20, 10, 2) == 2
    assert x_or_y(21, 7, 9) == 9
    assert x_or_y(25, 4, 6) == 6
    assert x_or_y(28, 3, 4) == 4

def test_x_or_y_edge_cases():
    assert x_or_y(1, 34, 12) == 12
    assert x_or_y(2, 34, 12) == 34
    assert x_or_y(3, 34, 12) == 34
    assert x_or_y(4, 34, 12) == 12
    assert x_or_y(5, 34, 12) == 34
    assert x_or_y(6, 34, 12) == 12
    assert x_or_y(8, 34, 12) == 12
    assert x_or_y(9, 34, 12) == 12
    assert x_or_y(10, 34, 12) == 12
    assert x_or_y(12, 34, 12) == 34
    assert x_or_y(14, 34, 12) == 12
    assert x_or_y(16, 34, 12) == 12
    assert x_or_y(18, 34, 12) == 12
    assert x_or_y(20, 34, 12) == 12
    assert x_or_y(22, 34, 12) == 12
    assert x_or_y(24, 34, 12) == 12
    assert x_or_y(26, 34, 12) == 12
    assert x_or_y(27, 34, 12) == 12
    assert x_or_y(28, 34, 12) == 12
    assert x_or_y(30, 34, 12) == 12
    assert x_or_y(32, 34, 12) == 12
    assert x_or_y(33, 34, 12) == 12
    assert x_or_y(34, 34, 12) == 34
    assert x_or_y(35, 34, 12) == 12
    assert x_or_y(36, 34, 12) == 12
    assert x_or_y(38, 34, 12) == 12
    assert x_or_y(39, 34, 12) == 12
    assert x_or_y(40, 34, 12) == 12
    assert x_or_y(42, 34, 12) == 12
    assert x_or_y(44, 34, 12) == 12
    assert x_or_y(45, 34, 12) == 12
    assert x_or_y(46, 34, 12) == 12
    assert x_or_y(48, 34, 12) == 12
    assert x_or_y(49, 34, 12) == 34
    assert x_or_y(50, 34, 12) == 12