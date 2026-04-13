
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

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
    If n is prime, return x. Otherwise, return y.
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
    assert x_or_y(13, -5, 10) == -5
    assert x_or_y(17, 0, 1) == 0
    assert x_or_y(19, 10, -10) == 10
    assert x_or_y(23, 2.5, 3.5) == 2.5
    assert x_or_y(29, "a", "b") == "a"

def test_x_or_y_not_prime_number():
    """Test when n is not a prime number."""
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(6, 7, 8) == 8
    assert x_or_y(9, 0, -1) == -1
    assert x_or_y(10, 1000, 1) == 1
    assert x_or_y(8, 5, 1) == 1
    assert x_or_y(12, -5, 10) == 10
    assert x_or_y(14, 0, 1) == 1
    assert x_or_y(16, 10, -10) == -10
    assert x_or_y(18, 2.5, 3.5) == 3.5
    assert x_or_y(20, "a", "b") == "b"

def test_x_or_y_edge_cases():
    """Test edge cases like 0, 1, and negative numbers."""
    assert x_or_y(0, 1, 2) == 2
    assert x_or_y(1, 3, 4) == 4
    assert x_or_y(-5, 5, 6) == 6  # Negative input for n
    assert x_or_y(2, 0, 0) == 0
    assert x_or_y(1, 0, 0) == 0
    assert x_or_y(1, 10, 20) == 20  # 1 is not prime
    assert x_or_y(2, 10, 20) == 10  # 2 is prime
    assert x_or_y(0, 10, 20) == 20  # 0 is not prime
    assert x_or_y(-1, 10, 20) == 20 # negative number is not prime
    assert x_or_y(100, 10, 20) == 20
    assert x_or_y(101, 10, 20) == 10

def test_x_or_y_large_numbers():
    """Test with large numbers to check for potential overflow issues."""
    assert x_or_y(1000000007, 100, 200) == 100  # Large prime
    assert x_or_y(1000000008, 300, 400) == 400  # Large non-prime

def test_x_or_y_x_and_y_same():
    """Test when x and y are the same value."""
    assert x_or_y(7, 5, 5) == 5
    assert x_or_y(4, 10, 10) == 10

def test_x_or_y_negative_x_and_y():
    """Test with negative values for x and y."""
    assert x_or_y(7, -10, -20) == -10
    assert x_or_y(4, -5, -6) == -6

def test_x_or_y_mixed_signs():
    """Test with mixed signs for x and y."""
    assert x_or_y(7, -10, 20) == -10
    assert x_or_y(4, 5, -6) == -6

def test_x_or_y_type_handling():
    assert x_or_y(7, 34.5, 12) == 34.5
    assert x_or_y(15, 8, 5.5) == 5.5
    assert x_or_y(7, "hello", 12) == "hello"
    assert x_or_y(15, 8, "world") == "world"
    assert x_or_y(7, True, False) == True
    assert x_or_y(15, False, True) == True