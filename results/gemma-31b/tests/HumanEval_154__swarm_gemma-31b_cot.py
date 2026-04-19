
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
import math

def test_cycpattern_check_b_longer_than_a():
    # If the word to be rotated (b) is longer than the target word (a),
    # no rotation of b can possibly be a substring of a.
    assert cycpattern_check("abc", "abcd") == False

def test_cycpattern_check_full_rotation():
    # This case tests if the function correctly identifies when the second word 
    # is a full cyclic rotation of the first word.
    assert cycpattern_check("abcde", "cdeab") == True