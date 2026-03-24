
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
    pass

def test_empty_b():
    """
    Test case for when the second word (b) is empty.
    The function should return True because an empty string is always a substring.
    """
    assert cycpattern_check("hello", "") == True
    assert cycpattern_check("abc", "") == True

def test_cycpattern_check_1():
    assert cycpattern_check("abcd","abd") == False

def test_cycpattern_check_2():
    assert cycpattern_check("hello","ell") == True

def test_cycpattern_check_3():
    assert cycpattern_check("whassup","psus") == False

def test_cycpattern_check_4():
    assert cycpattern_check("abab","baa") == True

def test_cycpattern_check_5():
    assert cycpattern_check("efef","eeff") == False

def test_cycpattern_check_6():
    assert cycpattern_check("himenss","simen") == True