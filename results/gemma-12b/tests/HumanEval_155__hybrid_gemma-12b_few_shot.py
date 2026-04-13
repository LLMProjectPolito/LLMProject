
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
        assert even_odd_count(2468) == (4, 0)
        assert even_odd_count(13579) == (0, 5)
        assert even_odd_count(1234567890) == (5, 5)
        assert even_odd_count(123456) == (3, 3)
        assert even_odd_count(24680) == (5, 0)
        assert even_odd_count(12345678901234567890) == (5, 10)
        assert even_odd_count(2468013579) == (5, 5)

    def test_negative_integer(self):
        """Tests with negative integers."""
        assert even_odd_count(-12) == (1, 1)
        assert even_odd_count(-13) == (0, 2)
        assert even_odd_count(-24) == (2, 0)
        assert even_odd_count(-12345) == (1, 4)
        assert even_odd_count(-2468) == (4, 0)
        assert even_odd_count(-1234567890) == (5, 5)

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

    def test_number_with_repeated_digits(self):
        """Tests with numbers containing repeated digits."""
        assert even_odd_count(112233) == (2, 3)
        assert even_odd_count(2222) == (4, 0)
        assert even_odd_count(1111) == (0, 4)

    def test_edge_cases(self):
        """Tests some edge cases."""
        assert even_odd_count(10) == (1, 1)
        assert even_odd_count(21) == (1, 1)
        assert even_odd_count(101) == (1, 2)
        assert even_odd_count(202) == (2, 1)
        assert even_odd_count(11) == (0, 2)
        assert even_odd_count(22) == (2, 0)
        assert even_odd_count(121) == (1, 2)
        assert even_odd_count(212) == (2, 1)
        assert even_odd_count(1000) == (3, 1)
        assert even_odd_count(2000) == (4, 0)
        assert even_odd_count(102) == (1, 2)
        assert even_odd_count(204) == (2, 1)

    def test_palindrome(self):
        """Tests the is_palindrome function."""
        assert is_palindrome('radar') == True
        assert is_palindrome('hello') == False
        assert is_palindrome('') == True

    def test_get_max(self):
        """Tests the get_max function."""
        assert get_max([1, 2, 3]) == 3
        assert get_max([]) == None
        assert get_max([5, 2, 8, 1]) == 8
        assert get_max([-1, -5, -2]) == -1