import pytest

def test_cycpattern_check_rotation_found():
    assert cycpattern_check("hello","ell") == True

def test_cycpattern_check_rotation_not_found():
    assert cycpattern_check("abcd","abd") == False

def test_cycpattern_check_rotation_found_at_end():
    assert cycpattern_check("whassup","sup") == True

def test_cycpattern_check_rotation_not_found_at_end():
    assert cycpattern_check("whassup","psus") == False

def test_cycpattern_check_rotation_found_in_middle():
    assert cycpattern_check("abab","baa") == True

def test_cycpattern_check_rotation_not_found_in_middle():
    assert cycpattern_check("efef","eeff") == False

def test_cycpattern_check_rotation_found_with_repeated_chars():
    assert cycpattern_check("himenss","simen") == True

def test_cycpattern_check_empty_string():
    assert cycpattern_check("hello","") == True

def test_cycpattern_check_empty_string_in_first_word():
    assert cycpattern_check("","hello") == False

def test_cycpattern_check_same_string():
    assert cycpattern_check("hello","hello") == True

def test_cycpattern_check_long_string():
    long_string = "a" * 1000
    assert cycpattern_check(long_string, "a") == True