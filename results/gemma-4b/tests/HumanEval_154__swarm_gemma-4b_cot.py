
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
import math

def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if b in a or any(rotation in a for rotation in rotations(b)):
        return True
    else:
        return False

def rotations(s):
    """Helper function to generate all rotations of a string."""
    return [s[i:] + s[:i] for i in range(len(s))]

def test_empty_b():
    assert cycpattern_check("abcd", "") == True

def test_empty_string():
    assert cycpattern_check("abc", "") == True
    assert cycpattern_check("", "abc") == False
    assert cycpattern_check("", "") == True

def test_cycpattern_check_edge_case(a, b):
    assert cycpattern_check(a, b) == True