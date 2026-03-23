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
    if n == 0:
        return False
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

    def test_negative_cases(self):
        assert cycpattern_check("abcd", "abd") == False
        assert cycpattern_check("whassup", "psus") == False
        assert cycpattern_check("efef", "eeff") == False
        assert cycpattern_check("abc", "abcd") == False
        assert cycpattern_check("abc", "bcde") == False
        assert cycpattern_check("abc", "cda") == False
        assert cycpattern_check("abc", "abcde") == False
        assert cycpattern_check("abc", "def") == False
        assert cycpattern_check("abc", "") == False
        assert cycpattern_check("", "abc") == False
        assert cycpattern_check("", "") == False

    def test_edge_cases(self):
        assert cycpattern_check("a", "a") == True
        assert cycpattern_check("a", "b") == False
        assert cycpattern_check("aa", "a") == True
        assert cycpattern_check("aa", "aa") == True
        assert cycpattern_check("aa", "ab") == False
        assert cycpattern_check("abcabc", "bca") == True
        assert cycpattern_check("abcabc", "cab") == True
        assert cycpattern_check("abcabc", "abc") == True
        assert cycpattern_check("abcabc", "bcab") == True
        assert cycpattern_check("abcabc", "cabc") == True
        assert cycpattern_check("abcabc", "abca") == False
        assert cycpattern_check("abcabc", "bcaba") == False

    def test_type_checking(self):
        with pytest.raises(TypeError):
            cycpattern_check(123, "abc")
        with pytest.raises(TypeError):
            cycpattern_check("abc", 123)
        with pytest.raises(TypeError):
            cycpattern_check(123, 123)