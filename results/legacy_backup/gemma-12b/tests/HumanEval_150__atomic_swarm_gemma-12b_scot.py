import pytest
import math

def test_x_or_y_prime_input():
    """Test when n is a prime number."""
    assert x_or_y(7, 34, 12) == 34

import pytest

def test_x_or_y_negative_n():
    """Test with a negative input for n.  Since the primality test
    is not defined for negative numbers, the function should return y."""
    assert x_or_y(-5, 10, 20) == 20

import pytest

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_n_is_negative():
    """Test case: n is negative, should return y."""
    assert x_or_y(-5, 10, 20) == 20

def test_x_and_y_are_strings():
    """Test case: x and y are strings, should return y."""
    assert x_or_y(5, "hello", "world") == "world"

def test_n_is_zero():
    """Test case: n is zero, should return y."""
    assert x_or_y(0, 1, 2) == 2

def test_n_is_one():
    """Test case: n is one, should return y."""
    assert x_or_y(1, 5, 10) == 10