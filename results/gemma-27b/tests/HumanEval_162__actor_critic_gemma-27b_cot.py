
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import hashlib
import pytest
import unicodedata

def test_string_to_md5_valid_string():
    text = 'Hello world'
    assert string_to_md5(text) == hashlib.md5(text.encode('utf-8')).hexdigest()

def test_string_to_md5_empty_string():
    # Expect None for an empty string input.
    assert string_to_md5('') is None

def test_string_to_md5_string_with_spaces():
    text = '  test  '
    assert string_to_md5(text) == hashlib.md5(text.encode('utf-8')).hexdigest()

def test_string_to_md5_string_with_special_characters():
    text = '!@#$%^&*()'
    assert string_to_md5(text) == hashlib.md5(text.encode('utf-8')).hexdigest()

def test_string_to_md5_long_string():
    long_string = 'This is a very long string to test the md5 hash function.' * 10
    assert string_to_md5(long_string) == hashlib.md5(long_string.encode('utf-8')).hexdigest()

def test_string_to_md5_unicode_string():
    text = '你好世界'
    assert string_to_md5(text) == hashlib.md5(text.encode('utf-8')).hexdigest()

def test_string_to_md5_numeric_string():
    text = '1234567890'
    assert string_to_md5(text) == hashlib.md5(text.encode('utf-8')).hexdigest()

def test_string_to_md5_mixed_string():
    text = 'Hello123World!'
    assert string_to_md5(text) == hashlib.md5(text.encode('utf-8')).hexdigest()

def test_string_to_md5_case_sensitivity():
    assert string_to_md5('Hello') != string_to_md5('hello')

def test_string_to_md5_non_string_input():
    with pytest.raises(TypeError):
        string_to_md5(123)

def test_string_to_md5_unicode_normalization():
    text = 'café'
    assert string_to_md5(text) == hashlib.md5(text.encode('utf-8')).hexdigest()

def test_string_to_md5_very_long_string():
    very_long_string = 'a' * 100000
    assert string_to_md5(very_long_string) == hashlib.md5(very_long_string.encode('utf-8')).hexdigest()