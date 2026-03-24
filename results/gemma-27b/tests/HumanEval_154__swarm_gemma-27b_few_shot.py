
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

def test_cycpattern_check_long_a_short_b_no_match():
    assert cycpattern_check("aaaaaaaaab", "bbbb") == False

def test_cycpattern_check_long_a_short_b_no_match_2():
    assert cycpattern_check("aaaaaaaaaa", "b") == False