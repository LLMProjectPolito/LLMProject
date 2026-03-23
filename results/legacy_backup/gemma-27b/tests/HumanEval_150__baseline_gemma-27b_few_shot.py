import pytest

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 5, 1) == 5
    assert x_or_y(5, 100, 1) == 100
    assert x_or_y(11, 2, 4) == 2
    assert x_or_y(13, 7, 9) == 7

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 3, 6) == 6
    assert x_or_y(8, 4, 8) == 8
    assert x_or_y(9, 1, 9) == 9
    assert x_or_y(10, 5, 10) == 10
    assert x_or_y(12, 6, 12) == 12
    assert x_or_y(14, 7, 14) == 14
    assert x_or_y(16, 8, 16) == 16

def test_x_or_y_one():
    assert x_or_y(1, 10, 20) == 20

def test_x_or_y_large_prime():
    assert x_or_y(7919, 1, 0) == 1

def test_x_or_y_large_not_prime():
    assert x_or_y(7920, 1, 0) == 0