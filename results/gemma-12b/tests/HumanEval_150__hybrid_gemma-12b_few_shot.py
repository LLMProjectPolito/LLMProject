
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


class TestXOrY:
    """Test suite for the x_or_y function."""

    def test_prime_number(self):
        """Tests with prime numbers."""
        assert x_or_y(7, 34, 12) == 34
        assert x_or_y(2, 100, 200) == 100
        assert x_or_y(11, 5, 10) == 5
        assert x_or_y(13, "a", "b") == "a"  # Test with strings

    def test_non_prime_number(self):
        """Tests with non-prime numbers."""
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(9, "x", "y") == "y"  # Test with strings
        assert x_or_y(6, 10, 20) == 20

    def test_edge_cases(self):
        """Tests edge cases like 0, 1, and negative numbers."""
        assert x_or_y(0, 1, 2) == 2
        assert x_or_y(1, 3, 4) == 4
        assert x_or_y(-5, 50, 60) == 60  # Negative numbers are not prime
        assert x_or_y(-1, 5, 6) == 6
        assert x_or_y(-2, 7, 8) == 8

    def test_large_numbers(self):
        """Tests with larger numbers to ensure no overflow or unexpected behavior."""
        assert x_or_y(1000000007, 1000, 2000) == 1000  # 1000000007 is prime
        assert x_or_y(1000000000, 500, 600) == 600  # 1000000000 is not prime

    def test_negative_x_and_y(self):
        """Test cases where both x and y are negative."""
        assert x_or_y(5, -10, -20) == -10
        assert x_or_y(4, -5, -10) == -10

    def test_zero_x_and_y(self):
        """Test cases where both x and y are zero."""
        assert x_or_y(7, 0, 0) == 0
        assert x_or_y(8, 0, 0) == 0

    def test_prime_with_zero_values(self):
        """Test case where n is prime and x or y is zero."""
        assert x_or_y(13, 0, 5) == 0
        assert x_or_y(17, 5, 0) == 5

    def test_non_prime_with_zero_values(self):
        """Test case where n is not prime and x or y is zero."""
        assert x_or_y(6, 0, 5) == 5
        assert x_or_y(8, 5, 0) == 0

    def test_mixed_types(self):
        """Tests with mixed data types for x and y."""
        assert x_or_y(5, 10, "hello") == 10
        assert x_or_y(4, "world", 20) == 20

    def test_is_prime_helper(self):
        """Tests the is_prime helper function directly."""
        assert is_prime(7) == True
        assert is_prime(4) == False
        assert is_prime(2) == True
        assert is_prime(1) == False
        assert is_prime(0) == False
        assert is_prime(-5) == False