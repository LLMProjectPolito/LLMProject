
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
    n = len(a)
    m = len(b)

    if m > n:
        return False

    for i in range(m):
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
    assert cycpattern_check("abc","abc") == True
    assert cycpattern_check("abc","bca") == True
    assert cycpattern_check("abc","cab") == True
    assert cycpattern_check("abc","cba") == False
    assert cycpattern_check("aaaaa","aa") == True
    assert cycpattern_check("aaaaa","aaa") == True
    assert cycpattern_check("aaaaa","aaaa") == True
    assert cycpattern_check("aaaaa","aaaaa") == True
    assert cycpattern_check("aaaaa","aaaaaa") == False
    assert cycpattern_check("","") == True
    assert cycpattern_check("abc","") == True
    assert cycpattern_check("","abc") == False
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("a", "b") == False
    assert cycpattern_check("ababab","aba") == True
    assert cycpattern_check("ababab","bab") == True
    assert cycpattern_check("ababab","ab") == True
    assert cycpattern_check("ababab","b") == True
    assert cycpattern_check("ababab","c") == False
    assert cycpattern_check("longstring","short") == False
    assert cycpattern_check("longstring","long") == True
    assert cycpattern_check("longstring","gstri") == True
    assert cycpattern_check("longstring","string") == True
    assert cycpattern_check("longstring","ngstri") == True