
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

def test_x_or_y_prime_n1():
    assert x_or_y(1, 34, 12) == 12

def test_x_or_y_prime_n2():
    assert x_or_y(2, 34, 12) == 34

def test_x_or_y_prime_n3():
    assert x_or_y(3, 34, 12) == 34

def test_x_or_y_prime_n5():
    assert x_or_y(5, 34, 12) == 34

def test_x_or_y_prime_n7():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_prime_n11():
    assert x_or_y(11, 34, 12) == 34

def test_x_or_y_non_prime_n1():
    assert x_or_y(1, 8, 5) == 5

def test_x_or_y_non_prime_n4():
    assert x_or_y(4, 8, 5) == 5

def test_x_or_y_non_prime_n6():
    assert x_or_y(6, 8, 5) == 5

def test_x_or_y_non_prime_n8():
    assert x_or_y(8, 8, 5) == 5

def test_x_or_y_x_equals_y():
    assert x_or_y(4, 8, 8) == 8

def test_x_or_y_n_greater_than_10():
    assert x_or_y(13, 34, 12) == 34