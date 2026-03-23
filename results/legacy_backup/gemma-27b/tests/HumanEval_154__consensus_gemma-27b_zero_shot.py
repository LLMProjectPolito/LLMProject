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
    assert cycpattern_check("aaaa","aa") == True

def test_cycpattern_check_11():
    assert cycpattern_check("aaaa","aaa") == True

def test_cycpattern_check_12():
    assert cycpattern_check("aaaa","a") == True

def test_cycpattern_check_13():
    assert cycpattern_check("a","aaaa") == False

def test_cycpattern_check_14():
    assert cycpattern_check("","") == False

def test_cycpattern_check_15():
    assert cycpattern_check("abc","") == False

def test_cycpattern_check_16():
    assert cycpattern_check("","abc") == False

def test_cycpattern_check_17():
    assert cycpattern_check("waterbottle","erbottlewat") == True

def test_cycpattern_check_18():
    assert cycpattern_check("waterbottle","lewaterbot") == False

def test_cycpattern_check_19():
    assert cycpattern_check("waterbottle","rbottlewat") == False

def test_cycpattern_check_longer_string():
    assert cycpattern_check("thisisalongstring", "long") == True

def test_cycpattern_check_longer_string_false():
    assert cycpattern_check("thisisalongstring", "short") == False

def test_cycpattern_check_substring_at_start():
    assert cycpattern_check("abcdef", "abc") == True

def test_cycpattern_check_substring_at_end():
    assert cycpattern_check("abcdef", "def") == True

def test_cycpattern_check_substring_in_middle():
    assert cycpattern_check("abcdef", "cde") == True

def test_cycpattern_check_repeated_pattern():
    assert cycpattern_check("abababab", "aba") == True

def test_cycpattern_check_repeated_pattern_false():
    assert cycpattern_check("abababab", "babab") == False

def test_cycpattern_check_complex_rotation_false():
    assert cycpattern_check("waterbottle", "bottlewaterr") == False