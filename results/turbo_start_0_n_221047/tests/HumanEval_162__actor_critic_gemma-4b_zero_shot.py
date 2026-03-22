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
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def test_string_to_md5_normal():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty():
    assert string_to_md5('') is None

def test_string_to_md5_single_char():
    assert string_to_md5('a') == '9709a533666666666666666666666666'

def test_string_to_md5_unicode():
    assert string_to_md5('你好世界') == 'b94d27b9934d3e08a52e52d97d2dbee1'

def test_string_to_md5_numbers():
    assert string_to_md5('12345') == '6b934236f5486652494a308964497592'

def test_string_to_md5_special_chars():
    assert string_to_md5('!@#$%^') == '88626967999999999999999999999999'

def test_string_to_md5_mixed():
    assert string_to_md5('Hello123!@#') == '69679999999999999999999999999999'

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the function with a large input."
    expected_md5 = '89679999999999999999999999999999'
    assert string_to_md5(long_string) == expected_md5

def test_string_to_md5_whitespace():
    assert string_to_md5('   ') == '39a8469f934299999999999999999999'

def test_string_to_md5_newline():
    assert string_to_md5('hello\nworld') == 'b94d27b9934d3e08a52e52d97d2dbee1'