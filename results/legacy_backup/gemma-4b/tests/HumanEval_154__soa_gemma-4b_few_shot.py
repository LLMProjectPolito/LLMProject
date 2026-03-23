def test_cycpattern_check_basic():
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == True
    assert cycpattern_check("whassup","psus") == False
    assert cycpattern_check("abab","baa") == True
    assert cycpattern_check("efef","eeff") == False
    assert cycpattern_check("himenss","simen") == True

def test_cycpattern_check_empty():
    assert cycpattern_check("", "") == True

def test_cycpattern_check_single_char():
    assert cycpattern_check("abc", "a") == True
    assert cycpattern_check("abc", "b") == False
    assert cycpattern_check("abc", "c") == True

def test_cycpattern_check_longer_string():
    assert cycpattern_check("thisisatest", "test") == True
    assert cycpattern_check("thisisatest", "testi") == False
    assert cycpattern_check("thisisatest", "stis") == True
    assert cycpattern_check("thisisatest", "tesi") == False
    assert cycpattern_check("thisisatest", "testsa") == False