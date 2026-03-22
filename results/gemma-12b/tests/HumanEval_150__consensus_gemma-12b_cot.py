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
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 3, 4) == 4
    assert x_or_y(8, 10, 15) == 15
    assert x_or_y(9, 20, 30) == 30
    assert x_or_y(10, 5, 10) == 10

def test_x_or_y_edge_cases():
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(0, 5, 10) == 10
    assert x_or_y(-1, 1, 2) == 2
    assert x_or_y(-2, 3, 4) == 4

def test_x_or_y_same_values():
    assert x_or_y(7, 5, 5) == 5
    assert x_or_y(4, 10, 10) == 10

def test_x_or_y_negative_numbers():
    assert x_or_y(-5, 1, 2) == 2
    assert x_or_y(5, -1, -2) == -1
    assert x_or_y(-7, -34, -12) == -34

def test_x_or_y_large_numbers():
    assert x_or_y(1000000007, 100, 200) == 100
    assert x_or_y(1000000008, 100, 200) == 200