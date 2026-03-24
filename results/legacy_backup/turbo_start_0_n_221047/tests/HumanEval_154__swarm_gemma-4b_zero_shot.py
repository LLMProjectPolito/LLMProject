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
    if b in a or any(rotation in a for rotation in rotate(b)):
        return True
    else:
        return False

def rotate(s):
    return s[1:] + s[0]

def test_cycpattern_check_abcd_abd():
    assert cycpattern_check("abcd", "abd") == False

def test_cycpattern_check_hello_ell():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_whassup_psus():
    assert cycpattern_check("whassup", "psus") == False

def test_cycpattern_check_abab_baa():
    assert cycpattern_check("abab", "baa") == True

def test_cycpattern_check_efef_eeff():
    assert cycpattern_check("efef", "eeff") == False

def test_cycpattern_check_himenss_simen():
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_empty_b():
    assert cycpattern_check("abcd", "") == True