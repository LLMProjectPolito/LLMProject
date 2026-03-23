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
    assert x_or_y(11, 99, 1) == 99
    assert x_or_y(13, 100, 0) == 100
    assert x_or_y(17, 1, 1) == 1
    assert x_or_y(19, 5, 5) == 5

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 5, 10) == 10
    assert x_or_y(8, 2, 4) == 4
    assert x_or_y(9, 3, 6) == 6
    assert x_or_y(10, 7, 8) == 8
    assert x_or_y(12, 11, 12) == 12
    assert x_or_y(14, 13, 14) == 14
    assert x_or_y(16, 15, 16) == 16
    assert x_or_y(1, 1, 1) == 1
    assert x_or_y(0, 1, 1) == 1

def test_x_or_y_large_numbers():
    assert x_or_y(101, 1000, 1) == 1000
    assert x_or_y(100, 1, 1000) == 1000
    assert x_or_y(97, 100, 1) == 100
    assert x_or_y(99, 1, 100) == 100

def test_x_or_y_negative_numbers():
    assert x_or_y(-7, -1, -2) == -1
    assert x_or_y(-15, -3, -4) == -4
    assert x_or_y(-1, -5, -6) == -6