
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
    """
    Test the edge case where the second word is longer than the first word.
    No rotation of a longer string can be a substring of a shorter string.
    """
    assert cycpattern_check("abc", "abcd") == False

def test_cycpattern_check_rotation_is_substring():
    """
    Test that the function returns True when b is not a substring of a,
    but a rotation of b (in this case 'aba') is a substring of a.
    """
    assert cycpattern_check("abacaba", "aab") == True