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

def test_cycpattern_check_basic_true():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_basic_false():
    assert cycpattern_check("abcd", "abd") == False

def test_cycpattern_check_whassup():
    assert cycpattern_check("whassup", "psus") == False

def test_cycpattern_check_abab():
    assert cycpattern_check("abab", "baa") == True

def test_cycpattern_check_efef():
    assert cycpattern_check("efef", "eeff") == False

def test_cycpattern_check_himenss():
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_empty_b():
    assert cycpattern_check("abc", "") == True

def test_cycpattern_check_empty_a():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_both_empty():
    assert cycpattern_check("", "") == True

def test_cycpattern_check_a_longer_than_b():
    assert cycpattern_check("abcdef", "abc") == True

def test_cycpattern_check_b_longer_than_a():
    assert cycpattern_check("abc", "abcdef") == False

def test_cycpattern_check_same_string():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_check_repeated_pattern():
    assert cycpattern_check("ababab", "ab") == True

def test_cycpattern_check_no_match():
    assert cycpattern_check("abcdefg", "xyz") == False

def test_cycpattern_check_b_at_end_of_a():
    assert cycpattern_check("abcdef", "ef") == True

def test_cycpattern_check_b_at_beginning_of_a():
    assert cycpattern_check("abcdef", "abc") == True

def test_cycpattern_check_b_is_rotation_of_substring():
    assert cycpattern_check("waterbottle", "erbottlewat") == True

def test_cycpattern_check_long_strings():
    a = "a" * 1000
    b = "a" * 500
    assert cycpattern_check(a, b) == True

def test_cycpattern_check_long_strings_no_match():
    a = "a" * 1000
    b = "b" * 500
    assert cycpattern_check(a, b) == False