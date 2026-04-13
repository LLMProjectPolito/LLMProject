
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest
import math


# Focus: Prime Number Determination
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
    assert x_or_y(11, 1, 2) == 1
    assert x_or_y(2, 5, 6) == 5

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 9, 10) == 10
    assert x_or_y(1, 11, 12) == 12

def test_x_or_y_edge_cases():
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(1, 3, 4) == 4
    assert x_or_y(2, 7, 8) == 7

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

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 5, 1) == 5
    assert x_or_y(5, 100, 0) == 100

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 7, 8) == 8
    assert x_or_y(9, 10, 11) == 11

def test_x_or_y_edge_cases():
    assert x_or_y(1, 5, 6) == 6
    assert x_or_y(0, 10, 20) == 20
    assert x_or_y(2, 0, 0) == 0

# Focus: Input Data Types
import pytest

def test_x_or_y_invalid_n_type():
    with pytest.raises(TypeError):
        x_or_y("7", 34, 12)

def test_x_or_y_invalid_x_type():
    with pytest.raises(TypeError):
        x_or_y(7, "34", 12)

def test_x_or_y_invalid_y_type():
    with pytest.raises(TypeError):
        x_or_y(7, 34, "12")