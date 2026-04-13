
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

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5

def test_x_or_y_one():
    assert x_or_y(1, 34, 12) == 12

def test_x_or_y_two():
    assert x_or_y(2, 34, 12) == 34

def test_x_or_y_large_prime():
    assert x_or_y(17, 20, 10) == 20

def test_x_or_y_large_not_prime():
    assert x_or_y(16, 20, 10) == 10

def test_x_or_y_edge_case_prime():
    assert x_or_y(3, 10, 20) == 10

def test_x_or_y_edge_case_not_prime():
    assert x_or_y(4, 10, 20) == 20