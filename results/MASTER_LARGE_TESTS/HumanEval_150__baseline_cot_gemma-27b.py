import pytest

def test_x_or_y_prime_number():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 5, 8) == 5
    assert x_or_y(5, 1, 2) == 1
    assert x_or_y(11, 100, 200) == 100
    assert x_or_y(13, -5, 5) == -5
    assert x_or_y(17, 0, 1) == 0

def test_x_or_y_non_prime_number():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 10, 20) == 20
    assert x_or_y(8, 5, 10) == 10
    assert x_or_y(9, 100, 1) == 1
    assert x_or_y(10, -10, 10) == 10
    assert x_or_y(12, 0, -1) == -1

def test_x_or_y_edge_cases():
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(1, 1, 2) == 2
    assert x_or_y(2, 0, 0) == 0
    assert x_or_y(1, 0, 0) == 0

def test_x_or_y_large_numbers():
    assert x_or_y(101, 1000, 2000) == 1000  # 101 is prime
    assert x_or_y(100, 1000, 2000) == 2000  # 100 is not prime

def test_x_or_y_negative_n():
    assert x_or_y(-7, 1, 2) == 2 # Negative numbers are not prime
    assert x_or_y(-1, 1, 2) == 2