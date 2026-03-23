import hashlib
import pytest

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5_hash

def test_string_to_md5_valid_string():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

def test_string_to_md5_string_with_spaces():
    assert string_to_md5('   ') == 'd41d8cd98f00b204e9800998ecf8427e'

def test_string_to_md5_string_with_special_characters():
    assert string_to_md5('!@#$%^&*()') == '9f86d081884c7d659a2feaa0c55ad015'

def test_string_to_md5_string_with_numbers():
    assert string_to_md5('1234567890') == '5d41402abc4b2a76b9719d911017c592'

def test_string_to_md5_long_string():
    long_string = 'This is a very long string to test the md5 function.' * 10
    expected_md5 = 'f4999999999999999999999999999999'
    assert string_to_md5(long_string) == expected_md5

def test_string_to_md5_unicode_string():
    assert string_to_md5('你好世界') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_string_to_md5_mixed_string():
    assert string_to_md5('Hello world 123!@#') == 'a94a8fe5ccb19ba61c4c0873d391e987'

def test_string_to_md5_newline_string():
    assert string_to_md5('Hello\nWorld') == '6cd3556deb0da54bca060b4c39479839'

def test_string_to_md5_binary_string():
    assert string_to_md5('\x00\x01\x02') == '8e2e0944a99919999999999999999999'

def test_string_to_md5_different_case():
    assert string_to_md5('hello world') == string_to_md5('Hello world')

def test_string_to_md5_wide_binary_string():
    assert string_to_md5(b'\x00' * 256) == '9e914645999999999999999999999999'