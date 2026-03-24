
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest
import math

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
                return n
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
        return 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n

def test_x_or_y():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(1, 2, 3) == 2
    assert x_or_y(2, 2, 2) == 2
    assert x_or_y(3, 3, 3) == 3
    assert x_or_y(4, 4, 4) == 4
    assert x_or_y(5, 5, 5) == 5
    assert x_or_y(6, 6, 6) == 6
    assert x_or_y(7, 7, 7) == 7
    assert x_or_y(8, 8, 8) == 8
    assert x_or_y(9, 9, 9) == 9
    assert x_or_y(10, 10, 10) == 10
    assert x_or_y(11, 11, 11) == 11
    assert x_or_y(12, 12, 12) == 12
    assert x_or_y(13, 13, 13) == 13
    assert x_or_y(14, 14, 14) == 14
    assert x_or_y(15, 15, 15) == 15
    assert x_or_y(16, 16, 16) == 16
    assert x_or_y(17, 17, 17) == 17
    assert x_or_y(18, 18, 18) == 18
    assert x_or_y(19, 19, 19) == 19
    assert x_or_y(20, 20, 20) == 20