
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
    n = len(b)
    for i in range(n):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False

def test_cycpattern_check_empty_b():
    assert cycpattern_check("abcd", "") == True

def test_cycpattern_check_example1():
    assert cycpattern_check("abcd","abd") == False

def test_cycpattern_check_example2():
    assert cycpattern_check("hello","ell") == True

def test_cycpattern_check_example3():
    assert cycpattern_check("whassup","psus") == False

def test_cycpattern_check_example4():
    assert cycpattern_check("abab","baa") == True

def test_cycpattern_check_example5():
    assert cycpattern_check("efef","eeff") == False

def test_cycpattern_check_example6():
    assert cycpattern_check("himenss","simen") == True