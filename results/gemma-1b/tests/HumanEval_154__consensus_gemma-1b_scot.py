
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
        return False
    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False

def test_cycpattern_check_example1():
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == True
    assert cycpattern_check("whassup","psus") == False
    assert cycpattern_check("abab","baa") == True
    assert cycpattern_check("efef","eeff") == False
    assert cycpattern_check("himenss","simen") == True

def test_cycpattern_check_empty_string():
    assert cycpattern_check("", "") == True
    assert cycpattern_check("a", "") == False
    assert cycpattern_check("", "a") == False

def test_cycpattern_check_single_char():
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("a", "b") == False
    assert cycpattern_check("b", "a") == False
    assert cycpattern_check("b", "b") == True

def test_cycpattern_check_same_string():
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("a", "b") == False
    assert cycpattern_check("b", "a") == False
    assert cycpattern_check("b", "b") == True

def test_cycpattern_check_longer_string():
    assert cycpattern_check("abcdefg","cdefg") == True
    assert cycpattern_check("abcde","cde") == True
    assert cycpattern_check("abcdefg","efg") == True
    assert cycpattern_check("abcdefg","fgh") == True
    assert cycpattern_check("abcdefg","gh") == True
    assert cycpattern_check("abcdefg","d") == False
    assert cycpattern_check("abcdefg","e") == False
    assert cycpattern_check("abcdefg","f") == False