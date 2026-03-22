import pytest

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_x_or_y_prime():
    """Test case where n is a prime number."""
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(5, 100, 200) == 100
    assert x_or_y(11, 5, 10) == 5

def test_x_or_y_not_prime():
    """Test case where n is not a prime number."""
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 10, 20) == 20
    assert x_or_y(6, 100, 200) == 200
    assert x_or_y(9, 5, 10) == 10

def test_x_or_y_n_is_1():
    """Test case where n is 1 (not prime)."""
    assert x_or_y(1, 10, 20) == 20

def test_x_or_y_n_is_0():
    """Test case where n is 0 (not prime)."""
    assert x_or_y(0, 10, 20) == 20

def test_x_or_y_n_is_negative():
    """Test case where n is negative (not prime)."""
    assert x_or_y(-5, 10, 20) == 20

def test_x_or_y_x_and_y_are_equal():
    """Test case where x and y are equal."""
    assert x_or_y(7, 5, 5) == 5
    assert x_or_y(4, 5, 5) == 5

def test_x_or_y_with_large_numbers():
    """Test case with large numbers to ensure no overflow issues."""
    assert x_or_y(1000000007, 1000, 2000) == 1000
    assert x_or_y(1000000008, 1000, 2000) == 2000

def test_x_or_y_with_negative_x_and_y():
    """Test case with negative x and y values."""
    assert x_or_y(7, -34, -12) == -34
    assert x_or_y(15, -8, -5) == -5

def test_x_or_y_with_zero_x_and_y():
    """Test case with zero x and y values."""
    assert x_or_y(7, 0, 0) == 0
    assert x_or_y(15, 0, 0) == 0