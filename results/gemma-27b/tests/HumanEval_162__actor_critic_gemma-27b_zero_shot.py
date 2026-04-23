
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

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
    assert string_to_md5('Hello world') == hashlib.md5('Hello world'.encode('utf-8')).hexdigest()

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

def test_string_to_md5_string_with_spaces():
    assert string_to_md5('   ') == hashlib.md5('   '.encode('utf-8')).hexdigest()

def test_string_to_md5_string_with_special_characters():
    assert string_to_md5('!@#$%^&*()') == hashlib.md5('!@#$%^&*()'.encode('utf-8')).hexdigest()

def test_string_to_md5_string_with_numbers():
    assert string_to_md5('1234567890') == hashlib.md5('1234567890'.encode('utf-8')).hexdigest()

def test_string_to_md5_long_string():
    long_string = 'This is a very long string to test the md5 function.' * 10
    assert string_to_md5(long_string) == hashlib.md5(long_string.encode('utf-8')).hexdigest()

def test_string_to_md5_unicode_string():
    assert string_to_md5('你好世界') == hashlib.md5('你好世界'.encode('utf-8')).hexdigest()

def test_string_to_md5_mixed_string():
    assert string_to_md5('Hello world 123!@#') == hashlib.md5('Hello world 123!@#'.encode('utf-8')).hexdigest()

def test_string_to_md5_newline_string():
    assert string_to_md5('Hello\nWorld') == hashlib.md5('Hello\nWorld'.encode('utf-8')).hexdigest()

def test_string_to_md5_case_sensitive():
    assert string_to_md5('hello world') != string_to_md5('Hello world')

def test_string_to_md5_single_character():
    assert string_to_md5('a') == hashlib.md5('a'.encode('utf-8')).hexdigest()

def test_string_to_md5_non_utf8():
    try:
        string_to_md5('\ud800')  # Invalid UTF-8 character
    except UnicodeEncodeError:
        pass  # Expected exception
    else:
        pytest.fail("UnicodeEncodeError not raised for invalid UTF-8 character")

# Removed test_string_to_md5_max_length_string as it only checked length

# Moved docstring test to a dedicated test function
def test_string_to_md5_docstring_example():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'