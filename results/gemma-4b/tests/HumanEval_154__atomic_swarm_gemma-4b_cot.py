
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

def test_basic():
    assert cycpattern_check("abcd","abd") == False

def test_empty_string():
    assert cycpattern_check("", "a") == False
    assert cycpattern_check("abc", "") == True
    assert cycpattern_check("", "") == True

import pytest

def test_empty_string():
    assert cycpattern_check("", "a") == False
    assert cycpattern_check("abc", "") == True
    assert cycpattern_check("", "") == True