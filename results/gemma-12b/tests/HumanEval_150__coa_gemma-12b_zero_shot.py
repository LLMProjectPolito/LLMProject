
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
    assert is_prime(7) == True
    assert is_prime(2) == True
    assert is_prime(11) == True
    assert is_prime(13) == True

def test_non_prime_number():
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False

def test_edge_cases():
    assert is_prime(0) == False
    assert is_prime(-1) == False
    assert is_prime(-2) == False

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