import pytest
from your_module import even_odd_count  # Replace your_module

class TestEvenOddCount:
    """
    A comprehensive pytest suite for the even_odd_count function.
    """

    def test_positive_integer(self):
        """Tests with a positive integer."""
        assert even_odd_count(123) == (1, 2)
        assert even_odd_count(124) == (2, 1)
        assert even_odd_count(123456) == (3, 3)
        assert even_odd_count(13579) == (0, 5)
        assert even_odd_count(24680) == (5, 0)
        assert even_odd_count(1234567890) == (5, 5)
        assert even_odd_count(2468013579) == (5, 5)

    def test_negative_integer(self):
        """Tests with a negative integer."""
        assert even_odd_count(-12) == (1, 1)
        assert even_odd_count(-123) == (1, 2)
        assert even_odd_count(-123456) == (3, 3)
        assert even_odd_count(-13579) == (0, 5)
        assert even_odd_count(-24680) == (5, 0)

    def test_zero(self):
        """Tests with zero."""
        assert even_odd_count(0) == (1, 0)

    def test_single_digit(self):
        """Tests with single-digit numbers (even and odd)."""
        assert even_odd_count(0) == (1, 0)
        assert even_odd_count(1) == (0, 1)
        assert even_odd_count(2) == (1, 0)
        assert even_odd_count(3) == (0, 1)
        assert even_odd_count(4) == (1, 0)
        assert even_odd_count(5) == (0, 1)
        assert even_odd_count(6) == (1, 0)
        assert even_odd_count(7) == (0, 1)
        assert even_odd_count(8) == (1, 0)
        assert even_odd_count(9) == (0, 1)

    def test_number_with_leading_zeros(self):
        """Tests with a number that might be interpreted as having leading zeros."""
        assert even_odd_count(10203) == (2, 2)
        assert even_odd_count(102) == (1, 2)
        assert even_odd_count(204) == (2, 1)

    def test_edge_cases(self):
        """Tests some edge cases."""
        assert even_odd_count(11) == (0, 2)
        assert even_odd_count(22) == (2, 0)
        assert even_odd_count(121) == (1, 2)
        assert even_odd_count(212) == (2, 1)
        assert even_odd_count(2222) == (4, 0)
        assert even_odd_count(1111) == (0, 4)
        assert even_odd_count(12345) == (2, 3)
        assert even_odd_count(21345) == (2, 3)
        assert even_odd_count(12346) == (2, 3)
        assert even_odd_count(21346) == (2, 3)


def test_palindrome_basic():
    """Tests basic palindrome functionality."""
    assert even_odd_count("radar") == True
    assert even_odd_count("hello") == False

def test_palindrome_empty():
    """Tests empty string palindrome functionality."""
    assert even_odd_count("") == True

def test_get_max_positive():
    """Tests getting the maximum of a list of positive integers."""
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    """Tests getting the maximum of an empty list."""
    assert get_max([]) == None