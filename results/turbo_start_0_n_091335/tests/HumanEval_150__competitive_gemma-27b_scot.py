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
    assert x_or_y(3, 5, 7) == 5
    assert x_or_y(5, 1, 2) == 1
    assert x_or_y(11, 100, 200) == 100
    assert x_or_y(13, 50, 60) == 50
    assert x_or_y(17, 10, 11) == 10
    assert x_or_y(19, 1000, 1001) == 1000
    assert x_or_y(23, 1, 0) == 1
    assert x_or_y(29, 2, 3) == 2

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 10, 20) == 20
    assert x_or_y(8, 5, 7) == 7
    assert x_or_y(9, 1, 2) == 2
    assert x_or_y(10, 100, 200) == 200
    assert x_or_y(12, 50, 60) == 60
    assert x_or_y(14, 10, 11) == 11
    assert x_or_y(16, 1000, 1001) == 1001
    assert x_or_y(18, 1, 0) == 0
    assert x_or_y(20, 2, 3) == 3
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(0, 10, 20) == 20
    assert x_or_y(-1, 10, 20) == 20
    assert x_or_y(-2, 10, 20) == 20