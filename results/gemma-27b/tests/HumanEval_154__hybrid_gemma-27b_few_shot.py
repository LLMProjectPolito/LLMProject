
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
        return True  # Empty string is always a substring

    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False

class TestCycpatternCheck:

    def test_basic_true(self):
        assert cycpattern_check("hello", "ell") == True

    def test_basic_false(self):
        assert cycpattern_check("abcd", "abd") == False

    def test_rotation_needed(self):
        assert cycpattern_check("abab", "baa") == True

    def test_no_match(self):
        assert cycpattern_check("efef", "eeff") == False

    def test_longer_string(self):
        assert cycpattern_check("himenss", "simen") == True

    def test_empty_a(self):
        assert cycpattern_check("", "abc") == False

    def test_empty_b(self):
        assert cycpattern_check("abc", "") == True

    def test_both_empty(self):
        assert cycpattern_check("", "") == True

    def test_b_longer_than_a(self):
        assert cycpattern_check("abc", "abcdef") == False

    def test_same_string(self):
        assert cycpattern_check("abc", "abc") == True

    def test_repeated_pattern_a(self):
        assert cycpattern_check("ababab", "ab") == True

    def test_repeated_pattern_b(self):
        assert cycpattern_check("abc", "aa") == False

    def test_case_sensitive(self):
        assert cycpattern_check("Hello", "ell") == False

    def test_special_characters(self):
        assert cycpattern_check("a!bc", "!bc") == True

    def test_numbers_and_letters(self):
        assert cycpattern_check("123abc456", "3abc") == True

    def test_long_strings_no_match(self):
        assert cycpattern_check("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba") == False

    def test_long_strings_with_match(self):
        long_string = "abcdefgh" * 10
        assert cycpattern_check(long_string, "defgh") == True

    def test_b_is_prefix_of_a(self):
        assert cycpattern_check("abcdef", "abc") == True

    def test_b_is_suffix_of_a(self):
        assert cycpattern_check("abcdef", "def") == True

    def test_cycpattern_check_longer_a(self):
        assert cycpattern_check("abcdefg", "bcd") == True

    def test_cycpattern_check_longer_b(self):
        assert cycpattern_check("abc", "abcdefg") == False

    def test_cycpattern_check_rotation_needed(self):
        assert cycpattern_check("waterbottle", "erbottlewat") == True

    def test_cycpattern_check_no_rotation_needed(self):
        assert cycpattern_check("waterbottle", "water") == True

    def test_cycpattern_check_complex_rotation(self):
        assert cycpattern_check("abcabcabc", "bca") == True

    def test_cycpattern_check_complex_no_match(self):
        assert cycpattern_check("abcabcabc", "def") == False

    def test_cycpattern_check_repeated_chars(self):
        assert cycpattern_check("aaaaaa", "aa") == True

    def test_cycpattern_check_repeated_chars_no_match(self):
        assert cycpattern_check("aaaaaa", "bbb") == False

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None