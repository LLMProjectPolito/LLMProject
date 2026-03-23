import pytest

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(5, 50, 60) == 50
    assert x_or_y(11, 100, 200) == 100
    assert x_or_y(13, 7, 9) == 7

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(4, 50, 60) == 60
    assert x_or_y(6, 100, 200) == 200
    assert x_or_y(8, 7, 9) == 9
    assert x_or_y(9, 1, 2) == 2
    assert x_or_y(10, 3, 4) == 4

def test_x_or_y_negative_n():
    assert x_or_y(-1, 10, 20) == 20
    assert x_or_y(-2, 5, 6) == 6
    assert x_or_y(-5, 7, 8) == 8

def test_x_or_y_zero_n():
    assert x_or_y(0, 10, 20) == 20

def test_x_or_y_large_prime():
    assert x_or_y(101, 1, 2) == 1

def test_x_or_y_large_non_prime():
    assert x_or_y(1000, 1, 2) == 2

def test_x_or_y_equal_x_y():
    assert x_or_y(7, 5, 5) == 5
    assert x_or_y(8, 5, 5) == 5

def test_x_or_y_type_hints():
    assert x_or_y(7, 34.5, 12) == 34.5
    assert x_or_y(7, "hello", "world") == "hello"
    assert x_or_y(7, 34, "world") == 34
    assert x_or_y(8, "hello", 12) == 12