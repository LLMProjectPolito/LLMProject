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

    def test_positive_case_1(self):
        assert cycpattern_check("hello", "ell") == True

    def test_positive_case_2(self):
        assert cycpattern_check("abab", "baa") == True

    def test_positive_case_3(self):
        assert cycpattern_check("himenss", "simen") == True

    def test_negative_case_1(self):
        assert cycpattern_check("abcd", "abd") == False

    def test_negative_case_2(self):
        assert cycpattern_check("whassup", "psus") == False

    def test_negative_case_3(self):
        assert cycpattern_check("efef", "eeff") == False

    def test_empty_string_b(self):
        assert cycpattern_check("hello", "") == False

    def test_empty_string_a(self):
        assert cycpattern_check("", "ell") == False

    def test_both_empty_strings(self):
        assert cycpattern_check("", "") == False

    def test_b_longer_than_a(self):
        assert cycpattern_check("abc", "abcd") == False

    def test_identical_strings(self):
        assert cycpattern_check("hello", "hello") == True

    def test_b_is_substring_no_rotation(self):
        assert cycpattern_check("abcdef", "abc") == True

    def test_rotation_is_substring(self):
        assert cycpattern_check("abcdef", "defabc") == True

    def test_case_sensitive(self):
        assert cycpattern_check("Hello", "ell") == False

    def test_special_characters(self):
        assert cycpattern_check("abc!@#", "@#abc!") == True

    def test_numbers(self):
        assert cycpattern_check("12345", "34512") == True

    def test_long_strings(self):
        long_a = "abcdefghijklmnopqrstuvwxyz" * 2
        long_b = "uvwxyzabcdefghijklmno"
        assert cycpattern_check(long_a, long_b) == True