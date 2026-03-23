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
    if n == 0:
        return True
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

def test_cycpattern_check_a_equals_b():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_check_b_longer_than_a():
    assert cycpattern_check("abc", "abcd") == False

def test_cycpattern_check_repeated_pattern():
    assert cycpattern_check("ababab", "aba") == True

def test_cycpattern_check_long_strings():
    assert cycpattern_check("thisisalongstring", "long") == True

def test_cycpattern_check_long_strings_false():
    assert cycpattern_check("thisisalongstring", "short") == False

def test_cycpattern_check_special_characters():
    assert cycpattern_check("a!b@c#", "b@c#") == True

def test_cycpattern_check_special_characters_false():
    assert cycpattern_check("a!b@c#", "b@d#") == False

def test_cycpattern_check_numbers():
    assert cycpattern_check("123456", "345") == True

def test_cycpattern_check_numbers_false():
    assert cycpattern_check("123456", "457") == False