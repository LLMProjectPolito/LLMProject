import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if (n % i) == 0:
            return y
    return x

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 5, 10) == 5
    assert x_or_y(13, 20, 1) == 20
    assert x_or_y(17, 100, 5) == 100

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(20, 1, 9) == 9
    assert x_or_y(21, 7, 2) == 2
    assert x_or_y(25, 3, 4) == 4

def test_x_or_y_edge_cases():
    assert x_or_y(1, 34, 12) == 12
    assert x_or_y(2, 34, 12) == 34
    assert x_or_y(3, 34, 12) == 34
    assert x_or_y(4, 34, 12) == 12
    assert x_or_y(5, 34, 12) == 34
    assert x_or_y(6, 34, 12) == 12
    assert x_or_y(8, 34, 12) == 12
    assert x_or_y(9, 34, 12) == 12
    assert x_or_y(10, 34, 12) == 12