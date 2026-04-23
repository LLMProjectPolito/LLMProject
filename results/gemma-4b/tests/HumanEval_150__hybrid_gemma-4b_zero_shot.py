
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
    else:
        return y

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 22, 1) == 22
    assert x_or_y(13, 100, 5) == 100
    assert x_or_y(17, 99, 6) == 99
    assert x_or_y(19, 88, 4) == 88
    assert x_or_y(23, 77, 3) == 77

def test_x_or_y_not_prime():
    assert x_or_y(4, 34, 12) == 12
    assert x_or_y(6, 8, 5) == 5
    assert x_or_y(8, 2, 9) == 9
    assert x_or_y(9, 10, 7) == 7
    assert x_or_y(10, 1, 2) == 2
    assert x_or_y(12, 3, 4) == 4

def test_x_or_y_edge_cases():
    assert x_or_y(1, 34, 12) == 12
    assert x_or_y(2, 34, 12) == 34
    assert x_or_y(3, 34, 12) == 34
    assert x_or_y(5, 34, 12) == 34
    assert x_or_y(100, 34, 12) == 12
    assert x_or_y(1000, 34, 12) == 12

def test_x_or_y_large_prime():
    assert x_or_y(997, 1000, 500) == 1000

def test_x_or_y_large_non_prime():
    assert x_or_y(1000, 1000, 500) == 500