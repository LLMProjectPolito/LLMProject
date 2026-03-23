import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if is_prime(n):
        return x
    else:
        return y

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 22, 1) == 22
    assert x_or_y(13, 100, 5) == 100
    assert x_or_y(17, 99, 1) == 99
    assert x_or_y(19, 88, 2) == 88

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(20, 1, 7) == 1
    assert x_or_y(21, 3, 9) == 3
    assert x_or_y(22, 4, 6) == 4
    assert x_or_y(25, 2, 8) == 2

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