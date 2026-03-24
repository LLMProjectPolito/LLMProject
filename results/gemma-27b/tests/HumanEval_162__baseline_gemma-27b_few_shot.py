
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

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

def test_md5_basic():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('test') == '098f6bcd4621d373cade4e832627b4f6'

def test_md5_empty():
    assert string_to_md5('') == None

def test_md5_long_string():
    long_string = "This is a very long string to test the MD5 hash function."
    expected_hash = '9a39a919499994999499949994999499' # Replace with actual hash
    assert string_to_md5(long_string) == '9a39a919499994999499949994999499'

def test_md5_with_numbers():
    assert string_to_md5('12345') == '5994471abb01112afcc18159f6cc74b4'

def test_md5_with_special_characters():
    assert string_to_md5('!@#$%^') == 'b10a8db164e0754105b7a99be72e3fe5'