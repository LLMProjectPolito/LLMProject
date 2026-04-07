
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
        return True
    if len(b) > len(a):
        return False

    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True

    return False

def test_empty_strings():
    assert cycpattern_check("", "") == True

def test_b_longer_than_a():
    assert cycpattern_check("abc", "abcd") == False

def test_b_is_substring_of_a():
    assert cycpattern_check("hello world", "world") == True

def test_b_rotation_is_substring_of_a():
    assert cycpattern_check("hello", "ell") == True

def test_no_match():
    assert cycpattern_check("abcd", "abd") == False

def test_a_and_b_same():
    assert cycpattern_check("test", "test") == True

def test_a_contains_b_multiple_times():
    assert cycpattern_check("abababa", "aba") == True

def test_edge_case_1():
    assert cycpattern_check("abab", "baa") == True

def test_edge_case_2():
    assert cycpattern_check("efef", "eeff") == False

def test_edge_case_3():
    assert cycpattern_check("himenss", "simen") == True

def test_long_strings():
    a = "abcdefghijklmnopqrstuvwxyz" * 2
    b = "uvwxyzabcdefghijklm"
    assert cycpattern_check(a, b) == True

def test_long_strings_no_match():
    a = "abcdefghijklmnopqrstuvwxyz" * 2
    b = "zyxwvutsrqponmlkjihgfedcba"
    assert cycpattern_check(a, b) == False

def test_b_is_empty():
    assert cycpattern_check("abc", "") == True