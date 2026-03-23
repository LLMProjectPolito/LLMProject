import pytest

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 5, 1) == 5
    assert x_or_y(5, 100, 200) == 100
    assert x_or_y(11, 1, 0) == 1
    assert x_or_y(13, -1, -2) == -1
    assert x_or_y(17, 0, 0) == 0
    assert x_or_y(19, 10, -10) == 10
    assert x_or_y(23, -5, 5) == -5
    assert x_or_y(29, 1000, 1) == 1000

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 3, 6) == 6
    assert x_or_y(8, 7, 8) == 8
    assert x_or_y(9, 9, 10) == 10
    assert x_or_y(10, 11, 12) == 12
    assert x_or_y(12, 13, 14) == 14
    assert x_or_y(14, 15, 16) == 16
    assert x_or_y(16, 17, 18) == 18
    assert x_or_y(18, 19, 20) == 20
    assert x_or_y(20, 21, 22) == 22
    assert x_or_y(1, 1, 2) == 2
    assert x_or_y(0, 1, 2) == 2

def test_x_or_y_edge_cases():
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(0, 5, 10) == 10
    assert x_or_y(21, 1, 1) == 1
    assert x_or_y(25, 5, 5) == 5
    assert x_or_y(29, 10, 0) == 10
    assert x_or_y(30, 0, 10) == 10
    assert x_or_y(2, 0, 0) == 0
    assert x_or_y(2, -1, -2) == -1
    assert x_or_y(4, -1, -2) == -2
    assert x_or_y(1, 1, 1) == 1
    assert x_or_y(1, -1, -1) == -1