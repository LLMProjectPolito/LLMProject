import pytest

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if is_prime(n):
        return x
    else:
        return y

class TestXorY:
    def test_prime_number(self):
        """Test when n is a prime number."""
        assert x_or_y(7, 34, 12) == 34
        assert x_or_y(2, 100, 200) == 100
        assert x_or_y(5, 5, 10) == 5
        assert x_or_y(11, 111, 222) == 111

    def test_non_prime_number(self):
        """Test when n is not a prime number."""
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(9, 10, 20) == 20
        assert x_or_y(10, 30, 40) == 40

    def test_edge_cases(self):
        """Test edge cases like 0, 1, and negative numbers."""
        assert x_or_y(0, 1, 2) == 2
        assert x_or_y(1, 3, 4) == 4
        assert x_or_y(-5, 50, 60) == 60  # Negative numbers are not prime

    def test_same_values(self):
        """Test when x and y are the same."""
        assert x_or_y(7, 5, 5) == 5
        assert x_or_y(10, 5, 5) == 5

    def test_large_numbers(self):
        """Test with larger numbers to ensure no overflow issues."""
        assert x_or_y(1000000007, 1000, 2000) == 1000
        assert x_or_y(1000000008, 1000, 2000) == 2000