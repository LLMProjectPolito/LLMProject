
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

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5_hash

def test_string_to_md5_hello_world():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

def test_string_to_md5_single_character():
    assert string_to_md5('a') == '96a66dcd6a89b7a8667793799999999'

def test_string_to_md5_numbers():
    assert string_to_md5('12345') == '6b934d081d87a849999999999999999'

def test_string_to_md5_special_characters():
    assert string_to_md5('!@#$%^') == '8e999999999999999999999999999999'

def test_string_to_md5_mixed_characters():
    assert string_to_md5('Hello123!@#') == 'b94d27b9934d031642a378a8778a98a1'

def test_string_to_md5_unicode_characters():
    assert string_to_md5('你好世界') == 'b9a36699999999999999999999999999'

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the function with a large input."
    expected_md5 = 'a94a8fe5ccb19ba61c4c0873d391e987'
    assert string_to_md5(long_string) == expected_md5

def test_string_to_md5_whitespace():
    assert string_to_md5('   ') == '39a8a3d39311969a8999999999999999'

def test_string_to_md5_case_sensitive():
    assert string_to_md5('Hello') != 'hello'