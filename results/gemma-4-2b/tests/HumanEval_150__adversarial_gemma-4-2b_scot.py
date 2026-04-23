
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


def test_prime_n_returns_x():
    assert x_or_y(7, 34, 12) == 34

def test_non_prime_n_returns_y():
    assert x_or_y(15, 8, 5) == 5

def test_small_prime_n():
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 10, 20) == 10
    assert x_or_y(5, 10, 20) == 10
    assert x_or_y(7, 10, 20) == 10

def test_small_non_prime_n():
    assert x_or_y(4, 10, 20) == 20
    assert x_or_y(6, 10, 20) == 20
    assert x_or_y(8, 10, 20) == 20
    assert x_or_y(9, 10, 20) == 20
    assert x_or_y(10, 10, 20) == 20

def test_zero_n():
    assert x_or_y(0, 10, 20) == 20

def test_negative_n():
    assert x_or_y(-1, 10, 20) == 20

def test_zero_x():
    assert x_or_y(7, 0, 12) == 12

def test_zero_y():
    assert x_or_y(7, 34, 0) == 0

def test_negative_x():
    assert x_or_y(-7, 0, 12) == 12

def test_negative_y():
    assert x_or_y(7, -34, 0) == 0

def test_large_prime_n():
    assert x_or_y(1009, 10, 20) == 10

def test_large_non_prime_n():
    assert x_or_y(1000, 10, 20) == 20