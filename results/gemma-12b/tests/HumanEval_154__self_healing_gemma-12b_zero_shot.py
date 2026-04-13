
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
    def test_positive_cases(self):
        assert cycpattern_check("hello", "ell") == True
        assert cycpattern_check("abab", "baa") == True
        assert cycpattern_check("himenss", "simen") == True
        assert cycpattern_check("abcabc", "bca") == True
        assert cycpattern_check("rotation", "tiona") == True
        assert cycpattern_check("circular", "culari") == True
        assert cycpattern_check("abcdefg", "efgab") == True

    def test_negative_cases(self):
        assert cycpattern_check("abcd", "abd") == False
        assert cycpattern_check("whassup", "psus") == False
        assert cycpattern_check("efef", "eeff") == False
        assert cycpattern_check("xyz", "abc") == False
        assert cycpattern_check("apple", "banana") == False
        assert cycpattern_check("test", "tset") == False
        assert cycpattern_check("abc", "abcd") == False

    def test_empty_string_cases(self):
        assert cycpattern_check("", "") == False
        assert cycpattern_check("abc", "") == False
        assert cycpattern_check("", "abc") == False

    def test_same_string_cases(self):
        assert cycpattern_check("abc", "abc") == True
        assert cycpattern_check("a", "a") == True

    def test_edge_cases(self):
        assert cycpattern_check("aaaaa", "aaaa") == True
        assert cycpattern_check("aaaaa", "aaab") == False
        assert cycpattern_check("abcde", "cdeab") == True
        assert cycpattern_check("abcde", "bcdea") == True
        assert cycpattern_check("abcde", "cdeba") == False