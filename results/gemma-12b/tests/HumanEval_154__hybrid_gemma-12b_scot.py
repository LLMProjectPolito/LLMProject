
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
    if not a:
        return False
    if len(b) > len(a):
        return False

    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False

class TestCycPatternCheck:
    def test_empty_b(self):
        assert cycpattern_check("abc", "") == True

    def test_empty_a(self):
        assert cycpattern_check("", "abc") == False

    def test_b_longer_than_a(self):
        assert cycpattern_check("abc", "abcd") == False

    def test_b_equal_to_a(self):
        assert cycpattern_check("abc", "abc") == True

    def test_b_is_substring_no_rotation(self):
        assert cycpattern_check("abcdef", "abc") == True

    def test_b_is_rotation_of_substring(self):
        assert cycpattern_check("abab", "baa") == True

    def test_b_not_substring_or_rotation(self):
        assert cycpattern_check("whassup", "psus") == False

    def test_overlapping_characters(self):
        assert cycpattern_check("hello", "ell") == True
        assert cycpattern_check("aaaa", "aa") == True

    def test_repeated_characters(self):
        assert cycpattern_check("efef", "eeff") == False
        assert cycpattern_check("himenss", "simen") == True

    def test_complex_rotation(self):
        assert cycpattern_check("abcde", "cdea") == True
        assert cycpattern_check("abcde", "eabcd") == True

    def test_substring_no_rotation(self):
        assert cycpattern_check("hello", "ell") == True

    def test_substring_with_rotation(self):
        assert cycpattern_check("abab", "baa") == True

    def test_no_substring(self):
        assert cycpattern_check("whassup", "psus") == False

    def test_both_empty(self):
        assert cycpattern_check("", "") == True

    def test_repeated_chars(self):
        assert cycpattern_check("aaaa", "aa") == True
        assert cycpattern_check("aaaa", "aaa") == True
        assert cycpattern_check("aaaa", "aaaa") == True
        assert cycpattern_check("aaaa", "bbbb") == False

    def test_special_chars(self):
        assert cycpattern_check("hello!", "lo!") == True
        assert cycpattern_check("hello?", "lo?") == True
        assert cycpattern_check("hello$", "lo$") == True
        assert cycpattern_check("hello#", "lo#") == True

    def test_edge_case_1(self):
        assert cycpattern_check("abcabc", "bca") == True

    def test_edge_case_2(self):
        assert cycpattern_check("abcdefg", "efgabc") == True