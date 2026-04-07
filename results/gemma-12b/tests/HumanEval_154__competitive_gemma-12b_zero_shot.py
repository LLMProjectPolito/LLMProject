
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

class TestCycpatternCheck:
    def test_positive_cases(self):
        assert cycpattern_check("hello", "ell") == True
        assert cycpattern_check("abab", "baa") == True
        assert cycpattern_check("himenss", "simen") == True
        assert cycpattern_check("abcde", "cde") == True
        assert cycpattern_check("abcde", "eabc") == True
        assert cycpattern_check("abcde", "bcdea") == True
        assert cycpattern_check("abcde", "deabc") == True
        assert cycpattern_check("abcde", "eabcd") == True
        assert cycpattern_check("aaaaa", "aaa") == True
        assert cycpattern_check("aaaaa", "aaaa") == True
        assert cycpattern_check("aaaaa", "aaaaa") == True
        assert cycpattern_check("abcdefg", "efgabc") == True

    def test_negative_cases(self):
        assert cycpattern_check("abcd", "abd") == False
        assert cycpattern_check("whassup", "psus") == False
        assert cycpattern_check("efef", "eeff") == False
        assert cycpattern_check("abc", "abcd") == False
        assert cycpattern_check("abc", "bcda") == False
        assert cycpattern_check("abc", "xyz") == False
        assert cycpattern_check("abc", "abcde") == False
        assert cycpattern_check("abc", "cba") == False
        assert cycpattern_check("abc", "cab") == False
        assert cycpattern_check("abc", "bac") == False
        assert cycpattern_check("abc", "acb") == False
        assert cycpattern_check("abc", "bca") == False
        assert cycpattern_check("abc", "ac") == False
        assert cycpattern_check("abc", "ab") == False
        assert cycpattern_check("abc", "bc") == False
        assert cycpattern_check("abc", "c") == False
        assert cycpattern_check("abc", "a") == False
        assert cycpattern_check("abc", "b") == False
        assert cycpattern_check("abc", "c") == False

    def test_empty_string_cases(self):
        assert cycpattern_check("", "") == True
        assert cycpattern_check("abc", "") == True
        assert cycpattern_check("", "abc") == False

    def test_same_string(self):
        assert cycpattern_check("abc", "abc") == True
        assert cycpattern_check("aaaa", "aaaa") == True

    def test_long_strings(self):
        long_a = "abcdefghijklmnopqrstuvwxyz" * 10
        assert cycpattern_check(long_a, "xyz") == True
        assert cycpattern_check(long_a, "zyx") == False
        assert cycpattern_check(long_a, long_a[:5]) == True
        assert cycpattern_check(long_a, long_a[5:]) == True