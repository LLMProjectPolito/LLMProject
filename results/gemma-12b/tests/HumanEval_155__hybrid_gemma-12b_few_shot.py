
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest
from your_module import even_odd_count  # Replace your_module

class TestEvenOddCount:
    """
    A comprehensive test suite for the even_odd_count function.
    """

    def test_positive_integer(self):
        """Tests with positive integers."""
        assert even_odd_count(123) == (1, 2)
        assert even_odd_count(124) == (2, 1)
        assert even_odd_count(123456) == (3, 3)
        assert even_odd_count(13579) == (0, 5)
        assert even_odd_count(24680) == (5, 0)
        assert even_odd_count(1234567890) == (5, 5)
        assert even_odd_count(2468013579) == (5, 5)

    def test_negative_integer(self):
        """Tests with negative integers."""
        assert even_odd_count(-12) == (1, 1)
        assert even_odd_count(-123) == (1, 2)
        assert even_odd_count(-123456) == (3, 3)
        assert even_odd_count(-13579) == (0, 5)
        assert even_odd_count(-24680) == (5, 0)
        assert even_odd_count(-13) == (0, 2)
        assert even_odd_count(-24) == (2, 0)
        assert even_odd_count(-12345) == (1, 4)
        assert even_odd_count(-2468) == (4, 0)

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
        """Tests with numbers that might be interpreted as having leading zeros."""
        assert even_odd_count(102) == (1, 2)
        assert even_odd_count(204) == (2, 1)
        assert even_odd_count(10203) == (2, 2)

    def test_all_same_digits(self):
        """Tests with numbers containing all the same digits."""
        assert even_odd_count(2222) == (4, 0)
        assert even_odd_count(1111) == (0, 4)
        assert even_odd_count(22222) == (5, 0)
        assert even_odd_count(11111) == (0, 5)

    def test_mixed_even_odd(self):
        """Tests with a mix of even and odd digits."""
        assert even_odd_count(12345) == (2, 3)
        assert even_odd_count(21345) == (2, 3)
        assert even_odd_count(13572) == (1, 4)
        assert even_odd_count(24681) == (4, 1)
        assert even_odd_count(12121) == (2, 3)
        assert even_odd_count(21212) == (3, 2)


def test_palindrome_basic():
    """Tests basic palindrome cases."""
    assert even_odd_count("radar") == True
    assert even_odd_count("hello") == False

def test_palindrome_empty():
    """Tests empty string palindrome case."""
    assert even_odd_count("") == True

def test_get_max_positive():
    """Tests getting the maximum of a list of positive integers."""
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    """Tests getting the maximum of an empty list."""
    assert get_max([]) == None