
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

class TestCycPatternCheck:
    def test_positive_cases(self):
        assert cycpattern_check("hello", "ell") == True
        assert cycpattern_check("abab", "baa") == True
        assert cycpattern_check("himenss", "simen") == True
        assert cycpattern_check("abcde", "cde") == True
        assert cycpattern_check("abcde", "eab") == False
        assert cycpattern_check("abcde", "dea") == False
        assert cycpattern_check("abcde", "abc") == True
        assert cycpattern_check("abcde", "bcd") == True
        assert cycpattern_check("abcde", "cde") == True
        assert cycpattern_check("abcde", "deab") == False
        assert cycpattern_check("abcde", "bcdea") == True
        assert cycpattern_check("abcde", "eabcd") == True
        assert cycpattern_check("abcde", "abcde") == True
        assert cycpattern_check("aaaaa", "aaaa") == True
        assert cycpattern_check("aaaaa", "aaaaa") == True
        assert cycpattern_check("aaaaa", "aa") == True
        assert cycpattern_check("aaaaa", "aaa") == True
        assert cycpattern_check("aaaaa", "aaaaa") == True
        assert cycpattern_check("abcabc", "bca") == True
        assert cycpattern_check("abcabc", "cab") == True
        assert cycpattern_check("abcabc", "abc") == True
        assert cycpattern_check("abcabc", "cba") == False

    def test_negative_cases(self):
        assert cycpattern_check("abcd", "abd") == False
        assert cycpattern_check("whassup", "psus") == False
        assert cycpattern_check("efef", "eeff") == False
        assert cycpattern_check("abc", "abcd") == False
        assert cycpattern_check("a", "aa") == False
        assert cycpattern_check("", "a") == False
        assert cycpattern_check("a", "") == True
        assert cycpattern_check("", "") == True
        assert cycpattern_check("abc", "def") == False
        assert cycpattern_check("abcdef", "fedcba") == False
        assert cycpattern_check("abcdef", "fedc") == False

    def test_edge_cases(self):
        assert cycpattern_check("a", "a") == True
        assert cycpattern_check("aa", "a") == True
        assert cycpattern_check("a", "aa") == False
        assert cycpattern_check("abc", "abc") == True
        assert cycpattern_check("abc", "cba") == False
        assert cycpattern_check("abc", "cab") == True
        assert cycpattern_check("abc", "bca") == True
        assert cycpattern_check("abc", "acb") == False
        assert cycpattern_check("abc", "bac") == False
        assert cycpattern_check("abc", "abcabc") == False
        assert cycpattern_check("abcabc", "abc") == True
        assert cycpattern_check("abcabc", "bca") == True
        assert cycpattern_check("abcabc", "cab") == True
        assert cycpattern_check("abcabc", "abcabc") == True
        assert cycpattern_check("abcabc", "bcabca") == True
        assert cycpattern_check("abcabc", "cabcab") == True
        assert cycpattern_check("abcabc", "abcabcabc") == False