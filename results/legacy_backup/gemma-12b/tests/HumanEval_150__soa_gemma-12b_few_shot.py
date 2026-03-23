import pytest

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 5, 10) == 5
    assert x_or_y(11, 100, 200) == 100
    assert x_or_y(17, -5, 0) == -5

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(9, 10, 20) == 20
    assert x_or_y(10, 0, -1) == -1

def test_x_or_y_edge_cases():
    assert x_or_y(1, 5, 10) == 10
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(-1, 3, 4) == 4
    assert x_or_y(23, 1000, 1) == 1000
    assert x_or_y(29, -10, 5) == -10