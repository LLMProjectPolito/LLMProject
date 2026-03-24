
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
    assert cycpattern_check("hello","ell") == True

def test_cycpattern_check_basic_false():
    assert cycpattern_check("abcd","abd") == False

def test_cycpattern_check_rotation_true():
    assert cycpattern_check("abab","baa") == True

def test_cycpattern_check_rotation_false():
    assert cycpattern_check("efef","eeff") == False

def test_cycpattern_check_longer_rotation_true():
    assert cycpattern_check("himenss","simen") == True

def test_cycpattern_check_same_word_true():
    assert cycpattern_check("word","word") == True

def test_cycpattern_check_empty_string_true():
    assert cycpattern_check("","") == True

def test_cycpattern_check_empty_pattern_true():
    assert cycpattern_check("word","") == True

def test_cycpattern_check_pattern_longer_than_string_false():
    assert cycpattern_check("abc","abcdef") == False

def test_cycpattern_check_pattern_with_spaces_true():
    assert cycpattern_check("hello world","world") == True

def test_cycpattern_check_pattern_with_spaces_false():
    assert cycpattern_check("hello world"," worl") == False

def test_cycpattern_check_case_sensitive_false():
    assert cycpattern_check("Hello","hello") == False

def test_cycpattern_check_case_sensitive_true():
    assert cycpattern_check("Hello","Hello") == True

def test_cycpattern_check_special_characters_true():
    assert cycpattern_check("!@#$%^","@#$") == True

def test_cycpattern_check_special_characters_false():
    assert cycpattern_check("!@#$%^","%^$#@") == False

def test_cycpattern_check_unicode_true():
    assert cycpattern_check("你好世界","世界") == True

def test_cycpattern_check_unicode_false():
    assert cycpattern_check("你好世界","世界啊") == False