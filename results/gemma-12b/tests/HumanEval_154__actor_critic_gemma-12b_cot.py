
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

    def test_rotation_not_simple(self):
        assert cycpattern_check("himenss", "simen") == True

    def test_longer_b_false(self):
        assert cycpattern_check("abc", "abcd") == False

    def test_same_word_true(self):
        assert cycpattern_check("abc", "abc") == True

    def test_empty_b_false(self):
        assert cycpattern_check("abc", "") == False

    def test_empty_a_false(self):
        assert cycpattern_check("", "abc") == False

    def test_repeated_chars_true(self):
        assert cycpattern_check("efef", "ef") == True

    def test_repeated_chars_false(self):
        assert cycpattern_check("efef", "eeff") == False

    def test_case_sensitive(self):
        assert cycpattern_check("Hello", "ell") == False
        assert cycpattern_check("hello", "Ell") == False

    def test_special_chars_true(self):
        assert cycpattern_check("!@#$", "#$!") == True

    def test_special_chars_false(self):
        assert cycpattern_check("!@#$", "!@#") == False

    def test_long_strings_true(self):
        assert cycpattern_check("abcdefghijklmnopqrstuvwxyz", "def") == True

    def test_long_strings_false(self):
        assert cycpattern_check("abcdefghijklmnopqrstuvwxyz", "ghi") == False

    def test_b_is_substring_but_not_rotation(self):
        assert cycpattern_check("abcde", "bcd") == True

    def test_b_is_prefix_of_a(self):
        assert cycpattern_check("abcdef", "abc") == True

    def test_b_is_suffix_of_a(self):
        assert cycpattern_check("abcdef", "def") == True

    def test_overlapping_rotations_true(self):
        assert cycpattern_check("aaaa", "aa") == True

    def test_identical_but_b_longer_false(self):
        assert cycpattern_check("abc", "abcde") == False

    def test_single_char_substring(self):
        assert cycpattern_check("abc", "a") == True