def test_cycpattern_check_positive():
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("himenss", "simen") == True
    assert cycpattern_check("abcabc", "bca") == True
    assert cycpattern_check("abcabc", "cab") == True
    assert cycpattern_check("abcabc", "abc") == True
    assert cycpattern_check("abcabc", "bcab") == True
    assert cycpattern_check("abcabc", "cabc") == True
    assert cycpattern_check("abcabc", "bcabc") == True
    assert cycpattern_check("abcabc", "abcabc") == True

def test_cycpattern_check_negative():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("abc", "d") == False
    assert cycpattern_check("abc", "abcd") == False
    assert cycpattern_check("abc", "cba") == False
    assert cycpattern_check("abc", "abcde") == False

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

def test_cycpattern_check_longer_pattern():
    assert cycpattern_check("thisisalongstring", "longstr") == True
    assert cycpattern_check("thisisalongstring", "strlong") == True
    assert cycpattern_check("thisisalongstring", "string") == True
    assert cycpattern_check("thisisalongstring", "isalong") == True
    assert cycpattern_check("thisisalongstring", "alongst") == True
    assert cycpattern_check("thisisalongstring", "longstri") == True
    assert cycpattern_check("thisisalongstring", "longstrin") == True
    assert cycpattern_check("thisisalongstring", "longstring") == True
    assert cycpattern_check("thisisalongstring", "notfound") == False