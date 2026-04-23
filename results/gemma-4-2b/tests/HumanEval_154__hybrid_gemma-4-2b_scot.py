
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
    if b in a:
        return True
    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False


def test_empty_strings():
    assert cycpattern_check("", "") == True

def test_b_is_empty():
    assert cycpattern_check("abc", "") == True
    assert cycpattern_check("", "") == True

def test_a_is_empty():
    assert cycpattern_check("", "abc") == True
    assert cycpattern_check("abc", "") == True

def test_b_is_substring_of_a():
    assert cycpattern_check("abc", "ab") == True
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("world", "orl") == True

def test_b_is_rotation_of_a():
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == True
    assert cycpattern_check("abcde", "cdeab") == True

def test_no_rotation_of_b_in_a():
    assert cycpattern_check("abcd", "efg") == False
    assert cycpattern_check("whassup", "psut") == False
    assert cycpattern_check("hello", "xyz") == False

def test_a_equals_b():
    assert cycpattern_check("abc", "abc") == True

def test_different_lengths():
    assert cycpattern_check("abc", "abcd") == False
    assert cycpattern_check("abcd", "abc") == False
    assert cycpattern_check("abc", "abcdef") == False

def test_long_strings():
    long_a = "abcdefghijklmnopqrstuvwxyz" * 10
    long_b = "xyz" * 5
    assert cycpattern_check(long_a, long_b) == True

def test_repeating_characters():
    assert cycpattern_check("aaaa", "aaa") == True
    assert cycpattern_check("aabb", "abb") == True
    assert cycpattern_check("ababab", "abab") == True

def test_mixed_cases():
    assert cycpattern_check("HelloWorld", "loW") == True
    assert cycpattern_check("HelloWorld", "hello") == True
    assert cycpattern_check("HelloWorld", "WORLD") == False