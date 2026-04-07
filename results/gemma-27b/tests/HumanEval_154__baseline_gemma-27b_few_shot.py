
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

def test_cycpattern_check_basic_true():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_basic_false():
    assert cycpattern_check("abcd", "abd") == False

def test_cycpattern_check_rotation_true():
    assert cycpattern_check("abab", "baa") == True

def test_cycpattern_check_no_rotation_true():
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_false_case():
    assert cycpattern_check("efef", "eeff") == False

def test_cycpattern_check_empty_b():
    assert cycpattern_check("hello", "") == True

def test_cycpattern_check_empty_a():
    assert cycpattern_check("", "ell") == False

def test_cycpattern_check_both_empty():
    assert cycpattern_check("", "") == True

def test_cycpattern_check_b_longer_than_a():
    assert cycpattern_check("abc", "abcd") == False

def test_cycpattern_check_same_string():
    assert cycpattern_check("test", "test") == True

def test_cycpattern_check_long_strings_true():
    assert cycpattern_check("thisisalongstring", "longstring") == True

def test_cycpattern_check_long_strings_false():
    assert cycpattern_check("thisisalongstring", "notpresent") == False