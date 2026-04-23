
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
    n = len(a)
    m = len(b)

    if m > n:
        return False

    for i in range(m):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True

    return False

@pytest.suite()
class TestCycPatternCheck:

    def test_empty_strings(self):
        assert cycpattern_check("", "") == False
        assert cycpattern_check("abc", "") == False
        assert cycpattern_check("", "abc") == False

    def test_basic_cases(self):
        assert cycpattern_check("abcd", "abd") == False
        assert cycpattern_check("hello", "ell") == True
        assert cycpattern_check("whassup", "psus") == False
        assert cycpattern_check("abab", "baa") == True
        assert cycpattern_check("efef", "eeff") == False
        assert cycpattern_check("himenss", "simen") == True

    def test_longer_strings(self):
        assert cycpattern_check("abcdefgh", "def") == True
        assert cycpattern_check("abcdefgh", "gh") == True
        assert cycpattern_check("abcdefgh", "abc") == True
        assert cycpattern_check("abcdefgh", "efgh") == True
        assert cycpattern_check("abcdefgh", "cdef") == True
        assert cycpattern_check("abcdefgh", "fgh") == True
        assert cycpattern_check("abcdefgh", "a") == True
        assert cycpattern_check("abcdefgh", "h") == True
        assert cycpattern_check("abcdefgh", "x") == False

    def test_same_strings(self):
        assert cycpattern_check("abc", "abc") == True
        assert cycpattern_check("hello", "hello") == True

    def test_substring_at_start(self):
        assert cycpattern_check("abcdef", "abc") == True

    def test_substring_at_end(self):
        assert cycpattern_check("abcdef", "def") == True

    def test_no_rotation_present(self):
        assert cycpattern_check("abcdefg", "xyz") == False

    def test_repeated_characters(self):
        assert cycpattern_check("aaaaa", "aaa") == True
        assert cycpattern_check("aaaaa", "aab") == False

    def test_edge_cases(self):
        assert cycpattern_check("a", "a") == True
        assert cycpattern_check("a", "b") == False
        assert cycpattern_check("ab", "ba") == True
        assert cycpattern_check("ab", "ab") == True
        assert cycpattern_check("ab", "ac") == False