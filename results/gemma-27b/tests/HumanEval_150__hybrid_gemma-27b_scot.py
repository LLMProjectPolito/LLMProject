
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
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

def test_prime_number():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 100, 200) == 100
    assert x_or_y(2, 5, 10) == 5

def test_non_prime_number():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(9, 7, 3) == 3

def test_edge_case_zero():
    assert x_or_y(0, 1, 2) == 2

def test_edge_case_one():
    assert x_or_y(1, 3, 4) == 4

def test_edge_case_two():
    assert x_or_y(2, 5, 10) == 5

def test_negative_number():
    assert x_or_y(-5, 1, 2) == 2
    assert x_or_y(-1, 7, 8) == 8

def test_large_prime():
    assert x_or_y(7919, 10, 20) == 10

def test_large_non_prime():
    assert x_or_y(7920, 30, 40) == 40