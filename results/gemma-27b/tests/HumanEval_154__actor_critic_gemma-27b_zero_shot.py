
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
    n = len(b)
    for i in range(n):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False

def test_cycpattern_check_basic_true():
    assert cycpattern_check("hello","ell") == True

def test_cycpattern_check_basic_false():
    assert cycpattern_check("abcd","abd") == False

def test_cycpattern_check_whassup():
    assert cycpattern_check("whassup","psus") == False

def test_cycpattern_check_abab():
    assert cycpattern_check("abab","baa") == True

def test_cycpattern_check_efef():
    assert cycpattern_check("efef","eeff") == False

def test_cycpattern_check_himenss():
    assert cycpattern_check("himenss","simen") == True

def test_cycpattern_check_empty_b():
    assert cycpattern_check("hello","") == True

def test_cycpattern_check_empty_a():
    assert cycpattern_check("","ell") == False

def test_cycpattern_check_a_shorter_than_b_no_match():
    assert cycpattern_check("ab","abc") == False

def test_cycpattern_check_b_is_rotation_of_a():
    assert cycpattern_check("abcdef","defabc") == True

def test_cycpattern_check_long_strings_true():
    assert cycpattern_check("thisisalongstringwithpattern","pattern") == True

def test_cycpattern_check_long_strings_false():
    assert cycpattern_check("thisisalongstringwithoutpattern","pattern") == False

def test_cycpattern_check_repeated_chars_no_match():
    assert cycpattern_check("aaaaa","aaaab") == False

def test_cycpattern_check_repeated_chars_match():
    assert cycpattern_check("aaaaa","aa") == True

def test_cycpattern_check_special_chars_true():
    assert cycpattern_check("!@#$%^","@#$") == True

def test_cycpattern_check_special_chars_false():
    assert cycpattern_check("!@#$%^","@#$x") == False

def test_cycpattern_check_b_much_longer_than_a():
    assert cycpattern_check("abc", "abcdefg") == False

def test_cycpattern_check_unicode():
    assert cycpattern_check("你好世界","世界你") == True

def test_cycpattern_check_numbers():
    assert cycpattern_check("12345","345") == True

def test_cycpattern_check_same_strings():
    assert cycpattern_check("abc","abc") == True

def test_cycpattern_check_b_single_char_no_match():
    assert cycpattern_check("abcdef","z") == False

def test_cycpattern_check_complex_unicode():
    assert cycpattern_check("你好世界！😊","世界你！") == True

def test_cycpattern_check_mixed_chars():
    assert cycpattern_check("a1b2c3d","2c3") == True