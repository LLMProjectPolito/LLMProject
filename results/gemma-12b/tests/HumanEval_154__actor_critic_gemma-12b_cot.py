
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
    if len(b) > len(a):
        return False
    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False

class TestCycpatterCheck:
    def test_cycpattern_check_basic_true(self):
        assert cycpattern_check("hello", "ell") == True

    def test_cycpattern_check_basic_false(self):
        assert cycpattern_check("abcd", "abd") == False

    def test_cycpattern_check_rotation_true(self):
        assert cycpattern_check("abab", "baa") == True

    def test_cycpattern_check_no_rotation_true(self):
        assert cycpattern_check("himenss", "simen") == True

    def test_cycpattern_check_longer_b_false(self):
        assert cycpattern_check("abc", "abcd") == False

    def test_cycpattern_check_equal_strings_true(self):
        assert cycpattern_check("abc", "abc") == True

    def test_cycpattern_check_empty_b_false(self):
        assert cycpattern_check("abc", "") == False

    def test_cycpattern_check_empty_a_false(self):
        assert cycpattern_check("", "abc") == False

    def test_cycpattern_check_both_empty_false(self):
        assert cycpattern_check("", "") == False

    def test_cycpattern_check_repeated_chars_true(self):
        assert cycpattern_check("aaaa", "aa") == True

    def test_cycpattern_check_repeated_chars_false(self):
        assert cycpattern_check("efef", "eeff") == False

    def test_cycpattern_check_substring_exists(self):
        assert cycpattern_check("abcdef", "abc") == True
        assert cycpattern_check("abcdef", "def") == True
        assert cycpattern_check("abcdef", "cde") == True

    def test_cycpattern_check_case_sensitive(self):
        assert cycpattern_check("Hello", "ell") == False  # Case-sensitive

    def test_cycpattern_check_special_characters(self):
        assert cycpattern_check("abc!@#", "@#") == True

    def test_cycpattern_check_numbers(self):
        assert cycpattern_check("12345", "234") == True

    def test_cycpattern_check_mixed_characters(self):
        assert cycpattern_check("a1b2c3", "b2c") == True

    def test_cycpattern_check_single_char_present(self):
        assert cycpattern_check("abcdef", "a") == True

    def test_cycpattern_check_overlapping_rotations(self):
        assert cycpattern_check("ababab", "bab") == True

    def test_cycpattern_check_a_is_substring_of_b(self):
        assert cycpattern_check("abc", "abcdef") == True

    def test_cycpattern_check_b_is_substring_of_a(self):
        assert cycpattern_check("abcdef", "abc") == True

    def test_cycpattern_check_unicode_characters(self):
        assert cycpattern_check("héllö", "llö") == True

    def test_cycpattern_check_unicode_characters_false(self):
        assert cycpattern_check("héllö", "llo") == False

    def test_cycpattern_check_long_strings(self):
        long_a = "a" * 1000
        long_b = "a" * 500
        assert cycpattern_check(long_a, long_b) == True

    def test_cycpattern_check_repeated_chars_complex(self):
        assert cycpattern_check("aabbcc", "bbcc") == True
        assert cycpattern_check("aabbcc", "bccb") == False
        assert cycpattern_check("aabbcc", "ccbb") == True