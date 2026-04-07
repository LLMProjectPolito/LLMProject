
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

import pytest

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    start = min(a, b)
    end = max(a, b)
    result = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            result.append(i)
    return result

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


class TestGenerateIntegers:
    """
    Pytest class for testing the generate_integers function.
    """

    def test_basic_ascending(self):
        """Tests the basic ascending case."""
        assert generate_integers(2, 8) == [2, 4, 6, 8]

    def test_basic_descending(self):
        """Tests the basic descending case."""
        assert generate_integers(8, 2) == [2, 4, 6, 8]

    def test_no_even_numbers(self):
        """Tests the case where there are no even numbers in the range."""
        assert generate_integers(10, 14) == []

    def test_single_even_number(self):
        """Tests the case with a single even number."""
        assert generate_integers(4, 4) == [4]

    def test_start_is_odd(self):
        """Tests when the start number is odd."""
        assert generate_integers(3, 7) == [4, 6]

    def test_end_is_odd(self):
        """Tests when the end number is odd."""
        assert generate_integers(5, 9) == [6, 8]

    def test_start_and_end_odd(self):
        """Tests when both start and end numbers are odd."""
        assert generate_integers(1, 3) == [2]

    def test_same_number_even(self):
        """Tests when both numbers are the same and even."""
        assert generate_integers(6, 6) == [6]

    def test_large_numbers(self):
        """Tests with larger numbers to ensure no overflow issues."""
        assert generate_integers(100, 110) == [100, 102, 104, 106, 108, 110]

    def test_negative_input(self):
        """Tests with negative input (should still work correctly due to min/max)."""
        assert generate_integers(-2, 2) == [-2, 0, 2]

    def test_zero_input(self):
        """Tests with zero as input."""
        assert generate_integers(0, 4) == [0, 2, 4]


class TestPalindrome:
    def test_palindrome_basic(self):
        assert is_palindrome('radar') == True
        assert is_palindrome('hello') == False

    def test_palindrome_empty(self):
        assert is_palindrome('') == True

class TestGetMax:
    def test_max_positive(self):
        assert get_max([1, 2, 3]) == 3

    def test_max_empty(self):
        assert get_max([]) == None