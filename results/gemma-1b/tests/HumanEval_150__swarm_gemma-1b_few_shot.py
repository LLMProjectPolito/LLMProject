
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
        for i in range(2, n):
            if n % i == 0:
                return n - 1
        return x
    else:
        return y

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
    assert x_or_y(13, 17, 23) == 23
    assert x_or_y(1, 2, 3) == 2
    assert x_or_y(2, 2, 2) == 2
    assert x_or_y(1, 1, 1) == 1
    assert x_or_y(1, 2, 1) == 1
    assert x_or_y(1, 3, 1) == 1
    assert x_or_y(1, 4, 1) == 1
    assert x_or_y(1, 5, 1) == 1
    assert x_or_y(1, 6, 1) == 1
    assert x_or_y(1, 7, 1) == 1
    assert x_or_y(1, 8, 1) == 1
    assert x_or_y(1, 9, 1) == 1
    assert x_or_y(1, 10, 1) == 1
    assert x_or_y(1, 11, 1) == 1
    assert x_or_y(1, 12, 1) == 1
    assert x_or_y(1, 13, 1) == 1
    assert x_or_y(1, 14, 1) == 1
    assert x_or_y(1, 15, 1) == 1
    assert x_or_y(1, 16, 1) == 1
    assert x_or_y(1, 17, 1) == 1
    assert x_or_y(1, 18, 1) == 1
    assert x_or_y(1, 19, 1) == 1
    assert x_or_y(1, 20, 1) == 1
    assert x_or_y(1, 21, 1) == 1
    assert x_or_y(1, 22, 1) == 1
    assert x_or_y(1, 23, 1) == 1
    assert x_or_y(1, 24, 1) == 1
    assert x_or_y(1, 25, 1) == 1
    assert x_or_y(1, 26, 1) == 1
    assert x_or_y(1, 27, 1) == 1
    assert x_or_y(1, 28, 1) == 1
    assert x_or_y(1, 29, 1) == 1
    assert x_or_y(1, 30, 1) == 1
    assert x_or_y(1, 31, 1) == 1
    assert x_or_y(1, 32, 1) == 1
    assert x_or_y(1, 33, 1) == 1
    assert x_or_y(1, 34, 1) == 1
    print("All tests passed")