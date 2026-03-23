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

class TestCycPatternCheck:
    def test_positive_cases(self):
        assert cycpattern_check("hello", "ell") == True
        assert cycpattern_check("abab", "baa") == True
        assert cycpattern_check("himenss", "simen") == True
        assert cycpattern_check("abcde", "cdeab") == True
        assert cycpattern_check("abcde", "eabcd") == True
        assert cycpattern_check("abcde", "bcdea") == True
        assert cycpattern_check("abcde", "cdeab") == True
        assert cycpattern_check("abcde", "deabc") == True
        assert cycpattern_check("abcde", "eabdc") == False

    def test_negative_cases(self):
        assert cycpattern_check("abcd", "abd") == False
        assert cycpattern_check("whassup", "psus") == False
        assert cycpattern_check("efef", "eeff") == False
        assert cycpattern_check("abc", "def") == False
        assert cycpattern_check("abc", "abcd") == False
        assert cycpattern_check("abcd", "abcde") == False
        assert cycpattern_check("a", "b") == False
        assert cycpattern_check("", "a") == False
        assert cycpattern_check("a", "") == False
        assert cycpattern_check("", "") == False

    def test_edge_cases(self):
        assert cycpattern_check("aaaa", "aa") == True
        assert cycpattern_check("aaaa", "aaa") == True
        assert cycpattern_check("aaaa", "aaaa") == True
        assert cycpattern_check("aaaa", "aaaaa") == False
        assert cycpattern_check("ababab", "bababa") == True
        assert cycpattern_check("ababab", "ababab") == True
        assert cycpattern_check("ababab", "baba") == True
        assert cycpattern_check("ababab", "aba") == True
        assert cycpattern_check("ababab", "bab") == True
        assert cycpattern_check("ababab", "ab") == True
        assert cycpattern_check("ababab", "ba") == True
        assert cycpattern_check("ababab", "a") == True
        assert cycpattern_check("ababab", "b") == True
        assert cycpattern_check("ababab", "abababx") == False

    def test_type_checking(self):
        with pytest.raises(TypeError):
            cycpattern_check(123, "abc")
        with pytest.raises(TypeError):
            cycpattern_check("abc", 123)
        with pytest.raises(TypeError):
            cycpattern_check(123, 123)