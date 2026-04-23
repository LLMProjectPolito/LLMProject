
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
        assert cycpattern_check("abc", "") == False
        assert cycpattern_check("", "abc") == False

    def test_basic_true_cases(self):
        assert cycpattern_check("hello", "ell") == True
        assert cycpattern_check("abab", "baa") == True
        assert cycpattern_check("himenss", "simen") == True
        assert cycpattern_check("waterbottle", "erbottlewat") == True
        assert cycpattern_check("abcabc", "bca") == True

    def test_basic_false_cases(self):
        assert cycpattern_check("abcd", "abd") == False
        assert cycpattern_check("whassup", "psus") == False
        assert cycpattern_check("efef", "eeff") == False
        assert cycpattern_check("abc", "def") == False
        assert cycpattern_check("abc", "abcd") == False

    def test_same_string(self):
        assert cycpattern_check("abc", "abc") == True
        assert cycpattern_check("aaaa", "aaaa") == True

    def test_substring_at_start(self):
        assert cycpattern_check("abcdef", "abc") == True

    def test_substring_at_end(self):
        assert cycpattern_check("abcdef", "def") == True

    def test_substring_in_middle(self):
        assert cycpattern_check("abcdef", "cde") == True

    def test_rotation_needed(self):
        assert cycpattern_check("waterbottle", "bottlewat") == True
        assert cycpattern_check("abcd", "cdab") == True

    def test_long_strings(self):
        long_string = "abcdefghijklmnopqrstuvwxyz" * 10
        assert cycpattern_check(long_string, "uvwxyz") == True
        assert cycpattern_check(long_string, "zyxwvu") == True
        assert cycpattern_check(long_string, "mnopqrst") == True
        assert cycpattern_check(long_string, "abcdefgh") == True
        assert cycpattern_check(long_string, "zyxwvutsrqponmlkjihgfedcba") == False

    def test_edge_cases(self):
        assert cycpattern_check("a", "a") == True
        assert cycpattern_check("a", "b") == False
        assert cycpattern_check("aa", "a") == True
        assert cycpattern_check("aa", "aa") == True
        assert cycpattern_check("aa", "aaa") == False
        assert cycpattern_check("abcde", "cdea") == True
        assert cycpattern_check("abcde", "eabcd") == True

    def test_special_characters(self):
        assert cycpattern_check("!@#$%^", "$%^!") == True
        assert cycpattern_check("!@#$%^", "^$#@!") == True
        assert cycpattern_check("!@#$%^", "abc") == False

    def test_mixed_case(self):
        assert cycpattern_check("Hello", "ell") == False
        assert cycpattern_check("Hello", "llo") == False
        assert cycpattern_check("Hello", "Hel") == False