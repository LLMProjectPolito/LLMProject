
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
    if n <= 1:
        return None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return None
    if n == x or n == y:
        return x
    else:
        return y

def test_x_or_y():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(1, 2, 3) == 2
    assert x_or_y(1, 3, 2) == 3
    assert x_or_y(2, 2, 2) == 2
    assert x_or_y(3, 3, 3) == 3
    assert x_or_y(4, 2, 1) == 1
    assert x_or_y(5, 5, 5) == 5
    assert x_or_y(6, 3, 2) == 2
    assert x_or_y(7, 7, 7) == 7
    assert x_or_y(8, 2, 1) == 1
    assert x_or_y(9, 3, 1) == 1
    assert x_or_y(10, 5, 2) == 2
    assert x_or_y(11, 7, 1) == 1
    assert x_or_y(12, 3, 4) == 4