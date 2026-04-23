
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.
    The input string is encoded using UTF-8 before hashing.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8'))
    return md5_hash.hexdigest()

def test_empty_string():
    assert string_to_md5("") is None

def test_valid_string():
    text = "Hello world"
    expected_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected_hash

def test_string_with_leading_trailing_whitespace():
    text = "  test  "
    expected_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected_hash

def test_string_with_control_characters():
    text = "test\t\n\r"
    expected_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected_hash

def test_case_sensitivity():
    text1 = "Hello"
    text2 = "hello"
    assert string_to_md5(text1) != string_to_md5(text2)

def test_string_with_unicode_characters():
    text = "你好世界"
    expected_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected_hash

def test_string_with_numbers():
    text = "1234567890"
    expected_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected_hash

def test_string_with_alphanumeric_and_special_characters():
    text = "Hello123!@#"
    expected_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected_hash

def test_long_string():
    long_string = "This is a very long string to test the md5 hash function."
    expected_hash = hashlib.md5(long_string.encode('utf-8')).hexdigest()
    assert string_to_md5(long_string) == expected_hash

def test_string_with_newline():
    text = "Hello\nworld"
    expected_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected_hash

def test_invalid_input_type():
    with pytest.raises(TypeError):
        string_to_md5(123)
    with pytest.raises(TypeError):
        string_to_md5([1, 2, 3])