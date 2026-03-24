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
    if b in a or b in a[1:] or b in a[:-1]:
        return True
    else:
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
    assert cycpattern_check("abc","cab") == True

def test_cycpattern_check_9():
    assert cycpattern_check("abc","bca") == True

def test_cycpattern_check_10():
    assert cycpattern_check("abc","acb") == False

def test_cycpattern_check_11():
    assert cycpattern_check("a","a") == True

def test_cycpattern_check_12():
    assert cycpattern_check("a","b") == False

def test_cycpattern_check_13():
    assert cycpattern_check("","abd") == False

def test_cycpattern_check_14():
    assert cycpattern_check("abcd","") == True

def test_cycpattern_check_15():
    assert cycpattern_check("abc","abcde") == False