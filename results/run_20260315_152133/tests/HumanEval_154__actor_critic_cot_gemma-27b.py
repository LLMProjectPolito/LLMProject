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

def test_basic_cases():
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == True
    assert cycpattern_check("whassup","psus") == False
    assert cycpattern_check("abab","baa") == True
    assert cycpattern_check("efef","eeff") == False
    assert cycpattern_check("himenss","simen") == True

def test_b_longer_than_a():
    assert cycpattern_check("abc","abcd") == False
    assert cycpattern_check("abc","abcde") == False

def test_b_equal_to_a():
    assert cycpattern_check("abc","abc") == True

def test_substring_cases():
    assert cycpattern_check("abcdef","def") == True
    assert cycpattern_check("abcdef","cde") == True

def test_repeated_characters():
    assert cycpattern_check("aaaa","aa") == True

def test_edge_cases():
    assert cycpattern_check("abcde","bcdea") == True
    assert cycpattern_check("abcde","cdeab") == True
    assert cycpattern_check("abcde","deabc") == True
    assert cycpattern_check("abcde","eabcd") == True
    assert cycpattern_check("abcde","abcdf") == False
    assert cycpattern_check("abcde","abced") == False

def test_empty_string_b():
    assert cycpattern_check("abcde", "") == True

def test_empty_string_a():
    assert cycpattern_check("", "abc") == False
    assert cycpattern_check("", "") == True

def test_single_character_b():
    assert cycpattern_check("abab", "b") == True

def test_long_repeating_pattern():
    long_a = "a" * 1000
    long_b = "a" * 500
    assert cycpattern_check(long_a, long_b) == True

    long_a = "abcdef" * 100
    long_b = "defabc" * 50
    assert cycpattern_check(long_a, long_b) == True