
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 5, 7) == 5
    assert x_or_y(5, 1, 2) == 1
    assert x_or_y(11, 100, 200) == 100
    assert x_or_y(13, -5, 5) == -5
    assert x_or_y(17, 0, 1) == 0
    assert x_or_y(19, 10, 10) == 10
    assert x_or_y(23, 1000, 1) == 1000
    assert x_or_y(29, -1, -2) == -1

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 10, 20) == 20
    assert x_or_y(8, 5, 7) == 7
    assert x_or_y(9, 1, 2) == 2
    assert x_or_y(10, 100, 200) == 200
    assert x_or_y(12, -5, 5) == 5
    assert x_or_y(14, 0, 1) == 1
    assert x_or_y(16, 10, 10) == 10
    assert x_or_y(18, 1000, 1) == 1
    assert x_or_y(20, -1, -2) == -2
    assert x_or_y(1, 1, 2) == 2
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(21, 1, 2) == 2

def test_x_or_y_edge_cases():
    assert x_or_y(2, 0, 0) == 0
    assert x_or_y(4, 0, 0) == 0
    assert x_or_y(1, 1, 1) == 1
    assert x_or_y(2, 1, 1) == 1
    assert x_or_y(3, 1, 1) == 1
    assert x_or_y(4, 1, 1) == 1