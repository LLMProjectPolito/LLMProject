import pytest

def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) < len(b):
        a, b = b, a

    for i in range(1, len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True

    return False

def test_cycpattern_check_basic():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_empty_strings():
    assert cycpattern_check("", "") == True
    assert cycpattern_check("a", "") == False
    assert cycpattern_check("", "a") == False

def test_cycpattern_check_single_char():
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("a", "b") == False
    assert cycpattern_check("b", "a") == False
    assert cycpattern_check("b", "b") == True

def test_cycpattern_check_longer_strings():
    assert cycpattern_check("abcdefg", "def") == True
    assert cycpattern_check("abcdefg", "gfed") == True
    assert cycpattern_check("abcdefg", "cdef") == True
    assert cycpattern_check("abcdefg", "efg") == True
    assert cycpattern_check("abcdefg", "abcdef") == True
    assert cycpattern_check("abcdefg", "gfedc") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdef") == True
    assert cycpattern_check("abcdefg", "abcdef") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    
def test_cycpattern_check_edge_cases():
    assert cycpattern_check("abc", "cba") == True
    assert cycpattern_check("abc", "bca") == True
    assert cycpattern_check("abc", "cab") == True
    assert cycpattern_check("abc", "c") == False
    assert cycpattern_check("abc", "ab") == False
    assert cycpattern_check("abc", "a") == False
    assert cycpattern_check("abc", "bc") == False
    assert cycpattern_check("abc", "c") == False
    
def test_cycpattern_check_with_duplicates():
    assert cycpattern_check("aabbcc", "aabb") == True
    assert cycpattern_check("aabbcc", "aabbcc") == True
    assert cycpattern_check("aabbcc", "aabb") == False
    
def test_cycpattern_check_complex():
    assert cycpattern_check("abac", "bac") == True
    assert cycpattern_check("abac", "cba") == False
    assert cycpattern_check("abac", "acb") == True
    assert cycpattern_check("abac", "bac") == True
    
def test_cycpattern_check_different_lengths():
    assert cycpattern_check("abc", "abcd") == False
    assert cycpattern_check("abc", "bc") == False
    assert cycpattern_check("abc", "c") == False
    assert cycpattern_check("abc", "ab") == False