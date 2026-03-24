
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
    if not a or not b:
        return False
    if b in a or b in a[1:] or b in a[:-1]:
        return True
    else:
        return False

def test_cycpattern_check_positive():
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == True
    assert cycpattern_check("whassup","psus") == False
    assert cycpattern_check("abab","baa") == True
    assert cycpattern_check("himenss","simen") == True
    assert cycpattern_check("abcabc","abc") == True
    assert cycpattern_check("abcabc","bca") == True
    assert cycpattern_check("abcabc","cab") == True

def test_cycpattern_check_negative():
    assert cycpattern_check("abcd","abc") == False
    assert cycpattern_check("abcd","efgh") == False
    assert cycpattern_check("hello","world") == False
    assert cycpattern_check("whassup","hello") == False
    assert cycpattern_check("abab","cdef") == False
    assert cycpattern_check("himenss","hello") == False

def test_cycpattern_check_empty_b_string():
    assert cycpattern_check("abcd","") == True
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_equal_strings():
    assert cycpattern_check("abc","abc") == True
    assert cycpattern_check("abc","bac") == True
    assert cycpattern_check("abc","cab") == True

def test_cycpattern_check_long_strings():
    assert cycpattern_check("abcdefghijk","cdefghij") == True
    assert cycpattern_check("abcdefghijk","ghi") == True
    assert cycpattern_check("abcdefghijk","jklm") == False
    assert cycpattern_check("abcdefghijk","abc") == False
    assert cycpattern_check("abcdefghijk","efgh") == True
    assert cycpattern_check("abcdefghijk","ijk") == True
    assert cycpattern_check("abcdefghijk","abcdefghijk") == True

def test_cycpattern_check_b_at_start():
    assert cycpattern_check("abcdef","abc") == True

def test_cycpattern_check_b_at_end():
    assert cycpattern_check("abcdef","def") == True

def test_cycpattern_check_b_middle():
    assert cycpattern_check("abcdef","cde") == True