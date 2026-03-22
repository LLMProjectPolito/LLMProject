import hashlib
import pytest

def test_string_to_md5_valid_string():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('This is a test.') == '5994471abb01112afcc18159f6cc74b4'
    assert string_to_md5('MD5 hash test') == '486ea46224d1bb4fb680f34f7c933f39'

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

def test_string_to_md5_string_with_spaces():
    assert string_to_md5('  test  ') == 'a185d599f19f69496999999999999999'
    assert string_to_md5('   ') == 'd41d8cd98f00b204e9800998ecf8427e'

def test_string_to_md5_string_with_numbers():
    assert string_to_md5('12345') == '827ccb0eea8a706c4c34a16891f84e7b'
    assert string_to_md5('1234567890') == '5d41402abc4b2a76b9719d911017c592'

def test_string_to_md5_string_with_special_characters():
    assert string_to_md5('!@#$%^') == 'b10a8db164e0754105b7a99be72e3fe5'
    assert string_to_md5('!@#$%^&*()') == '827ccb0eea8a706c4c34a16891f84e7b'

def test_string_to_md5_long_string():
    long_string = 'This is a very long string to test the md5 hash function.'
    assert string_to_md5(long_string) == '9f86d081884c7d659a2feaa0c55ad015'
    long_string = 'a' * 1000
    assert string_to_md5(long_string) == 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'

def test_string_to_md5_unicode_string():
    assert string_to_md5('你好世界') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_string_to_md5_mixed_string():
    assert string_to_md5('Hello123!@#') == '5994471abb01112afcc18159f6cc74b4'
    assert string_to_md5('Hello world 123!@#') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_string_to_md5_different_case():
    assert string_to_md5('hello world') == 'b10a8db164e0754105b7a99be72e3fe5'
    assert string_to_md5('HELLO WORLD') == '6cd3556deb0da54bca060b4c39479839'

def test_string_to_md5_string_with_newline():
    assert string_to_md5('Hello\nworld') == '6cd3556deb0da54bca060b4c39479839'
    assert string_to_md5('Hello\nWorld') == '6cd3556deb0da54bca060b4c39479839'