
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
    if not b:
        return True
    if b in a or any(rotation in a for rotation in rotate(b)):
        return True
    else:
        return False

def rotate(s):
    return s[1:] + s[0]

def test_cycpattern_check_basic():
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == True
    assert cycpattern_check("whassup","psus") == False
    assert cycpattern_check("abab","baa") == True
    assert cycpattern_check("efef","eeff") == False
    assert cycpattern_check("himenss","simen") == True

def test_cycpattern_check_empty_b():
    assert cycpattern_check("abcd", "") == True
    assert cycpattern_check("", "") == True

def test_cycpattern_check_empty_a():
    assert cycpattern_check("", "abd") == False

def test_cycpattern_check_same_word():
    assert cycpattern_check("hello", "hello") == True
    assert cycpattern_check("abab", "abab") == True

def test_cycpattern_check_substring_at_end():
    assert cycpattern_check("abcdef", "def") == True
    assert cycpattern_check("abcdef", "cdef") == True
    assert cycpattern_check("abcdef", "bcdef") == True

def test_cycpattern_check_substring_in_middle():
    assert cycpattern_check("abcdef", "cdef") == True
    assert cycpattern_check("abcdef", "bcdef") == True

def test_cycpattern_check_no_match():
    assert cycpattern_check("abcdef", "xyz") == False
    assert cycpattern_check("abcdef", "abce") == False

def test_cycpattern_check_long_words():
    assert cycpattern_check("abcdefghijk", "ijk") == True
    assert cycpattern_check("abcdefghijk", "ghijk") == True
    assert cycpattern_check("abcdefghijk", "abcdefghijk") == True

def test_cycpattern_check_overlapping_rotations():
    assert cycpattern_check("abababa", "aba") == True
    assert cycpattern_check("abababa", "bab") == True

def test_cycpattern_check_special_characters():
    assert cycpattern_check("!@#$%^", "!@#") == True
    assert cycpattern_check("!@#$%^", "$%^!") == True

def test_cycpattern_check_numbers():
    assert cycpattern_check("123456", "345") == True
    assert cycpattern_check("123456", "654") == True