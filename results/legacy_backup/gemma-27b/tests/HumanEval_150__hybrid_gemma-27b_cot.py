import pytest

def is_prime(n):
    """Helper function to determine if a number is prime."""
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
    """
    Given an integer n, and two other integers x and y,
    return x if n is a prime number, otherwise return y.
    """
    if is_prime(n):
        return x
    else:
        return y

def test_x_or_y_prime_number():
    """Test when n is a prime number."""
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 5, 1) == 5
    assert x_or_y(5, 100, 0) == 100
    assert x_or_y(11, -1, 1) == -1

def test_x_or_y_not_prime_number():
    """Test when n is not a prime number."""
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 7, 8) == 8
    assert x_or_y(9, 0, -1) == -1
    assert x_or_y(10, 1000, 1) == 1

def test_x_or_y_edge_cases():
    """Test edge cases like 0, 1, and negative numbers."""
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(1, 3, 4) == 4
    assert x_or_y(-5, 5, 6) == 6  # Negative input for n
    assert x_or_y(2, -10, 5) == -10 # Negative x
    assert x_or_y(3, 10, -5) == 10 # Negative y

def test_x_or_y_large_numbers():
    """Test with large numbers to check for potential overflow issues."""
    assert x_or_y(1000000007, 100, 200) == 100  # Large prime
    assert x_or_y(1000000008, 300, 400) == 400  # Large non-prime

def test_x_or_y_same_values():
    """Test when x and y are the same."""
    assert x_or_y(7, 5, 5) == 5
    assert x_or_y(10, 2, 2) == 2

def test_x_or_y_zero_values():
    """Test when x or y is zero."""
    assert x_or_y(7, 0, 5) == 0
    assert x_or_y(10, 5, 0) == 0
    assert x_or_y(7, 0, 0) == 0

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 5, 1) == 5
    assert x_or_y(5, 100, 200) == 100
    assert x_or_y(11, 1, 2) == 1
    assert x_or_y(13, -5, 10) == -5
    assert x_or_y(17, 0, 1) == 0
    assert x_or_y(19, 10, -10) == 10
    assert x_or_y(23, 1000, -1000) == 1000
    assert x_or_y(29, -1, -2) == -1

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 10, 20) == 20
    assert x_or_y(8, 5, 1) == 1
    assert x_or_y(9, 100, 200) == 200
    assert x_or_y(10, 1, 2) == 2
    assert x_or_y(12, -5, 10) == 10
    assert x_or_y(14, 0, 1) == 1
    assert x_or_y(16, 10, -10) == -10
    assert x_or_y(18, 1000, -1000) == -1000
    assert x_or_y(20, -1, -2) == -2

def test_x_or_y_edge_cases():
    assert x_or_y(1, 10, 20) == 20  # 1 is not prime
    assert x_or_y(2, 10, 20) == 10  # 2 is prime
    assert x_or_y(0, 10, 20) == 20  # 0 is not prime
    assert x_or_y(-1, 10, 20) == 20 # negative number is not prime
    assert x_or_y(100, 10, 20) == 20
    assert x_or_y(101, 10, 20) == 10

def test_x_or_y_large_numbers():
    assert x_or_y(1000000007, 1, 2) == 1 # large prime
    assert x_or_y(1000000008, 1, 2) == 2 # large non-prime

def test_x_or_y_same_values():
    assert x_or_y(7, 5, 5) == 5
    assert x_or_y(4, 5, 5) == 5