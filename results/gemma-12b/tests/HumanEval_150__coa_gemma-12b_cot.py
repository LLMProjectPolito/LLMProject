import pytest
import math


# Focus: Prime Number Logic
def test_x_or_y_prime_number():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 100, 200) == 100
    assert x_or_y(5, 50, 60) == 50

def test_x_or_y_non_prime_number():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(4, 25, 35) == 35

def test_x_or_y_edge_cases():
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(3, 7, 9) == 7

# Focus: Boundary Values
import pytest

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_x_or_y_prime_boundary_1():
    """Test when n is the smallest prime number (2)."""
    assert x_or_y(2, 10, 20) == 10

def test_x_or_y_non_prime_boundary_1():
    """Test when n is the smallest non-prime number (1)."""
    assert x_or_y(1, 5, 15) == 15

def test_x_or_y_prime_boundary_large():
    """Test with a larger prime number."""
    assert x_or_y(997, 100, 200) == 100

# Focus: Type Scenarios
import pytest

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_x_or_y_prime_input():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 100, 200) == 100
    assert x_or_y(5, 50, 60) == 50
    assert x_or_y(11, 77, 88) == 77

def test_x_or_y_non_prime_input():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(4, 25, 35) == 35
    assert x_or_y(6, 40, 50) == 50

def test_x_or_y_edge_cases():
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(1, 1, 2) == 2
    assert x_or_y(2, 1, 2) == 1