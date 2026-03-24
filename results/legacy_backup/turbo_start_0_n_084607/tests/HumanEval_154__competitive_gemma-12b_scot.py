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
        assert cycpattern_check("abcabc", "bca") == True
        assert cycpattern_check("rotation", "tati") == True
        assert cycpattern_check("abcdefg", "cdef") == True
        assert cycpattern_check("abcdefg", "efgab") == True
        assert cycpattern_check("abcdefg", "gfabcde") == True

    def test_negative_cases(self):
        assert cycpattern_check("abcd", "abd") == False
        assert cycpattern_check("whassup", "psus") == False
        assert cycpattern_check("efef", "eeff") == False
        assert cycpattern_check("abc", "abcd") == False
        assert cycpattern_check("abc", "def") == False
        assert cycpattern_check("abc", "cabx") == False
        assert cycpattern_check("abc", "xyz") == False
        assert cycpattern_check("aaaa", "aaab") == False

    def test_empty_string_cases(self):
        assert cycpattern_check("", "") == True
        assert cycpattern_check("abc", "") == True
        assert cycpattern_check("", "abc") == False

    def test_same_string_cases(self):
        assert cycpattern_check("abc", "abc") == True
        assert cycpattern_check("abc", "cba") == True

    def test_long_string_cases(self):
        long_a = "a" * 100
        long_b = "a" * 50
        assert cycpattern_check(long_a, long_b) == True

        long_a = "a" * 100
        long_b = "b" * 50
        assert cycpattern_check(long_a, long_b) == False

    def test_special_characters(self):
        assert cycpattern_check("!@#$%^", "$%^!") == True
        assert cycpattern_check("!@#$%^", "&*()") == False