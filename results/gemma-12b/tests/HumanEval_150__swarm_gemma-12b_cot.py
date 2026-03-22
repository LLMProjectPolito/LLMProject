import pytest
import math

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_x_or_y_edge_case_n_equals_1():
    """Test when n is 1, which is not prime, so y should be returned."""
    assert x_or_y(1, 10, 20) == 20

def test_x_or_y_edge_case_n_equals_one():
    """Test when n is 1, which is not prime, so y should be returned."""
    assert x_or_y(1, 10, 20) == 20