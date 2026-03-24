
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest
import math


# Focus: Prime Number Logic
def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_prime_number():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(11, 100, 20) == 100
    assert x_or_y(2, 50, 10) == 50

def test_non_prime_number():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 7) == 7
    assert x_or_y(9, 25, 15) == 15

def test_edge_cases():
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(0, 30, 40) == 40

# Focus: Boundary Values
def test_x_or_y_boundary_prime():
    assert x_or_y(2, 5, 10) == 5

def test_x_or_y_boundary_non_prime():
    assert x_or_y(1, 5, 10) == 10

def test_x_or_y_boundary_edge_case():
    assert x_or_y(0, 5, 10) == 10

# Focus: Type Scenarios
def test_prime_returns_x():
    assert x_or_y(7, 34, 12) == 34

def test_non_prime_returns_y():
    assert x_or_y(15, 8, 5) == 5

def test_edge_case_one_returns_y():
    assert x_or_y(1, 10, 20) == 20