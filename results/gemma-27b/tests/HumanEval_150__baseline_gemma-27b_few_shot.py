
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 5, 1) == 5
    assert x_or_y(5, 100, 1) == 100
    assert x_or_y(11, 2, 3) == 2
    assert x_or_y(13, 4, 5) == 4
    assert x_or_y(17, 6, 7) == 6
    assert x_or_y(19, 8, 9) == 8

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 3, 4) == 4
    assert x_or_y(8, 5, 6) == 6
    assert x_or_y(9, 7, 8) == 8
    assert x_or_y(10, 9, 10) == 10
    assert x_or_y(12, 11, 12) == 12
    assert x_or_y(14, 13, 14) == 14
    assert x_or_y(16, 15, 16) == 16
    assert x_or_y(1, 17, 18) == 18
    assert x_or_y(0, 19, 20) == 20