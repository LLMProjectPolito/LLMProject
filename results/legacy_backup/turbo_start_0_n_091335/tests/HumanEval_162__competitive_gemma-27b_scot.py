import hashlib
import pytest

def test_string_to_md5_valid_string():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

def test_string_to_md5_different_string():
    assert string_to_md5('test') == '098f6bcd4621d373cade4e832627b4f6'

def test_string_to_md5_with_numbers():
    assert string_to_md5('12345') == '5d41402abc4b2a76b9719d911017c592'

def test_string_to_md5_with_special_characters():
    assert string_to_md5('!@#$%^') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the md5 function."
    assert string_to_md5(long_string) == 'd9b1b7a8649999999999999999999999'

def test_string_to_md5_unicode_string():
    assert string_to_md5('你好世界') == '5994471abb01112afcc18159f6cc74b4'