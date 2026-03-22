import pytest
import hashlib

def test_string_to_md5_basic(string_to_md5):
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty(string_to_md5):
    assert string_to_md5('') is None

def test_string_to_md5_whitespace(string_to_md5):
    assert string_to_md5('   ') == 'd41d8cd98f00b204e9800998ecf8427e'

def test_string_to_md5_long_string(string_to_md5):
    long_string = 'a' * 1000
    assert string_to_md5(long_string) == 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'

def test_string_to_md5_unicode(string_to_md5):
    assert string_to_md5('你好世界') == '5994471abb01112afcc18159f6cc74b4'

def test_string_to_md5_special_characters(string_to_md5):
    assert string_to_md5('!@#$%^&*()_+=-') == '94999999999999999999999999999999'

def test_string_to_md5_numbers(string_to_md5):
    assert string_to_md5('1234567890') == '5d41402abc4b2a76b9719d911017c592'

def test_string_to_md5_mixed_case(string_to_md5):
    assert string_to_md5('Hello World') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_string_to_md5_binary_data(string_to_md5):
    assert string_to_md5('0101010101010101') == '9a8a9999999999999999999999999999'

def test_string_to_md5_return_type(string_to_md5):
    assert isinstance(string_to_md5("test"), str)
    assert string_to_md5("") is None

def test_string_to_md5_case_sensitivity(string_to_md5):
    assert string_to_md5("Hello world") != string_to_md5("hello world")

def test_string_to_md5_hexadecimal_output(string_to_md5):
    result = string_to_md5("test")
    assert isinstance(result, str)
    assert all(c in "0123456789abcdef" for c in result)

def test_string_to_md5_with_newlines_and_tabs(string_to_md5):
    assert string_to_md5("Hello\nWorld\t!") == "b10a8db164e0754105b7a99be72e3fe5"

def test_string_to_md5_symbols(string_to_md5):
    assert string_to_md5("!@#$%^") == "9249f564996996964996969649969696"