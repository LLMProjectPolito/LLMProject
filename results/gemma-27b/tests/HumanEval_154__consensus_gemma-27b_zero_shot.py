
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

def test_cycpattern_check_1():
    assert cycpattern_check("abcd","abd") == False

def test_cycpattern_check_2():
    assert cycpattern_check("hello","ell") == True

def test_cycpattern_check_3():
    assert cycpattern_check("whassup","psus") == False

def test_cycpattern_check_4():
    assert cycpattern_check("abab","baa") == True

def test_cycpattern_check_5():
    assert cycpattern_check("efef","eeff") == False

def test_cycpattern_check_6():
    assert cycpattern_check("himenss","simen") == True

def test_cycpattern_check_7():
    assert cycpattern_check("abc","abc") == True

def test_cycpattern_check_8():
    assert cycpattern_check("abc","bca") == True

def test_cycpattern_check_9():
    assert cycpattern_check("abc","cab") == True

def test_cycpattern_check_10():
    assert cycpattern_check("abc","acb") == False

def test_cycpattern_check_11():
    assert cycpattern_check("aaaaa","aa") == True

def test_cycpattern_check_12():
    assert cycpattern_check("aaaaa","aaa") == True

def test_cycpattern_check_13():
    assert cycpattern_check("aaaaa","aaaa") == True

def test_cycpattern_check_14():
    assert cycpattern_check("aaaaa","aaaaa") == True

def test_cycpattern_check_15():
    assert cycpattern_check("aaaaa","aaaaab") == False

def test_cycpattern_check_16():
    assert cycpattern_check("","") == True

def test_cycpattern_check_17():
    assert cycpattern_check("abc","") == True

def test_cycpattern_check_18():
    assert cycpattern_check("","abc") == False

def test_cycpattern_check_19():
    assert cycpattern_check("longstring","short") == False

def test_cycpattern_check_20():
    assert cycpattern_check("longstring","string") == True

def test_cycpattern_check_18_alt():
    assert cycpattern_check("waterbottle","erbottlewat") == True

def test_cycpattern_check_19_alt():
    assert cycpattern_check("waterbottle","rbottlewat") == False

def test_cycpattern_check_11_alt():
    assert cycpattern_check("aaaa","aa") == True

def test_cycpattern_check_12_alt():
    assert cycpattern_check("aaaa","aaa") == True

def test_cycpattern_check_13_alt():
    assert cycpattern_check("aaaa","a") == True

def test_cycpattern_check_14_alt():
    assert cycpattern_check("a","aaaa") == False