
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

    The function treats 0 and 1 as non-prime.

    Examples:
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    
    """
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

def test_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 5, 1) == 5
    assert x_or_y(5, 100, 1) == 100
    assert x_or_y(11, 1, 2) == 1
    assert x_or_y(13, 99, 0) == 99
    assert x_or_y(7919, 1, 2) == 1  # Larger prime number
    assert x_or_y(101, 5, 6) == 5

def test_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 3, 4) == 4
    assert x_or_y(8, 7, 6) == 6
    assert x_or_y(9, 10, 11) == 11
    assert x_or_y(10, 12, 13) == 13
    assert x_or_y(100, 1, 2) == 2 # Larger non-prime

def test_edge_cases_zero():
    assert x_or_y(0, 1, 2) == 2  # 0 is not prime
    assert x_or_y(2, 0, 0) == 0
    assert x_or_y(4, 0, 0) == 0

def test_edge_cases_one():
    assert x_or_y(1, 1, 2) == 2  # 1 is not prime

def test_zero_values():
    assert x_or_y(2, 0, 1) == 0 # n is prime, x is zero
    assert x_or_y(4, 0, 1) == 1 # n is not prime, x is zero
    assert x_or_y(2, 1, 0) == 1 # n is prime, y is zero
    assert x_or_y(4, 1, 0) == 0 # n is not prime, y is zero