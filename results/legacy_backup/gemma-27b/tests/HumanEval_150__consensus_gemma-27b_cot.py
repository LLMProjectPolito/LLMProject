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
    assert x_or_y(13, 50, 10) == 50
    assert x_or_y(17, 1000, 1) == 1000
    assert x_or_y(19, 2, 4) == 2
    assert x_or_y(13, 99, 1) == 99
    assert x_or_y(17, 50, 25) == 50
    assert x_or_y(19, 10, 5) == 10
    assert x_or_y(23, 1000, 1) == 1000
    assert x_or_y(29, 2, 4) == 2

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 10, 5) == 5
    assert x_or_y(8, 20, 10) == 10
    assert x_or_y(9, 3, 1) == 1
    assert x_or_y(10, 5, 2) == 2
    assert x_or_y(12, 100, 1) == 1
    assert x_or_y(14, 2, 4) == 4
    assert x_or_y(16, 1, 2) == 2
    assert x_or_y(10, 100, 200) == 200
    assert x_or_y(12, 1, 2) == 2
    assert x_or_y(14, 99, 1) == 1
    assert x_or_y(16, 50, 25) == 25
    assert x_or_y(18, 10, 5) == 5
    assert x_or_y(20, 1000, 1) == 1
    assert x_or_y(21, 2, 4) == 4

def test_x_or_y_edge_cases():
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(-1, 1, 2) == 2
    assert x_or_y(100, 1, 2) == 2
    assert x_or_y(101, 1, 2) == 1

def test_x_or_y_large_numbers():
    assert x_or_y(1000000007, 100, 200) == 100  # Prime
    assert x_or_y(1000000008, 100, 200) == 200  # Not prime

def test_x_or_y_same_values():
    assert x_or_y(7, 5, 5) == 5
    assert x_or_y(15, 5, 5) == 5

def test_x_or_y_negative_values():
    assert x_or_y(7, -34, 12) == -34
    assert x_or_y(15, 8, -5) == -5
    assert x_or_y(7, -34, -12) == -34
    assert x_or_y(15, -8, -5) == -5

def test_x_or_y_types():
    assert x_or_y(7, 34.5, 12) == 34.5
    assert x_or_y(15, 8, 5.5) == 5.5
    assert x_or_y(7, "hello", "world") == "hello"
    assert x_or_y(15, "a", "b") == "b"
    assert x_or_y(7, 34, "world") == 34
    assert x_or_y(15, 8, "b") == "b"