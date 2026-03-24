
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


# Focus: Substring Search Variations
import pytest

def test_cycpattern_check_basic_true():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_basic_false():
    assert cycpattern_check("abcd", "abd") == False

def test_cycpattern_check_rotation_true():
    assert cycpattern_check("abab", "baa") == True

def test_cycpattern_check_no_match():
    assert cycpattern_check("efef", "eeff") == False

def test_cycpattern_check_longer_string():
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_empty_b():
    assert cycpattern_check("abc", "") == True

def test_cycpattern_check_empty_a():
    assert cycpattern_check("", "abc") == False

# Focus: Rotational Equivalence
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

def test_rotational_equivalence_positive():
    assert cycpattern_check("hello", "ell") == True

def test_rotational_equivalence_negative():
    assert cycpattern_check("abcd", "abd") == False

def test_rotational_equivalence_complex():
    assert cycpattern_check("abab", "baa") == True

# Focus: Edge Cases - Empty/Null Strings
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

    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False

def test_empty_a():
    assert cycpattern_check("", "abc") == False

def test_empty_b():
    assert cycpattern_check("abc", "") == False

def test_both_empty():
    assert cycpattern_check("", "") == False