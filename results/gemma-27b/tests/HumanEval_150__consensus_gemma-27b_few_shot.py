import pytest

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 5, 1) == 5
    assert x_or_y(5, 100, 1) == 100
    assert x_or_y(11, 1, 2) == 1
    assert x_or_y(13, 50, 10) == 50
    assert x_or_y(17, 1000, 1) == 1000
    assert x_or_y(19, 2, 3) == 2

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 5, 10) == 10
    assert x_or_y(8, 10, 1) == 1
    assert x_or_y(9, 20, 5) == 5
    assert x_or_y(10, 1, 100) == 100
    assert x_or_y(12, 5, 1) == 1
    assert x_or_y(14, 10, 20) == 20
    assert x_or_y(16, 1, 2) == 2
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(0, 1, 2) == 2