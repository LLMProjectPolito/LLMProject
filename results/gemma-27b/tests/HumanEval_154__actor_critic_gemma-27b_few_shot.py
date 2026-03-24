
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") -> False
    cycpattern_check("hello","ell") -> True
    cycpattern_check("whassup","psus") -> False
    cycpattern_check("abab","baa") -> True
    cycpattern_check("efef","eeff") -> False
    cycpattern_check("himenss","simen") -> True

    """
    if not a or not b:
        return False

    if len(b) > len(a):
        return False

    if a == b:
        return True

    return b in (a + a)


import pytest

def test_basic1():
    assert cycpattern_check("abcd","abd") == False

def test_basic2():
    assert cycpattern_check("hello","ell") == True

def test_basic3():
    assert cycpattern_check("whassup","psus") == False

def test_basic4():
    assert cycpattern_check("abab","baa") == True

def test_basic5():
    assert cycpattern_check("efef","eeff") == False

def test_basic6():
    assert cycpattern_check("himenss","simen") == True

def test_empty_a():
    assert cycpattern_check("", "abc") == False

def test_empty_b():
    assert cycpattern_check("abc", "") == True

def test_empty_both():
    assert cycpattern_check("", "") == False

def test_len_b_greater():
    assert cycpattern_check("abc", "abcd") == False

def test_long_strings_true():
    a = "abcdefgh" * 100
    b = "defghabc"
    assert cycpattern_check(a, b) == True

def test_long_strings_false():
    a = "abcdefgh" * 100
    b = "defghabcx"
    assert cycpattern_check(a, b) == False

def test_identical():
    assert cycpattern_check("abc", "abc") == True

def test_special_chars():
    assert cycpattern_check("a!b@c#", "b@c#a") == True
    assert cycpattern_check("a!b@c#", "c#a!b") == True

def test_unicode():
    assert cycpattern_check("你好世界", "世界你好") == True
    assert cycpattern_check("你好世界", "好世") == True