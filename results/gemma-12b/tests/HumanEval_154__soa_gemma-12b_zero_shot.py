
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
    def test_positive_cases(self):
        assert cycpattern_check("hello", "ell") == True
        assert cycpattern_check("abab", "baa") == True
        assert cycpattern_check("himenss", "simen") == True
        assert cycpattern_check("abcde", "cde") == True
        assert cycpattern_check("abcde", "eab") == True
        assert cycpattern_check("abcde", "bcd") == True
        assert cycpattern_check("abcde", "abc") == True
        assert cycpattern_check("abcde", "deabc") == True
        assert cycpattern_check("aaaaa", "aaa") == True
        assert cycpattern_check("aaaaa", "aaaa") == True
        assert cycpattern_check("aaaaa", "aa") == True
        assert cycpattern_check("aaaaa", "a") == True
        assert cycpattern_check("aaaaa", "aaaaa") == True

    def test_negative_cases(self):
        assert cycpattern_check("abcd", "abd") == False
        assert cycpattern_check("whassup", "psus") == False
        assert cycpattern_check("efef", "eeff") == False
        assert cycpattern_check("abc", "abcd") == False
        assert cycpattern_check("abc", "bcde") == False
        assert cycpattern_check("abc", "def") == False
        assert cycpattern_check("abc", "abcde") == False
        assert cycpattern_check("abcde", "fgh") == False
        assert cycpattern_check("abcde", "abcdef") == False
        assert cycpattern_check("aaaaa", "bbbbb") == False
        assert cycpattern_check("aaaaa", "aaaaaa") == False
        assert cycpattern_check("aaaaa", "b") == False

    def test_empty_string_cases(self):
        assert cycpattern_check("", "") == True
        assert cycpattern_check("abc", "") == True
        assert cycpattern_check("", "abc") == False

    def test_same_string_cases(self):
        assert cycpattern_check("abc", "abc") == True
        assert cycpattern_check("abab", "abab") == True

    def test_edge_cases(self):
        assert cycpattern_check("a", "a") == True
        assert cycpattern_check("a", "b") == False
        assert cycpattern_check("aa", "a") == True
        assert cycpattern_check("aa", "aa") == True
        assert cycpattern_check("aa", "ab") == False
        assert cycpattern_check("aba", "ba") == True
        assert cycpattern_check("aba", "ab") == True
        assert cycpattern_check("aba", "a") == True
        assert cycpattern_check("aba", "b") == True
        assert cycpattern_check("aba", "aba") == True
        assert cycpattern_check("aba", "bab") == True
        assert cycpattern_check("aba", "baa") == True