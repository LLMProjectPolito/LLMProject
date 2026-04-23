
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

import pytest

def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if not b:
        return False
    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False

class TestCycPatternCheck:
    """
    Pytest class for testing the cycpattern_check function.
    This class uses parametrization to test various scenarios with different inputs.
    """

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            ("abcd", "abd", False),
            ("hello", "ell", True),
            ("whassup", "psus", False),
            ("abab", "baa", True),
            ("efef", "eeff", False),
            ("himenss", "simen", True),
            ("abcde", "cde", True),
            ("abcde", "edc", False),
            ("abcde", "abc", True),
            ("abcde", "e", True),
            ("abcde", "", False),  # Empty b
            ("abcde", "f", False),
            ("aaaaa", "aaaa", True),
            ("aaaaa", "aaab", False),
            ("aaaaa", "baaaa", True),
            ("aaaaa", "aaaaa", True),
            ("a", "a", True),
            ("a", "b", False),
            ("aa", "a", True),
            ("aa", "aa", True),
            ("aa", "b", False),
            ("abcabc", "bca", True),
            ("abcabc", "cab", True),
            ("abcabc", "abc", True),
            ("abcabc", "cba", False),
            ("abcabc", "bcab", True),
            ("abcabc", "bcabc", True),
            ("abcabc", "abcabc", True),
            ("abcabc", "xyz", False),
        ],
    )
    def test_cycpattern_check(a, b, expected):
        """
        Tests the cycpattern_check function with various inputs and expected outputs.
        """
        assert cycpattern_check(a, b) == expected

    def test_cycpattern_check_type_hints():
        """
        Tests that the function handles type hints correctly.
        """
        with pytest.raises(TypeError):
            cycpattern_check(123, "abc")
        with pytest.raises(TypeError):
            cycpattern_check("abc", 123)

    def test_cycpattern_check_long_strings():
        """
        Tests the function with long strings to ensure performance and correctness.
        """
        long_a = "a" * 1000
        long_b = "a" * 500
        assert cycpattern_check(long_a, long_b) == True

        long_a = "a" * 1000
        long_b = "b" * 500
        assert cycpattern_check(long_a, long_b) == False

    @pytest.mark.parametrize("a, b, expected", [
        ("abcd", "abd", False),
        ("hello", "ell", True),
        ("whassup", "psus", False),
        ("abab", "baa", True),
        ("efef", "eeff", False),
        ("himenss", "simen", True),
        ("abcde", "cde", True),
        ("abcde", "edcba", False),
        ("aaaaa", "aaaa", True),
        ("aaaaa", "aaab", False),
        ("abc", "abc", True),
        ("abc", "acb", False),
        ("a", "a", True),
        ("a", "b", False),
        ("", "a", False),
        ("", "", False),
        ("abc", "", False),
        ("abcabc", "bca", True),
        ("abcabc", "cab", True),
        ("abcabc", "abc", True),
        ("abcabc", "bcab", True),
        ("abcabc", "cabc", True),
        ("abcabc", "bcabc", True),
        ("abcabc", "abcabc", True),
        ("abcabc", "xyz", False),
        ("abcdefg", "efgabc", True),
        ("abcdefg", "abcdegf", False),
        ("abcdefg", "defgabc", True),
        ("abcdefg", "gabcdef", True),
        ("abcdefg", "abcdef", True),
        ("abcdefg", "bcdefga", True),
        ("abcdefg", "abcdefg", True),
        ("abcdefg", "abcdefgh", False),
    ])
    def test_cycpattern_check_extended(a, b, expected):
        assert cycpattern_check(a, b) == expected


def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None