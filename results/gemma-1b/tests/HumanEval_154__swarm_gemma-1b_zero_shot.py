import pytest
import math

def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    s1 = a
    s2 = b
    s3 = s2
    s4 = s2.replace(s2[0], "")
    s5 = s2.replace(s2[-1], "")

    if s1 in s3:
        return True
    if s3 in s1:
        return True
    if s4 in s2:
        return True
    if s5 in s2:
        return True
    return False

def test_cycpattern_check():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True

    # Additional tests for robustness
    assert cycpattern_check("abc", "cba") == True
    assert cycpattern_check("abc", "bac") == True
    assert cycpattern_check("abc", "bca") == True
    assert cycpattern_check("abc", "cba") == False
    assert cycpattern_check("abcd", "dcb") == True
    assert cycpattern_check("abcd", "dc") == True
    assert cycpattern_check("abcd", "d") == False
    assert cycpattern_check("abcd", "abc") == False
    assert cycpattern_check("abcd", "ab") == False
    assert cycpattern_check("abcd", "a") == False
    assert cycpattern_check("abcd", "b") == False
    assert cycpattern_check("abcd", "c") == False
    assert cycpattern_check("abcd", "d") == False
    assert cycpattern_check("abcd", "e") == False
    assert cycpattern_check("abcd", "f") == False
    assert cycpattern_check("abcd", "g") == False
    assert cycpattern_check("abcd", "h") == False
    assert cycpattern_check("abcd", "i") == False
    assert cycpattern_check("abcd", "j") == False
    assert cycpattern_check("abcd", "k") == False
    assert cycpattern_check("abcd", "l") == False
    assert cycpattern_check("abcd", "m") == False
    assert cycpattern_check("abcd", "n") == False
    assert cycpattern_check("abcd", "o") == False
    assert cycpattern_check("abcd", "p") == False
    assert cycpattern_check("abcd", "q") == False
    assert cycpattern_check("abcd", "r") == False
    assert cycpattern_check("abcd", "s") == False
    assert cycpattern_check("abcd", "t") == False
    assert cycpattern_check("abcd", "u") == False
    assert cycpattern_check("abcd", "v") == False
    assert cycpattern_check("abcd", "w") == False
    assert cycpattern_check("abcd", "x") == False
    assert cycpattern_check("abcd", "y") == False
    assert cycpattern_check("abcd", "z") == False