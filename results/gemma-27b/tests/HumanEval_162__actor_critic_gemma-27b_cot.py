
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import hashlib
import pytest

def calculate_md5(text):
    """Helper function to calculate the MD5 hash of a string."""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def test_string_to_md5_valid_string():
    text = 'Hello world'
    expected_hash = calculate_md5(text)
    assert string_to_md5(text) == expected_hash

def test_string_to_md5_empty_string():
    text = ''
    assert string_to_md5(text) is None

def test_string_to_md5_complex_string():
    text = 'Hello world 123!@#你好世界'
    expected_hash = calculate_md5(text)
    assert string_to_md5(text) == expected_hash

def test_string_to_md5_long_string():
    text = 'This is a very long string to test the md5 function.' * 100
    expected_hash = calculate_md5(text)
    assert string_to_md5(text) == expected_hash

def test_string_to_md5_string_with_spaces():
    text = '  test  '
    expected_hash = calculate_md5(text)
    assert string_to_md5(text) == expected_hash

def test_string_to_md5_unicode_string():
    text = '你好世界🌍'  # Includes characters outside BMP
    expected_hash = calculate_md5(text)
    assert string_to_md5(text) == expected_hash

def test_string_to_md5_case_sensitivity():
    text1 = 'Hello'
    text2 = 'hello'
    assert string_to_md5(text1) != string_to_md5(text2)

def test_string_to_md5_non_string_input():
    with pytest.raises(TypeError):
        string_to_md5(123)
    with pytest.raises(TypeError):
        string_to_md5([1, 2, 3])
    with pytest.raises(TypeError):
        string_to_md5(None)