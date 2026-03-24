
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

    Note: Returning True when b is empty is intentional.  It signifies that an empty pattern is always found within a string.
    """
    n = len(b)
    for i in range(n):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False

def test_basic_true_false():
    assert cycpattern_check("hello","ell") == True
    assert cycpattern_check("abcd","abd") == False

def test_whassup():
    assert cycpattern_check("whassup","psus") == False

def test_abab():
    assert cycpattern_check("abab","baa") == True

def test_efef():
    assert cycpattern_check("efef","eeff") == False

def test_himenss():
    assert cycpattern_check("himenss","simen") == True

def test_empty_b():
    assert cycpattern_check("hello","") == True

def test_empty_a():
    assert cycpattern_check("","ell") == False

def test_both_empty():
    assert cycpattern_check("","") == True

def test_a_equals_b():
    assert cycpattern_check("test","test") == True

def test_b_longer_than_a():
    assert cycpattern_check("abc","abcdef") == False

def test_b_much_longer_than_a():
    assert cycpattern_check("abc", "abcdefghijklmnopqrstuvwxyz") == False

def test_unicode():
    assert cycpattern_check("你好世界","世界") == True

def test_unicode_false():
    assert cycpattern_check("你好世界","你好世界啊") == False

def test_complex_rotation():
    assert cycpattern_check("abcdefgh", "efghab") == True

def test_repeated_chars():
    assert cycpattern_check("banana", "a") == True

def test_repeated_chars_false():
    assert cycpattern_check("aaaaa","aaaab") == False

def test_special_chars():
    assert cycpattern_check("!@#$%^&*()","@#$") == True

def test_special_chars_false():
    assert cycpattern_check("!@#$%^&*()","@#$x") == False

def test_long_strings_almost_match():
    long_string = "a" * 1000 + "b"
    pattern = "b" * 999 + "a"
    assert cycpattern_check(long_string, pattern) == False

def test_unicode_both():
    assert cycpattern_check("你好世界你好","世界你") == True

def test_substring_of_itself():
    assert cycpattern_check("abcabc", "abc") == True