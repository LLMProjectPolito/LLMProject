
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
    assert x_or_y(11, 5, 8) == 5
    assert x_or_y(13, 10, 20) == 10
    assert x_or_y(2, 1, 5) == 1
    assert x_or_y(3, 2, 3) == 2
    assert x_or_y(5, 4, 5) == 4
    assert x_or_y(7, 6, 7) == 6
    assert x_or_y(17, 1, 17) == 1
    assert x_or_y(1009, 34, 12) == 34
    assert x_or_y(1009, 5, 8) == 5

def test_x_or_y_not_prime_number():
    assert x_or_y(4, 34, 12) == 12
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(9, 10, 20) == 20
    assert x_or_y(1, 1, 5) == 5
    assert x_or_y(6, 34, 12) == 12
    assert x_or_y(10, 34, 12) == 12
    assert x_or_y(12, 34, 12) == 12
    assert x_or_y(16, 34, 12) == 12
    assert x_or_y(25, 34, 12) == 12
    assert x_or_y(27, 34, 12) == 12
    assert x_or_y(36, 34, 12) == 12
    assert x_or_y(49, 34, 12) == 12
    assert x_or_y(1000000007, 1, 2) == 1
    assert x_or_y(0, 34, 12) == 12
    assert x_or_y(0, 8, 5) == 5