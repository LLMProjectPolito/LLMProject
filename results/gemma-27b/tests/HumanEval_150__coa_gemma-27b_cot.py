import pytest
import math


# Focus: Prime Number Determination
import pytest

def test_prime_number_returns_x():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 100, 50) == 100
    assert x_or_y(3, 200, 100) == 200
    assert x_or_y(5, 1, 0) == 1
    assert x_or_y(11, 99, 1) == 99

def test_non_prime_number_returns_y():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 10, 20) == 20
    assert x_or_y(8, 5, 10) == 10
    assert x_or_y(9, 100, 1) == 1

def test_edge_cases():
    assert x_or_y(1, 10, 20) == 20  # 1 is not prime
    assert x_or_y(2, 10, 20) == 10 # 2 is prime

# Focus: Value Assignment Logic
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
    assert x_or_y(5, 100, 0) == 100
    assert x_or_y(11, 1, 2) == 1

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 7, 8) == 8
    assert x_or_y(9, 10, 11) == 11
    assert x_or_y(1, 12, 13) == 13

def test_x_or_y_edge_cases():
    assert x_or_y(0, 5, 6) == 6
    assert x_or_y(1, 5, 6) == 6
    assert x_or_y(2, 0, 0) == 0
    assert x_or_y(2, -1, 1) == -1
    assert x_or_y(4, -5, -6) == -6

# Focus: Input Data Types
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

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if is_prime(n):
        return x
    else:
        return y

def test_x_or_y_int_inputs():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(4, 10, 20) == 20
    assert x_or_y(1, 10, 20) == 20

def test_x_or_y_float_inputs():
    assert x_or_y(7.0, 34.0, 12.0) == 34.0
    assert x_or_y(15.0, 8.0, 5.0) == 5.0
    assert x_or_y(2.0, 10.0, 20.0) == 10.0
    assert x_or_y(4.0, 10.0, 20.0) == 20.0
    assert x_or_y(1.0, 10.0, 20.0) == 20.0

def test_x_or_y_mixed_inputs():
    assert x_or_y(7, 34.0, 12) == 34.0
    assert x_or_y(15.0, 8, 5.0) == 5.0
    assert x_or_y(2.0, 10, 20.0) == 10
    assert x_or_y(4.0, 10.0, 20) == 20
    assert x_or_y(1, 10.0, 20) == 20