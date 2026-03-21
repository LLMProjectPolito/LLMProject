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

    if a == b:
        return True

    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False

def test_empty_string_a():
    assert cycpattern_check("", "abc") == False

def test_empty_string_b():
    assert cycpattern_check("abc", "") == False

def test_empty_strings_a_and_b():
    assert cycpattern_check("", "") == False

def test_b_longer_than_a():
    assert cycpattern_check("abc", "abcd") == False

def test_a_equals_b():
    assert cycpattern_check("abc", "abc") == True

def test_b_is_prefix_of_a():
    assert cycpattern_check("abcdef", "abc") == True

def test_b_is_suffix_of_a():
    assert cycpattern_check("abcdef", "def") == True

def test_b_is_empty():
    assert cycpattern_check("abcdef", "") == True

def test_example_1():
    assert cycpattern_check("abcd", "abd") == False

def test_example_2():
    assert cycpattern_check("hello", "ell") == True

def test_example_3():
    assert cycpattern_check("whassup", "psus") == False

def test_example_4():
    assert cycpattern_check("abab", "baa") == True

def test_example_5():
    assert cycpattern_check("efef", "eeff") == False

def test_example_6():
    assert cycpattern_check("himenss", "simen") == True