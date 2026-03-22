import pytest

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 5, 1) == 5
    assert x_or_y(5, 100, 1) == 100
    assert x_or_y(11, 1, 2) == 1
    assert x_or_y(13, 50, 10) == 50

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 10, 5) == 5
    assert x_or_y(8, 20, 1) == 1
    assert x_or_y(9, 100, 50) == 50
    assert x_or_y(10, 1, 10) == 10

def test_x_or_y_one():
    assert x_or_y(1, 10, 20) == 20

def test_x_or_y_large_prime():
    assert x_or_y(7919, 1, 2) == 1

def test_x_or_y_large_not_prime():
    assert x_or_y(7920, 1, 2) == 2