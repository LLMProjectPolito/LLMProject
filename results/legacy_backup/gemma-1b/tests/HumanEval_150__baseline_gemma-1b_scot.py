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

def test_x_or_y_non_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(16, 16, 16) == 16
    assert x_or_y(20, 10, 10) == 10
    assert x_or_y(21, 21, 21) == 21
    assert x_or_y(22, 22, 22) == 22
    assert x_or_y(23, 23, 23) == 23
    assert x_or_y(24, 24, 24) == 24
    assert x_or_y(25, 25, 25) == 25
    assert x_or_y(26, 26, 26) == 26
    assert x_or_y(27, 27, 27) == 27
    assert x_or_y(30, 15, 15) == 15
    assert x_or_y(31, 31, 31) == 31
    assert x_or_y(32, 32, 32) == 32
    assert x_or_y(33, 33, 33) == 33
    assert x_or_y(34, 34, 34) == 34
    assert x_or_y(35, 35, 35) == 35
    assert x_or_y(36, 36, 36) == 36
    assert x_or_y(37, 37, 37) == 37
    assert x_or_y(38, 38, 38) == 38
    assert x_or_y(40, 10, 10) == 10
    print("All test cases passed")