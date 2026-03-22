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

def test_prime_number_returns_x():
    """Test case where n is prime, should return x."""
    assert x_or_y(7, 34, 12) == 34

def test_non_prime_number_returns_y():
    """Test case where n is not prime, should return y."""
    assert x_or_y(15, 8, 5) == 5

def test_edge_case_n_equals_1():
    """Test case where n is 1 (not prime), should return y."""
    assert x_or_y(1, 10, 20) == 20

def test_edge_case_n_equals_2():
    """Test case where n is 2 (prime), should return x."""
    assert x_or_y(2, 5, 10) == 5

# Focus: Boundary Values
import pytest

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_x_or_y_boundary_prime():
    """Test when n is the smallest prime number (2)."""
    assert x_or_y(2, 34, 12) == 34

def test_x_or_y_boundary_non_prime():
    """Test when n is the smallest non-prime number (1)."""
    assert x_or_y(1, 34, 12) == 12

def test_x_or_y_boundary_edge_case():
    """Test when n is a number close to a prime number (e.g., 4, which is not prime)."""
    assert x_or_y(4, 34, 12) == 12

# Focus: Type Scenarios
def test_x_or_y_prime_n():
    """Test case where n is a prime number."""
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_non_prime_n():
    """Test case where n is not a prime number."""
    assert x_or_y(15, 8, 5) == 5

def test_x_or_y_n_is_one():
    """Test case where n is 1 (not prime)."""
    assert x_or_y(1, 10, 20) == 20