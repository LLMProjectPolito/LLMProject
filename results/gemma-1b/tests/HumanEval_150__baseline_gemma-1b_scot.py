
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
    return x

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(11, 11, 11) == 11
    assert x_or_y(13, 13, 13) == 13
    assert x_or_y(17, 17, 17) == 17
    assert x_or_y(2, 2, 2) == 2
    assert x_or_y(3, 3, 3) == 3
    assert x_or_y(4, 4, 4) == 4
    assert x_or_y(5, 5, 5) == 5
    assert x_or_y(6, 6, 6) == 6
    assert x_or_y(9, 9, 9) == 9
    assert x_or_y(10, 10, 10) == 10
    assert x_or_y(12, 12, 12) == 12
    assert x_or_y(13, 13, 13) == 13
    assert x_or_y(17, 17, 17) == 17
    assert x_or_y(2, 2, 2) == 2
    print("All test cases passed")

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(17, 17, 17) == 17
    assert x_or_y(2, 2, 2) == 2
    assert x_or_y(3, 3, 3) == 3
    assert x_or_y(4, 4, 4) == 4
    assert x_or_y(5, 5, 5) == 5
    assert x_or_y(6, 6, 6) == 6
    assert x_or_y(7, 7, 7) == 7
    assert x_or_y(8, 8, 8) == 8
    assert x_or_y(9, 9, 9) == 9
    assert x_or_y(10, 10, 10) == 10
    assert x_or_y(11, 11, 11) == 11
    assert x_or_y(12, 12, 12) == 12
    assert x_or_y(13, 13, 13) == 13
    assert x_or_y(14, 14, 14) == 14
    assert x_or_y(15, 15, 15) == 15
    print("All test cases passed")