def test_cycpattern_check_basic_true():
    assert cycpattern_check("hello","ell") == True

def test_cycpattern_check_basic_false():
    assert cycpattern_check("abcd","abd") == False

def test_cycpattern_check_rotation_true():
    assert cycpattern_check("abab","baa") == True

def test_cycpattern_check_rotation_false():
    assert cycpattern_check("efef","eeff") == False

def test_cycpattern_check_longer_rotation_true():
    assert cycpattern_check("himenss","simen") == True

def test_cycpattern_check_same_string():
    assert cycpattern_check("abc","abc") == True

def test_cycpattern_check_empty_string():
    assert cycpattern_check("","a") == False
    assert cycpattern_check("a","") == False
    assert cycpattern_check("","") == False

def test_cycpattern_check_single_char_true():
    assert cycpattern_check("a","a") == True

def test_cycpattern_check_single_char_false():
    assert cycpattern_check("a","b") == False

def test_cycpattern_check_complex_true():
    assert cycpattern_check("thisisateststring","test") == True

def test_cycpattern_check_complex_false():
    assert cycpattern_check("thisisateststring","testing") == False

def test_cycpattern_check_overlapping_rotation_true():
    assert cycpattern_check("aaaa","aaa") == True

def test_cycpattern_check_overlapping_rotation_false():
    assert cycpattern_check("aaaa","aab") == False