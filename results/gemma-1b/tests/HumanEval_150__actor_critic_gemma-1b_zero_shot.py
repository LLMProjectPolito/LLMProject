
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
        for i in range(2, n):
            if n % i == 0:
                return i
    return y

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_simple():
    assert x_or_y(15, 8, 5) == 5

def test_x_or_y_edge_case_small():
    assert x_or_y(2, 3, 5) == 3

def test_x_or_y_edge_case_large():
    assert x_or_y(100, 2, 5) == 5

def test_x_or_y_edge_case_prime_and_small():
    assert x_or_y(7, 2, 5) == 5

def test_x_or_y_edge_case_prime_and_large():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_no_prime():
    assert x_or_y(4, 2, 5) == 5

def test_x_or_y_one_prime():
    assert x_or_y(3, 3, 5) == 5

def test_x_or_y_one_prime_and_small():
    assert x_or_y(3, 2, 5) == 5