def test_cycpattern_check_basic_true():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_basic_false():
    assert cycpattern_check("abcd", "abd") == False

def test_cycpattern_check_rotation_true():
    assert cycpattern_check("abab", "baa") == True

def test_cycpattern_check_no_match():
    assert cycpattern_check("whassup", "psus") == False

def test_cycpattern_check_different_lengths_false():
    assert cycpattern_check("efef", "eeff") == False

def test_cycpattern_check_longer_pattern_true():
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_empty_pattern():
    assert cycpattern_check("abc", "") == True

def test_cycpattern_check_empty_string():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_both_empty():
    assert cycpattern_check("", "") == True

def test_cycpattern_check_pattern_longer_than_string():
    assert cycpattern_check("abc", "abcd") == False

def test_cycpattern_check_repeated_chars():
    assert cycpattern_check("aaaaa", "aa") == True

def test_cycpattern_check_repeated_chars_no_match():
    assert cycpattern_check("aaaaa", "bbb") == False