
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
    if not b:
        return True
    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
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
    assert cycpattern_check("abcd","abce") == False
    assert cycpattern_check("abcd","efgh") == False
    assert cycpattern_check("efef","eeff") == False
    assert cycpattern_check("test","tes") == False
    assert cycpattern_check("test","est") == False
    assert cycpattern_check("test","tse") == False

def test_cycpattern_check_empty_b():
    assert cycpattern_check("abcd","") == True

def test_cycpattern_check_empty_a():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_same_string():
    assert cycpattern_check("abc","abc") == True
    assert cycpattern_check("abc","bac") == True
    assert cycpattern_check("abc","cab") == True

def test_cycpattern_check_long_strings():
    assert cycpattern_check("abcdefghijk","cdefghij") == True
    assert cycpattern_check("abcdefghijk","ghi") == True
    assert cycpattern_check("abcdefghijk","jklm") == False
    assert cycpattern_check("abcdefghijk","abcdefghijk") == True
    assert cycpattern_check("abcdefghijk","hgfedcba") == True
    assert cycpattern_check("abcdefghijk","ijkabcde") == False