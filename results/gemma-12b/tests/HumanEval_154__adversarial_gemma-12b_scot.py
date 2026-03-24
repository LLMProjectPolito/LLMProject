
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
        return True
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

    def test_rotation_false(self):
        assert cycpattern_check("whassup", "psus") == False

    def test_empty_a(self):
        assert cycpattern_check("", "abc") == False

    def test_empty_b(self):
        assert cycpattern_check("abc", "") == True

    def test_both_empty(self):
        assert cycpattern_check("", "") == True

    def test_identical_strings(self):
        assert cycpattern_check("abc", "abc") == True

    def test_b_longer_than_a(self):
        assert cycpattern_check("abc", "abcd") == False

    def test_overlapping_rotation(self):
        assert cycpattern_check("abcabc", "bca") == True

    def test_complex_rotation(self):
        assert cycpattern_check("efef", "eeff") == False