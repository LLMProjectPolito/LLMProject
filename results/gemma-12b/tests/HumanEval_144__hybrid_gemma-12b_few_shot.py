
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """

import pytest
from fractions import Fraction

def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    x_frac = Fraction(x)
    n_frac = Fraction(n)
    product = x_frac * n_frac
    return product.denominator == 1

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


class TestSimplify:
    """Pytest class for testing the simplify function."""

    def test_simplify_whole_number_result(self):
        """Tests cases where the result is a whole number."""
        assert simplify("1/5", "5/1") == True
        assert simplify("2/4", "2/1") == True
        assert simplify("1/1", "1/1") == True
        assert simplify("3/7", "7/3") == True
        assert simplify("1/2", "2/1") == True
        assert simplify("4/8", "2/1") == True

    def test_simplify_non_whole_number_result(self):
        """Tests cases where the result is not a whole number."""
        assert simplify("1/6", "2/1") == False
        assert simplify("7/10", "10/2") == False
        assert simplify("1/3", "1/2") == False
        assert simplify("2/5", "3/4") == False
        assert simplify("1/7", "2/3") == False

    def test_simplify_edge_cases(self):
        """Tests edge cases like fractions with 1 as numerator or denominator."""
        assert simplify("1/10", "10/1") == True
        assert simplify("10/1", "1/1") == True
        assert simplify("1/2", "1/1") == False
        assert simplify("1/1", "1/2") == False

    def test_simplify_large_numbers(self):
        """Tests cases with larger numbers to ensure no overflow issues."""
        assert simplify("1000/2", "2/1000") == True
        assert simplify("1000000/3", "3/1000000") == True
        assert simplify("12345/6789", "6789/12345") == False
        assert simplify("12345/67890", "67890/12345") == True
        assert simplify("12345/67890", "67891/12345") == False

    def test_simplify_same_fraction(self):
        """Tests cases where both inputs are the same fraction."""
        assert simplify("1/2", "1/2") == False
        assert simplify("3/4", "3/4") == False
        assert simplify("1/1", "1/1") == True

    def test_simplify_with_zeros_in_numerator(self):
        assert simplify("0/5", "5/1") == True

    def test_simplify_invalid_input(self):
        """Tests cases with invalid input (e.g., zero denominator)."""
        with pytest.raises(ZeroDivisionError):
            simplify("1/0", "1/1")
        with pytest.raises(ValueError):
            simplify("a/b", "1/1")  # Invalid fraction format
        with pytest.raises(ValueError):
            simplify("1/1", "b/c")  # Invalid fraction format


class TestPalindrome:
    """Pytest class for testing the is_palindrome function."""

    def test_palindrome_basic(self):
        assert is_palindrome('radar') == True
        assert is_palindrome('hello') == False

    def test_palindrome_empty(self):
        assert is_palindrome('') == True

    def test_palindrome_single_char(self):
        assert is_palindrome('a') == True

    def test_palindrome_mixed_case(self):
        assert is_palindrome('Racecar') == False  # Case-sensitive

    def test_palindrome_with_spaces(self):
        assert is_palindrome("A man, a plan, a canal: Panama") == False # Spaces are not ignored

class TestGetMax:
    """Pytest class for testing the get_max function."""

    def test_max_positive(self):
        assert get_max([1, 2, 3]) == 3

    def test_max_empty(self):
        assert get_max([]) == None

    def test_max_negative(self):
        assert get_max([-1, -2, -3]) == -1

    def test_max_mixed(self):
        assert get_max([-1, 2, -3, 4]) == 4

    def test_max_duplicates(self):
        assert get_max([1, 2, 2, 3]) == 3