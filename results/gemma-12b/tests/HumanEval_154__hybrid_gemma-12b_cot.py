
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
    def test_basic_true(self):
        assert cycpattern_check("hello", "ell") == True

    def test_basic_false(self):
        assert cycpattern_check("abcd", "abd") == False

    def test_rotation_true(self):
        assert cycpattern_check("abab", "baa") == True

    def test_no_rotation_true(self):
        assert cycpattern_check("himenss", "simen") == True

    def test_longer_b_false(self):
        assert cycpattern_check("abc", "abcd") == False

    def test_equal_strings_true(self):
        assert cycpattern_check("abc", "abc") == True

    def test_empty_b_false(self):
        assert cycpattern_check("abc", "") == False

    def test_empty_a_false(self):
        assert cycpattern_check("", "abc") == False

    def test_both_empty_false(self):
        assert cycpattern_check("", "") == False

    def test_repeated_chars_true(self):
        assert cycpattern_check("aaaa", "aa") == True

    def test_repeated_chars_false(self):
        assert cycpattern_check("efef", "eeff") == False

    def test_case_sensitive(self):
        assert cycpattern_check("Hello", "ell") == False

    def test_special_chars(self):
        assert cycpattern_check("abc!@#", "@#") == True

    def test_unicode_chars(self):
        assert cycpattern_check("你好世界", "界世") == True

    def test_long_strings_true(self):
        long_a = "abcdefghijklmnopqrstuvwxyz" * 2
        long_b = "uvwxyzabcdef"
        assert cycpattern_check(long_a, long_b) == True

    def test_long_strings_false(self):
        long_a = "abcdefghijklmnopqrstuvwxyz" * 2
        long_b = "zyxwvu"
        assert cycpattern_check(long_a, long_b) == False