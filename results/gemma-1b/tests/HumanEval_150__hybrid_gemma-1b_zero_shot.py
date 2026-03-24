
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def x_or_y(n, x, y):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return i
    return x

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(2, 3, 5) == 5
    assert x_or_y(3, 3, 5) == 3
    assert x_or_y(5, 5, 5) == 5
    assert x_or_y(11, 11, 11) == 11
    assert x_or_y(13, 13, 13) == 13
    assert x_or_y(17, 17, 17) == 17
    assert x_or_y(19, 19, 19) == 19
    assert x_or_y(23, 23, 23) == 23
    assert x_or_y(29, 29, 29) == 29
    assert x_or_y(31, 31, 31) == 31
    assert x_or_y(37, 37, 37) == 37
    assert x_or_y(41, 41, 41) == 41
    assert x_or_y(43, 43, 43) == 43
    assert x_or_y(47, 47, 47) == 47
    assert x_or_y(53, 53, 53) == 53
    assert x_or_y(59, 59, 59) == 59
    assert x_or_y(61, 61, 61) == 61
    assert x_or_y(67, 67, 67) == 67
    assert x_or_y(71, 71, 71) == 71
    assert x_or_y(73, 73, 73) == 73
    assert x_or_y(79, 79, 79) == 79
    assert x_or_y(83, 83, 83) == 83
    assert x_or_y(89, 89, 89) == 89
    print("All tests passed")