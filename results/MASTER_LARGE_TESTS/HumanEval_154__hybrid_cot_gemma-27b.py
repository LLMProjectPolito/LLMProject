import pytest

def test_basic_cases():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True

def test_empty_string_cases():
    assert cycpattern_check("abc", "") == True
    assert cycpattern_check("", "abc") == False
    assert cycpattern_check("", "") == True

def test_identical_strings():
    assert cycpattern_check("abc", "abc") == True

def test_b_longer_than_a():
    assert cycpattern_check("abc", "abcd") == False

def test_rotations():
    assert cycpattern_check("waterbottle", "erbottlewat") == True
    assert cycpattern_check("waterbottle", "tlewaterbo") == True
    assert cycpattern_check("abcde", "cdeab") == True
    assert cycpattern_check("abcde", "eabcd") == True

def test_overlapping_patterns():
    assert cycpattern_check("ababab", "aba") == True
    assert cycpattern_check("ababab", "bab") == True
    assert cycpattern_check("abcabc", "bca") == True
    assert cycpattern_check("abcabc", "cab") == True

def test_repeated_characters():
    assert cycpattern_check("aaaaa", "aa") == True
    assert cycpattern_check("aaaaa", "aaa") == True
    assert cycpattern_check("ababab", "ab") == True
    assert cycpattern_check("ababab", "ba") == True
    assert cycpattern_check("aaaa", "aa") == True
    assert cycpattern_check("aaaa", "aaaab") == False

def test_edge_cases_lengths():
    assert cycpattern_check("abcdef", "bcdefg") == False
    assert cycpattern_check("abcdef", "bcdef") == True
    assert cycpattern_check("abcdef", "cdef") == True
    assert cycpattern_check("abcdefg", "bcdef") == True

def test_unicode_characters():
    assert cycpattern_check("你好世界", "世界你") == True
    assert cycpattern_check("你好世界", "好世") == True
    assert cycpattern_check("你好世界", "界世") == False

def test_long_strings():
    long_string = "a" * 1000
    assert cycpattern_check(long_string, "a" * 500) == True
    assert cycpattern_check(long_string, "b" * 500) == False

def test_no_match():
    assert cycpattern_check("abcdef", "xyz") == False

def test_boundary_conditions():
    assert cycpattern_check("abcdefg", "cdefgh") == False
    assert cycpattern_check("abcdefg", "defg") == True
    assert cycpattern_check("abcdefg", "efg") == True
    assert cycpattern_check("abcdefg", "fg") == True
    assert cycpattern_check("abcdefg", "g") == True
    assert cycpattern_check("abcdefg", "h") == False

def test_single_char_pattern():
    assert cycpattern_check("abc", "a") == True
    assert cycpattern_check("abc", "b") == True
    assert cycpattern_check("abc", "c") == True
    assert cycpattern_check("abc", "d") == False

def test_pattern_longer_than_string():
    assert cycpattern_check("abc", "abcd") == False
    assert cycpattern_check("a", "aa") == False