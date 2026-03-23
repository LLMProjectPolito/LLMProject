import pytest
import math

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34

def test_edge_n_is_zero():
    """Test when n is zero, which is not a prime number."""
    assert x_or_y(0, 34, 12) == 12

import pytest

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_x_or_y_negative_n():
    """Test with a negative value for n."""
    assert x_or_y(-5, 10, 20) == 20

def test_x_or_y_zero_n():
    """Test with zero for n."""
    assert x_or_y(0, 5, 15) == 15

def test_x_or_y_one_n():
    """Test with one for n."""
    assert x_or_y(1, 7, 9) == 9

def test_x_or_y_large_prime():
    """Test with a large prime number for n."""
    assert x_or_y(997, 1, 2) == 1

def test_x_or_y_large_non_prime():
    """Test with a large non-prime number for n."""
    assert x_or_y(1000, 3, 4) == 4

def test_x_or_y_x_and_y_same():
    """Test when x and y are the same."""
    assert x_or_y(5, 8, 8) == 8

def test_x_or_y_n_is_prime_x_is_negative():
    """Test when n is prime and x is negative."""
    assert x_or_y(7, -5, 10) == -5

def test_x_or_y_n_is_not_prime_y_is_negative():
    """Test when n is not prime and y is negative."""
    assert x_or_y(4, 10, -5) == -5