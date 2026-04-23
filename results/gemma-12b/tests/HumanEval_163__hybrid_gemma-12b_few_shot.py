
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
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative.")
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


class TestFunctions:
    """
    Comprehensive pytest suite for multiple functions.
    """

    def test_generate_integers_basic_ascending(self):
        """Tests the basic ascending case."""
        assert generate_integers(2, 8) == [2, 4, 6, 8]

    def test_generate_integers_basic_descending(self):
        """Tests the basic descending case."""
        assert generate_integers(8, 2) == [2, 4, 6, 8]

    def test_generate_integers_no_even_numbers(self):
        """Tests when there are no even numbers in the range."""
        assert generate_integers(10, 14) == []

    def test_generate_integers_single_even_number(self):
        """Tests when there's only one even number in the range."""
        assert generate_integers(2, 3) == [2]

    def test_generate_integers_start_and_end_are_even(self):
        """Tests when both start and end are even."""
        assert generate_integers(4, 8) == [4, 6, 8]

    def test_generate_integers_start_is_odd_end_is_even(self):
        """Tests when start is odd and end is even."""
        assert generate_integers(1, 6) == [2, 4, 6]

    def test_generate_integers_start_is_even_end_is_odd(self):
        """Tests when start is even and end is odd."""
        assert generate_integers(6, 7) == [6]

    def test_generate_integers_same_numbers(self):
        """Tests when start and end are the same."""
        assert generate_integers(2, 2) == [2]

    def test_generate_integers_start_greater_than_end(self):
        """Tests when start is greater than end (should still work correctly)."""
        assert generate_integers(8, 2) == [2, 4, 6, 8]

    def test_generate_integers_large_numbers(self):
        """Tests with larger numbers to ensure no overflow or performance issues."""
        assert generate_integers(100, 110) == [100, 102, 104, 106, 108, 110]

    def test_generate_integers_negative_input(self):
        """Tests with negative input (should raise ValueError)."""
        with pytest.raises(ValueError):
            generate_integers(-2, 8)

        with pytest.raises(ValueError):
            generate_integers(2, -8)

        with pytest.raises(ValueError):
            generate_integers(-2, -8)

    def test_generate_integers_zero_input(self):
        """Tests with zero as input."""
        assert generate_integers(0, 4) == [0, 2, 4]

    def test_is_palindrome_basic(self):
        """Tests basic palindrome cases."""
        assert is_palindrome('radar') == True
        assert is_palindrome('hello') == False

    def test_is_palindrome_empty(self):
        """Tests empty string palindrome case."""
        assert is_palindrome('') == True

    def test_is_palindrome_single_char(self):
        """Tests single character string."""
        assert is_palindrome('a') == True

    def test_is_palindrome_mixed_case(self):
        """Tests mixed case palindrome."""
        assert is_palindrome('Racecar') == False # Case sensitive

    def test_get_max_positive(self):
        """Tests getting the max of a list of positive numbers."""
        assert get_max([1, 2, 3]) == 3

    def test_get_max_empty(self):
        """Tests getting the max of an empty list."""
        assert get_max([]) == None

    def test_get_max_negative(self):
        """Tests getting the max of a list of negative numbers."""
        assert get_max([-1, -2, -3]) == -1

    def test_get_max_mixed(self):
        """Tests getting the max of a list of mixed positive and negative numbers."""
        assert get_max([-1, 2, -3, 4]) == 4