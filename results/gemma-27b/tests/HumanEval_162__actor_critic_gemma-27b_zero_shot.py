
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
    md5_hash = hashlib.md5('Hello world'.encode('utf-8')).hexdigest()
    assert string_to_md5('Hello world') == md5_hash

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

def test_string_to_md5_string_with_spaces():
    md5_hash = hashlib.md5('   '.encode('utf-8')).hexdigest()
    assert string_to_md5('   ') == md5_hash

def test_string_to_md5_string_with_special_characters():
    md5_hash = hashlib.md5('!@#$%^&*()'.encode('utf-8')).hexdigest()
    assert string_to_md5('!@#$%^&*()') == md5_hash

def test_string_to_md5_string_with_numbers():
    md5_hash = hashlib.md5('1234567890'.encode('utf-8')).hexdigest()
    assert string_to_md5('1234567890') == md5_hash

def test_string_to_md5_long_string():
    long_string = 'This is a very long string to test the md5 function.' * 10
    md5_hash = hashlib.md5(long_string.encode('utf-8')).hexdigest()
    assert string_to_md5(long_string) == md5_hash

def test_string_to_md5_unicode_string():
    md5_hash = hashlib.md5('你好世界'.encode('utf-8')).hexdigest()
    assert string_to_md5('你好世界') == md5_hash

def test_string_to_md5_mixed_string():
    md5_hash = hashlib.md5('Hello world 123!@#'.encode('utf-8')).hexdigest()
    assert string_to_md5('Hello world 123!@#') == md5_hash

def test_string_to_md5_newline_string():
    md5_hash = hashlib.md5('Hello\nWorld'.encode('utf-8')).hexdigest()
    assert string_to_md5('Hello\nWorld') == md5_hash

def test_string_to_md5_byte_string():
    assert string_to_md5('some bytes') == hashlib.md5('some bytes'.encode('utf-8')).hexdigest()

def test_string_to_md5_very_long_string():
    very_long_string = 'a' * 1000
    md5_hash = hashlib.md5(very_long_string.encode('utf-8')).hexdigest()
    assert string_to_md5(very_long_string) == md5_hash