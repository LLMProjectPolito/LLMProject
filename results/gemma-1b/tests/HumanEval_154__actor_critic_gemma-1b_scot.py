
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

def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) == 0 or len(b) == 0:
        return False

    if len(a) == 1 and len(b) == 1:
        return a.lower() in b.lower()

    if len(a) == 1:
        return a.lower() in b.lower()

    if len(b) == 1:
        return b.lower() in a.lower()

    for i in range(1, len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True

    return False

def test_cycpattern_check():
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == True
    assert cycpattern_check("whassup","psus") == False
    assert cycpattern_check("abab","baa") == True
    assert cycpattern_check("efef","eeff") == False
    assert cycpattern_check("himenss","simen") == True

    # Edge cases
    assert cycpattern_check("", "") == False
    assert cycpattern_check("a", "") == False
    assert cycpattern_check("", "a") == False
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("abc", "cba") == True
    assert cycpattern_check("abc", "bac") == True
    assert cycpattern_check("abc", "bca") == True
    assert cycpattern_check("abc", "cab") == True
    assert cycpattern_check("abc", "cba") == False
    assert cycpattern_check("abcd", "dcb") == True
    assert cycpattern_check("abcd", "bcda") == True
    assert cycpattern_check("abcd", "bcda") == False
    assert cycpattern_check("abcde", "cde") == True
    assert cycpattern_check("abcde", "edc") == True
    assert cycpattern_check("abcde", "de") == True
    assert cycpattern_check("abcde", "e") == True
    assert cycpattern_check("abcde", "d") == True
    assert cycpattern_check("abcde", "e") == False
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("a", "b") == False
    assert cycpattern_check("ab", "ba") == True
    assert cycpattern_check("ab", "bc") == False
    assert cycpattern_check("abc", "cba") == False
    assert cycpattern_check("abc", "cab") == False
    assert cycpattern_check("abc", "bca") == False
    assert cycpattern_check("abc", "acb") == False
    assert cycpattern_check("abc", "bac") == False
    assert cycpattern_check("abc", "bca") == False
    assert cycpattern_check("abc", "cba") == False
    print("All test cases passed")