import pytest
import math


# Focus: Prime Number Logic
def test_x_or_y_prime_returns_x():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_non_prime_returns_y():
    assert x_or_y(15, 8, 5) == 5

def test_x_or_y_prime_edge_case():
    assert x_or_y(2, 10, 20) == 10

# Focus: Boundary Values
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
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

def test_x_or_y_prime_boundary():
    assert x_or_y(2, 5, 10) == 5
    assert x_or_y(3, 5, 10) == 5

def test_x_or_y_non_prime_boundary():
    assert x_or_y(1, 5, 10) == 10
    assert x_or_y(4, 5, 10) == 10

# Focus: Type Scenarios
def test_x_or_y_prime_x():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_non_prime_y():
    assert x_or_y(15, 8, 5) == 5

def test_x_or_y_prime_large_x():
    assert x_or_y(101, 1000, 1) == 1000