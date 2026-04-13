
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
    n = len(b)
    for i in range(n):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False

class TestCycpatternCheck:
    def test_empty_strings(self):
        assert cycpattern_check("", "") == False

    def test_empty_b(self):
        assert cycpattern_check("abcd", "") == False

    def test_empty_a(self):
        assert cycpattern_check("", "abc") == False

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

    def test_same_string(self):
        assert cycpattern_check("abc", "abc") == True

    def test_b_longer_than_a(self):
        assert cycpattern_check("abc", "abcd") == False

    def test_repeated_pattern(self):
        assert cycpattern_check("ababab", "aba") == True

    def test_complex_rotation(self):
        assert cycpattern_check("waterbottle", "erbottlewat") == True

    def test_case_sensitive(self):
        assert cycpattern_check("Hello", "ell") == False

    def test_special_characters(self):
        assert cycpattern_check("a!b@c#", "b@c#a") == True

    def test_numbers(self):
        assert cycpattern_check("12345", "34512") == True

    def test_long_strings_no_match(self):
        assert cycpattern_check("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba") == False

    def test_long_strings_with_match(self):
        assert cycpattern_check("abcdefghijklmnopqrstuvwxyz", "def") == True