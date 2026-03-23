import pytest
import math


# Focus: Substring Presence
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

def test_substring_presence_positive():
    assert cycpattern_check("hello", "ell") == True

def test_substring_presence_negative():
    assert cycpattern_check("abcd", "abd") == False

def test_substring_presence_rotation():
    assert cycpattern_check("abab", "baa") == True

# Focus: Rotation Handling
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

def test_rotation_substring_present():
    assert cycpattern_check("hello", "ell") == True

def test_rotation_substring_not_present():
    assert cycpattern_check("abcd", "abd") == False

def test_rotation_substring_present_complex():
    assert cycpattern_check("abab", "baa") == True

# Focus: Edge Cases (Empty Strings/Null Inputs)
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
    if not a or not b:
        return False
    n = len(b)
    for i in range(n):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False

def test_empty_string_a():
    assert cycpattern_check("", "abc") == False

def test_empty_string_b():
    assert cycpattern_check("abc", "") == False

def test_both_empty_strings():
    assert cycpattern_check("", "") == False