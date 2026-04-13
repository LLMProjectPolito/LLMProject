
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
    if len(b) > len(a):
        return False

    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True

    return False


def test_empty_strings():
    assert cycpattern_check("", "") == False

def test_b_longer_than_a():
    assert cycpattern_check("abc", "abcd") == False

def test_b_is_substring_of_a():
    assert cycpattern_check("hello", "ell") == True

def test_rotation_is_substring_of_a():
    assert cycpattern_check("waterbottle", "erbottlewat") == True

def test_no_match():
    assert cycpattern_check("abcd", "abd") == False

def test_identical_strings():
    assert cycpattern_check("hello", "hello") == True

def test_repeating_patterns():
    assert cycpattern_check("ababab", "aba") == True
    assert cycpattern_check("ababab", "bab") == True

def test_edge_case_1():
    assert cycpattern_check("abab", "baa") == True

def test_edge_case_2():
    assert cycpattern_check("efef", "eeff") == False

def test_edge_case_3():
    assert cycpattern_check("himenss", "simen") == True

def test_another_no_match():
    assert cycpattern_check("whassup", "psus") == False

def test_b_at_end():
    assert cycpattern_check("abcdef", "def") == True

def test_b_at_beginning():
    assert cycpattern_check("abcdef", "abc") == True