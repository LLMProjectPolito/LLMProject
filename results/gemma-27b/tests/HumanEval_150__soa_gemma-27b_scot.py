
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
    assert x_or_y(11, 99, 1) == 99
    assert x_or_y(13, 100, 0) == 100
    assert x_or_y(17, 1, 1) == 1
    assert x_or_y(19, 2, 2) == 2

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 3, 4) == 4
    assert x_or_y(8, 5, 6) == 6
    assert x_or_y(9, 7, 8) == 8
    assert x_or_y(10, 10, 11) == 11
    assert x_or_y(12, 12, 13) == 13
    assert x_or_y(14, 14, 15) == 15
    assert x_or_y(16, 16, 17) == 17
    assert x_or_y(1, 1, 2) == 2
    assert x_or_y(0, 1, 2) == 2

def test_x_or_y_edge_cases():
    assert x_or_y(2, 0, 0) == 0
    assert x_or_y(1, 0, 0) == 0
    assert x_or_y(2, -1, 1) == -1
    assert x_or_y(1, -1, 1) == 1
    assert x_or_y(100, -1, -2) == -2
    assert x_or_y(101, -1, -2) == -1