
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

def test_cycpattern_check_basic_true():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_basic_false():
    assert cycpattern_check("abcd", "abd") == False

def test_cycpattern_check_rotation_true():
    assert cycpattern_check("abab", "baa") == True

def test_cycpattern_check_no_match():
    assert cycpattern_check("efef", "eeff") == False

def test_cycpattern_check_longer_substring():
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_empty_b():
    assert cycpattern_check("abc", "") == True

def test_cycpattern_check_empty_a():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_both_empty():
    assert cycpattern_check("", "") == True

def test_cycpattern_check_a_shorter_than_b():
    assert cycpattern_check("ab", "abc") == False

def test_cycpattern_check_same_strings():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_check_b_is_a():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_check_b_rotation_of_a():
    assert cycpattern_check("abcabc", "bca") == True

def test_cycpattern_check_b_rotation_of_a_longer():
    assert cycpattern_check("abcabcabc", "cab") == True

def test_cycpattern_check_b_rotation_of_a_not_substring():
    assert cycpattern_check("abcabc", "cba") == False

def test_cycpattern_check_special_characters():
    assert cycpattern_check("a!b@c#", "b@c#") == True

def test_cycpattern_check_special_characters_no_match():
    assert cycpattern_check("a!b@c#", "c#b@") == False

def test_cycpattern_check_numbers():
    assert cycpattern_check("12345", "234") == True

def test_cycpattern_check_numbers_no_match():
    assert cycpattern_check("12345", "351") == False

def test_cycpattern_check_mixed_characters():
    assert cycpattern_check("a1b2c3d", "b2c3") == True

def test_cycpattern_check_mixed_characters_no_match():
    assert cycpattern_check("a1b2c3d", "c3a1") == False