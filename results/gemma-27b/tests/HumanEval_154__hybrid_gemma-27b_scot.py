
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
    n = len(a)
    m = len(b)

    if m > n:
        return False

    for i in range(m):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True

    return False

def test_cycpattern_check_basic_true():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_basic_false():
    assert cycpattern_check("abcd", "abd") == False

def test_cycpattern_check_b_longer_than_a():
    assert cycpattern_check("abc", "abcd") == False

def test_cycpattern_check_identical_strings():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_check_empty_string_b():
    assert cycpattern_check("abc", "") == True

def test_cycpattern_check_empty_string_a():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_repeating_pattern():
    assert cycpattern_check("ababab", "aba") == True

def test_cycpattern_check_example_1():
    assert cycpattern_check("abcd","abd") == False

def test_cycpattern_check_example_2():
    assert cycpattern_check("hello","ell") == True

def test_cycpattern_check_example_3():
    assert cycpattern_check("whassup","psus") == False

def test_cycpattern_check_example_4():
    assert cycpattern_check("abab","baa") == True

def test_cycpattern_check_example_5():
    assert cycpattern_check("efef","eeff") == False

def test_cycpattern_check_example_6():
    assert cycpattern_check("himenss","simen") == True