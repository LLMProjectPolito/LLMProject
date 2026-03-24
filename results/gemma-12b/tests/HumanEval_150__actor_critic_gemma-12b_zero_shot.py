
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
    Negative numbers are treated as non-prime.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

def test_prime_number():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 100, 200) == 100
    assert x_or_y(5, 50, 60) == 50
    assert x_or_y(11, 70, 80) == 70
    assert x_or_y(13, 1, 2) == 1
    assert x_or_y(1000000007, 100, 200) == 100

def test_non_prime_number():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 20, 30) == 30
    assert x_or_y(6, 10, 15) == 15
    assert x_or_y(8, 40, 50) == 50
    assert x_or_y(9, 1000, 2000) == 2000
    assert x_or_y(1, 3, 4) == 4

def test_zero_or_negative_input():
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(-1, 5, 6) == 6
    assert x_or_y(-7, 10, 20) == 20

def test_large_numbers():
    assert x_or_y(1000000008, 100, 200) == 200