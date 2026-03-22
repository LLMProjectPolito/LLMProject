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
    if not a or not b:
        return False

    for i in range(len(b)):
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

    def test_basic_false_cases(self):
        assert cycpattern_check("abcd", "abd") == False
        assert cycpattern_check("whassup", "psus") == False
        assert cycpattern_check("efef", "eeff") == False
        assert cycpattern_check("abc", "def") == False

    def test_substring_at_start(self):
        assert cycpattern_check("abcdef", "abc") == True

    def test_substring_at_end(self):
        assert cycpattern_check("abcdef", "def") == True

    def test_substring_in_middle(self):
        assert cycpattern_check("abcdef", "cde") == True

    def test_rotation_needed(self):
        assert cycpattern_check("waterbottle", "bottlewater") == True
        assert cycpattern_check("abcde", "cdeab") == True

    def test_long_strings(self):
        a = "a" * 1000 + "b" * 1000
        b = "b" * 500 + "a" * 500
        assert cycpattern_check(a, b) == True

    def test_identical_strings(self):
        assert cycpattern_check("abc", "abc") == True

    def test_case_sensitivity(self):
        assert cycpattern_check("Hello", "ell") == False
        assert cycpattern_check("hello", "Ell") == False

    def test_special_characters(self):
        assert cycpattern_check("a!b@c#", "b@c#a") == True
        assert cycpattern_check("a!b@c#", "c#a!b") == True
        assert cycpattern_check("a!b@c#", "d$e%f^") == False

    def test_numbers(self):
        assert cycpattern_check("123456", "345612") == True
        assert cycpattern_check("123456", "654321") == False