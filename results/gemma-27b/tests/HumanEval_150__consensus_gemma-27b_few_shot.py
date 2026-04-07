
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
    assert x_or_y(3, 5, 1) == 5
    assert x_or_y(5, 100, 200) == 100
    assert x_or_y(11, 1, 0) == 1
    assert x_or_y(13, -1, -2) == -1
    assert x_or_y(17, 0, 0) == 0
    assert x_or_y(19, 10, -10) == 10
    assert x_or_y(23, 2, 4) == 2
    assert x_or_y(29, 5, 10) == 5

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 3, 6) == 6
    assert x_or_y(8, 7, 8) == 8
    assert x_or_y(9, 9, 10) == 10
    assert x_or_y(10, 11, 12) == 12
    assert x_or_y(12, 13, 14) == 14
    assert x_or_y(14, 15, 16) == 16
    assert x_or_y(16, 17, 18) == 18
    assert x_or_y(21, 22, 23) == 23
    assert x_or_y(6, 10, 5) == 5
    assert x_or_y(8, 20, 1) == 1
    assert x_or_y(10, 100, 0) == 0
    assert x_or_y(12, 1, 2) == 2
    assert x_or_y(14, -5, 10) == 10
    assert x_or_y(16, 0, 0) == 0
    assert x_or_y(18, 1000, 1) == 1
    assert x_or_y(20, 2, 4) == 4
    assert x_or_y(21, 5, 10) == 10
    assert x_or_y(22, 10, 5) == 5
    assert x_or_y(24, 1, 2) == 2
    assert x_or_y(25, 5, 10) == 10

def test_x_or_y_edge_cases():
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(0, 10, 20) == 20
    assert x_or_y(-1, 10, 20) == 20
    assert x_or_y(2, 0, 0) == 0
    assert x_or_y(4, 0, 0) == 0
    assert x_or_y(1, 0, 0) == 0
    assert x_or_y(1, 1, 2) == 2
    assert x_or_y(0, 5, 1) == 1
    assert x_or_y(2, -1, -2) == -1
    assert x_or_y(4, -1, -2) == -2
    assert x_or_y(1, -1, -2) == -2
    assert x_or_y(0, -1, -2) == -2
    assert x_or_y(-1, -1, -2) == -2