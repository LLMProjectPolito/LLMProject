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
        assert cycpattern_check("abcde", "cde") == True
        assert cycpattern_check("abcde", "eabc") == True
        assert cycpattern_check("abcde", "bcdea") == True
        assert cycpattern_check("abcde", "deabc") == True
        assert cycpattern_check("abcde", "eabcd") == True
        assert cycpattern_check("aaaaa", "aaaa") == True
        assert cycpattern_check("aaaaa", "aaaaa") == True
        assert cycpattern_check("aaaaa", "aa") == True
        assert cycpattern_check("aaaaa", "a") == True
        assert cycpattern_check("abcabc", "bca") == True
        assert cycpattern_check("abcabc", "cab") == True
        assert cycpattern_check("abcabc", "abc") == True
        assert cycpattern_check("abcabc", "bca") == True
        assert cycpattern_check("abcabc", "cba") == False

    def test_negative_cases(self):
        assert cycpattern_check("abcd", "abd") == False
        assert cycpattern_check("whassup", "psus") == False
        assert cycpattern_check("efef", "eeff") == False
        assert cycpattern_check("abc", "abcd") == False
        assert cycpattern_check("abc", "bcde") == False
        assert cycpattern_check("abc", "xyz") == False
        assert cycpattern_check("abc", "abcde") == False
        assert cycpattern_check("abc", "cde") == False
        assert cycpattern_check("abc", "deabc") == False
        assert cycpattern_check("abc", "bcda") == False
        assert cycpattern_check("abc", "abcd") == False
        assert cycpattern_check("abc", "dabc") == False
        assert cycpattern_check("abc", "ab") == False
        assert cycpattern_check("abc", "ac") == False
        assert cycpattern_check("abc", "bc") == False
        assert cycpattern_check("abc", "c") == False
        assert cycpattern_check("abc", "") == False
        assert cycpattern_check("", "abc") == False
        assert cycpattern_check("", "") == False

    def test_empty_strings(self):
        assert cycpattern_check("", "") == False
        assert cycpattern_check("abc", "") == False
        assert cycpattern_check("", "abc") == False

    def test_single_character_strings(self):
        assert cycpattern_check("a", "a") == True
        assert cycpattern_check("a", "b") == False
        assert cycpattern_check("b", "a") == False
        assert cycpattern_check("aa", "a") == True
        assert cycpattern_check("a", "aa") == False

    def test_identical_strings(self):
        assert cycpattern_check("abc", "abc") == True
        assert cycpattern_check("aaaa", "aaaa") == True

    def test_substring_at_start(self):
        assert cycpattern_check("abcdef", "abc") == True

    def test_substring_at_end(self):
        assert cycpattern_check("abcdef", "def") == True

    def test_substring_in_middle(self):
        assert cycpattern_check("abcdef", "cde") == True

    def test_long_strings(self):
        long_a = "abcdefghijklmnopqrstuvwxyz" * 10
        long_b = "xyz"
        assert cycpattern_check(long_a, long_b) == True

    def test_special_characters(self):
        assert cycpattern_check("!@#$%^", "$%^") == True
        assert cycpattern_check("!@#$%^", "%$^") == True
        assert cycpattern_check("!@#$%^", "#$%") == False