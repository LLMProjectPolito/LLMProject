
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
        assert cycpattern_check(long_string, "xyz") == True
        assert cycpattern_check(long_string, "zyx") == True
        assert cycpattern_check(long_string, "abcdef") == True
        assert cycpattern_check(long_string, "uvwxyz") == False

    def test_edge_cases(self):
        assert cycpattern_check("a", "a") == True
        assert cycpattern_check("a", "b") == False
        assert cycpattern_check("aa", "a") == True
        assert cycpattern_check("aa", "aa") == True
        assert cycpattern_check("aa", "aaa") == False
        assert cycpattern_check("abcde", "cdea") == False
        assert cycpattern_check("abcde", "eabc") == False

    def test_repeated_patterns(self):
        assert cycpattern_check("aaaaaa", "aa") == True
        assert cycpattern_check("ababab", "bab") == True
        assert cycpattern_check("ababab", "aba") == True

    def test_case_sensitivity(self):
        assert cycpattern_check("Hello", "ell") == False
        assert cycpattern_check("hello", "Ell") == False

    def test_special_characters(self):
        assert cycpattern_check("a!b@c#", "!b@c") == True
        assert cycpattern_check("a!b@c#", "b@c#a") == True
        assert cycpattern_check("a!b@c#", "c#a!b") == True

    def test_numbers(self):
        assert cycpattern_check("123456", "234") == True
        assert cycpattern_check("123456", "4561") == True

    def test_edge_case_same_length_no_match(self):
        assert cycpattern_check("abc", "bac") == False

    def test_edge_case_same_length_match(self):
        assert cycpattern_check("abc", "abc") == True

    def test_b_longer_than_a(self):
        assert cycpattern_check("abc", "abcdef") == False