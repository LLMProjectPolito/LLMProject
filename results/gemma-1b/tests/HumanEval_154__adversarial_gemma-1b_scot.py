
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

def test_cycpattern_check_empty_strings():
    assert cycpattern_check("", "") == False

def test_cycpattern_check_one_empty_string():
    assert cycpattern_check("abc", "") == False

def test_cycpattern_check_both_empty():
    assert cycpattern_check("", "") == False

def test_cycpattern_check_simple_case1():
    assert cycpattern_check("abcd", "abd") == False

def test_cycpattern_check_simple_case2():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_simple_case3():
    assert cycpattern_check("whassup", "psus") == False

def test_cycpattern_check_simple_case4():
    assert cycpattern_check("abab", "baa") == True

def test_cycpattern_check_simple_case5():
    assert cycpattern_check("efef", "eeff") == False

def test_cycpattern_check_simple_case6():
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_longer_strings():
    assert cycpattern_check("abcdefg", "def") == True

def test_cycpattern_check_longer_strings_no_match():
    assert cycpattern_check("abcdefg", "xyz") == False

def test_cycpattern_check_case_with_rotation():
    assert cycpattern_check("abc", "cba") == True

def test_cycpattern_check_case_with_rotation_2():
    assert cycpattern_check("abc", "bca") == True

def test_cycpattern_check_case_with_rotation_3():
    assert cycpattern_check("abc", "cab") == True