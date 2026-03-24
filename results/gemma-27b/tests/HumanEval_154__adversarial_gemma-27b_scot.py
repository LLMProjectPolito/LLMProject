
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
    if not b:
        return True  # Empty string is always a substring

    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True

    return False


def test_empty_strings():
    assert cycpattern_check("", "") == True
    assert cycpattern_check("abc", "") == True
    assert cycpattern_check("", "abc") == False

def test_b_longer_than_a():
    assert cycpattern_check("abc", "abcd") == False

def test_b_is_substring_of_a():
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("abcdef", "bcd") == True

def test_rotation_needed():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("himenss", "simen") == True

def test_no_match():
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("efef", "eeff") == False

def test_a_and_b_same():
    assert cycpattern_check("hello", "hello") == True

def test_a_contains_b_multiple_times():
    assert cycpattern_check("ababab", "ab") == True

def test_b_is_a():
    assert cycpattern_check("abc", "abc") == True

def test_case_sensitivity():
    assert cycpattern_check("Hello", "ell") == False
    assert cycpattern_check("hello", "Ell") == False