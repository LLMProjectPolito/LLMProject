
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

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
import pytest

def test_cycpattern_check_empty_strings():
    assert cycpattern_check("", "") == False
    assert cycpattern_check("abc", "") == False
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_basic_cases():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_longer_string():
    assert cycpattern_check("abcdefgh", "def") == True
    assert cycpattern_check("abcdefgh", "gh") == True
    assert cycpattern_check("abcdefgh", "abc") == True
    assert cycpattern_check("abcdefgh", "efgh") == True
    assert cycpattern_check("abcdefgh", "fed") == False

def test_cycpattern_check_same_string():
    assert cycpattern_check("abc", "abc") == True
    assert cycpattern_check("xyz", "xyz") == True

def test_cycpattern_check_substring_at_start():
    assert cycpattern_check("abcdef", "abc") == True

def test_cycpattern_check_substring_at_end():
    assert cycpattern_check("abcdef", "def") == True

def test_cycpattern_check_no_match():
    assert cycpattern_check("abcdef", "ghi") == False

def test_cycpattern_check_repeated_characters():
    assert cycpattern_check("aaaaa", "aaa") == True
    assert cycpattern_check("aaaaa", "aab") == False

def test_cycpattern_check_different_lengths():
    assert cycpattern_check("abc", "abcd") == False
    assert cycpattern_check("abcd", "abc") == True