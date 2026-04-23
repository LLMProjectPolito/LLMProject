
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

@pytest.suite()
class TestCycpatternCheck:

    def test_empty_string_a(self):
        assert cycpattern_check("", "abc") == False

    def test_empty_string_b(self):
        assert cycpattern_check("abc", "") == False

    def test_both_empty_strings(self):
        assert cycpattern_check("", "") == False

    def test_basic_true(self):
        assert cycpattern_check("hello", "ell") == True

    def test_basic_false(self):
        assert cycpattern_check("abcd", "abd") == False

    def test_rotation_true(self):
        assert cycpattern_check("abab", "baa") == True

    def test_rotation_false(self):
        assert cycpattern_check("efef", "eeff") == False

    def test_another_true(self):
        assert cycpattern_check("himenss", "simen") == True

    def test_another_false(self):
        assert cycpattern_check("whassup", "psus") == False

    def test_same_string(self):
        assert cycpattern_check("abc", "abc") == True

    def test_b_longer_than_a(self):
        assert cycpattern_check("abc", "abcdef") == False

    def test_a_longer_than_b(self):
        assert cycpattern_check("abcdef", "abc") == True

    def test_repeated_characters(self):
        assert cycpattern_check("aaaaa", "aaa") == True

    def test_edge_case_1(self):
        assert cycpattern_check("a", "a") == True

    def test_edge_case_2(self):
        assert cycpattern_check("a", "b") == False

    def test_edge_case_3(self):
        assert cycpattern_check("abcabc", "bca") == True

    def test_edge_case_4(self):
        assert cycpattern_check("abcabc", "cab") == True