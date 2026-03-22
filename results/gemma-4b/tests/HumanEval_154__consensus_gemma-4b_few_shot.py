def test_cycpattern_check_basic():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_empty():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_single_char():
    assert cycpattern_check("abc", "a") == True
    assert cycpattern_check("abc", "b") == False
    assert cycpattern_check("abc", "c") == True

def test_cycpattern_check_same_string():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_check_rotation():
    assert cycpattern_check("abcd", "bcda") == True
    assert cycpattern_check("abcd", "cdab") == True
    assert cycpattern_check("abcd", "dabc") == True
    assert cycpattern_check("abcd", "abdc") == False