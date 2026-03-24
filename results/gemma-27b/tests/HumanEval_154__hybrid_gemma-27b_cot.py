
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
    def test_cycpattern_check_basic_true(self):
        assert cycpattern_check("hello", "ell") == True

    def test_cycpattern_check_basic_false(self):
        assert cycpattern_check("abcd", "abd") == False

    def test_cycpattern_check_rotation_true(self):
        assert cycpattern_check("abab", "baa") == True

    def test_cycpattern_check_no_match(self):
        assert cycpattern_check("efef", "eeff") == False

    def test_cycpattern_check_longer_substring(self):
        assert cycpattern_check("himenss", "simen") == True

    def test_cycpattern_check_empty_b(self):
        assert cycpattern_check("abc", "") == False

    def test_cycpattern_check_empty_a(self):
        assert cycpattern_check("", "abc") == False

    def test_cycpattern_check_both_empty(self):
        assert cycpattern_check("", "") == False

    def test_cycpattern_check_a_shorter_than_b(self):
        assert cycpattern_check("ab", "abc") == False

    def test_cycpattern_check_same_strings(self):
        assert cycpattern_check("abc", "abc") == True

    def test_cycpattern_check_b_is_a(self):
        assert cycpattern_check("abc", "abc") == True

    def test_cycpattern_check_b_rotation_of_a(self):
        assert cycpattern_check("abcabc", "bca") == True

    def test_cycpattern_check_b_rotation_of_a_longer(self):
        assert cycpattern_check("abcabcabc", "cab") == True

    def test_cycpattern_check_repeated_chars(self):
        assert cycpattern_check("aaaaa", "aa") == True

    def test_cycpattern_check_repeated_chars_no_match(self):
        assert cycpattern_check("aaaaa", "bb") == False

    def test_cycpattern_check_special_chars(self):
        assert cycpattern_check("!@#$%^", "$%^") == True

    def test_cycpattern_check_special_chars_no_match(self):
        assert cycpattern_check("!@#$%^", "&*()") == False

    def test_cycpattern_check_mixed_case(self):
        assert cycpattern_check("Hello", "ell") == False

    def test_cycpattern_check_long_strings_true(self):
        assert cycpattern_check("thisisalongstringwithsomepattern", "stringwith") == True

    def test_cycpattern_check_long_strings_false(self):
        assert cycpattern_check("thisisalongstringwithsomepattern", "notpresent") == False

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
        assert cycpattern_check("waterbottle", "bottlewater") == True
        assert cycpattern_check("abcde", "cdeab") == True

    def test_long_strings(self):
        long_string = "a" * 1000
        assert cycpattern_check(long_string, "a" * 500) == True
        assert cycpattern_check(long_string, "b" * 500) == False

    def test_different_lengths(self):
        assert cycpattern_check("abc", "abcd") == False
        assert cycpattern_check("abcd", "abc") == True

    def test_special_characters(self):
        assert cycpattern_check("a!b@c#", "b@c#a") == True
        assert cycpattern_check("a!b@c#", "c#a!b") == True
        assert cycpattern_check("a!b@c#", "d$e%f^") == False

    def test_case_sensitivity(self):
        assert cycpattern_check("Hello", "ell") == False
        assert cycpattern_check("Hello", "Hello") == True

    def test_numeric_strings(self):
        assert cycpattern_check("123456", "345612") == True
        assert cycpattern_check("123456", "789012") == False

    def test_edge_case_single_char(self):
        assert cycpattern_check("a", "a") == True
        assert cycpattern_check("ab", "b") == True
        assert cycpattern_check("ab", "c") == False