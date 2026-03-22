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
    assert x_or_y(11, 1, 2) == 1
    assert x_or_y(13, 7, 8) == 7
    assert x_or_y(17, 9, 10) == 9
    assert x_or_y(19, 11, 12) == 11
    assert x_or_y(23, 13, 14) == 13
    assert x_or_y(29, 15, 16) == 15

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 3, 4) == 4
    assert x_or_y(8, 5, 6) == 6
    assert x_or_y(9, 7, 8) == 8
    assert x_or_y(10, 9, 10) == 10
    assert x_or_y(12, 11, 12) == 12
    assert x_or_y(14, 13, 14) == 14
    assert x_or_y(16, 15, 16) == 16
    assert x_or_y(18, 17, 18) == 18
    assert x_or_y(20, 19, 20) == 20

def test_x_or_y_edge_cases():
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(-1, 3, 4) == 4
    assert x_or_y(100, 100, 100) == 100

def test_x_or_y_large_numbers():
    assert x_or_y(1000000007, 1, 2) == 1  # Prime
    assert x_or_y(1000000008, 3, 4) == 4  # Not prime

def test_x_or_y_types():
    assert x_or_y(7, 34.5, 12.6) == 34.5
    assert x_or_y(15, 8.1, 5.2) == 5.2
    assert x_or_y(7, "hello", "world") == "hello"
    assert x_or_y(15, "foo", "bar") == "bar"