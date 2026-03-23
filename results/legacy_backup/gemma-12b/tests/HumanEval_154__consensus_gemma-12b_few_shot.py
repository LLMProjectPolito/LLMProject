def test_cycpattern_check_positive():
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("himenss", "simen") == True
    assert cycpattern_check("abcabc", "bca") == True
    assert cycpattern_check("abcabc", "cab") == True
    assert cycpattern_check("abcabc", "abc") == True
    assert cycpattern_check("abcabc", "cba") == False
    assert cycpattern_check("abcabc", "bcab") == True
    assert cycpattern_check("abcabc", "bcaba") == False

def test_cycpattern_check_negative():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("abc", "abcd") == False
    assert cycpattern_check("abc", "bcde") == False
    assert cycpattern_check("abc", "cda") == False

def test_cycpattern_check_empty_string():
    assert cycpattern_check("", "") == True
    assert cycpattern_check("abc", "") == True
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_single_char():
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("a", "b") == False
    assert cycpattern_check("aa", "a") == True
    assert cycpattern_check("aa", "aa") == True
    assert cycpattern_check("aa", "ab") == False

def test_cycpattern_check_long_strings():
    assert cycpattern_check("abcdefghijklmnopqrstuvwxyz", "def") == True
    assert cycpattern_check("abcdefghijklmnopqrstuvwxyz", "zyx") == True
    assert cycpattern_check("abcdefghijklmnopqrstuvwxyz", "abc") == True
    assert cycpattern_check("abcdefghijklmnopqrstuvwxyz", "xyz") == True
    assert cycpattern_check("abcdefghijklmnopqrstuvwxyz", "defg") == False
    assert cycpattern_check("abcdefghijklmnopqrstuvwxyz", "zyxw") == False