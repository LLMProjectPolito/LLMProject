
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

def test_x_or_y_prime_number():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 10, 20) == 10
    assert x_or_y(13, 5, 15) == 5
    assert x_or_y(2, 1, 2) == 1
    assert x_or_y(3, 1, 2) == 1

def test_x_or_y_not_prime_number():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(9, 1, 2) == 2
    assert x_or_y(10, 1, 2) == 2
    assert x_or_y(12, 1, 2) == 2
    assert x_or_y(14, 1, 2) == 2

def test_x_or_y_edge_cases():
    assert x_or_y(1, 1, 2) == 2
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(-1, 1, 2) == 2