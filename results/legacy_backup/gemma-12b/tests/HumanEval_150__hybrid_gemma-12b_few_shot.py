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

class TestXOrY:
    """Test suite for the x_or_y function."""

    def test_prime_x(self):
        """Test case where n is prime and should return x."""
        assert x_or_y(7, 34, 12) == 34
        assert x_or_y(2, 100, 200) == 100
        assert x_or_y(11, -5, 0) == -5

    def test_non_prime_y(self):
        """Test case where n is not prime and should return y."""
        assert x_or_y(15, 8, 5) == 5
        assert x_or_y(4, 1, 2) == 2
        assert x_or_y(9, 10, 20) == 20

    def test_edge_cases(self):
        """Test cases for edge conditions like 0, 1, and negative numbers."""
        assert x_or_y(0, 1, 2) == 2  # 0 is not prime
        assert x_or_y(1, 3, 4) == 4  # 1 is not prime
        assert x_or_y(-1, 5, 6) == 6 # -1 is not prime
        assert x_or_y(-2, 7, 8) == 8 # -2 is not prime

    def test_large_numbers(self):
        """Test cases with larger numbers to ensure no overflow or unexpected behavior."""
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

    def test_same_values(self):
        """Test when x and y are the same."""
        assert x_or_y(5, 7, 7) == 7
        assert x_or_y(4, 7, 7) == 7

    def test_negative_x_and_y_prime(self):
        """Test with negative x and y values when n is prime."""
        assert x_or_y(7, -34, -12) == -34
        assert x_or_y(15, -8, -5) == -5

def test_palindrome_basic():
    """Tests for the is_palindrome function."""
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    """Tests for the is_palindrome function with an empty string."""
    assert is_palindrome('') == True

def test_get_max_positive():
    """Tests for the get_max function with positive numbers."""
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    """Tests for the get_max function with an empty list."""
    assert get_max([]) == None