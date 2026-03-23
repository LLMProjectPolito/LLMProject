import hashlib
import pytest

def test_string_to_md5_valid_string():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

def test_string_to_md5_different_string():
    assert string_to_md5('This is a test') == 'e5e9fa1ba31ecd1ae84f75caaa474f3a6'

def test_string_to_md5_string_with_numbers():
    assert string_to_md5('12345') == '5994471abb01112afcc18159f6cc74b4'

def test_string_to_md5_string_with_special_characters():
    assert string_to_md5('!@#$%^') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_string_to_md5_long_string():
    long_string = 'This is a very long string to test the md5 hash function.'
    assert string_to_md5(long_string) == '9f86d081884c7d659a2feaa0c55ad015'

def test_string_to_md5_unicode_string():
    assert string_to_md5('你好世界') == 'b10a8db164e0754105b7a99be72e3fe5'