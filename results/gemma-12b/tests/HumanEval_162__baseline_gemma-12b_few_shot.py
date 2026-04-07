
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
    md5_hash = hashlib.md5(text.encode('utf-8'))
    return md5_hash.hexdigest()

def test_string_to_md5_valid():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('abc') == 'ba7816bf8f01cfea414140de5dae2223'
    assert string_to_md5('12345') == '5d414c7b119794610da0d97679c441cd'

def test_string_to_md5_empty():
    assert string_to_md5('') is None

def test_string_to_md5_special_characters():
    assert string_to_md5('!@#$%^') == '9469c999999999999999999999999999'
    assert string_to_md5('你好世界') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_string_to_md5_unicode():
    assert string_to_md5('éàçüö') == '94a99999999999999999999999999999'

def test_string_to_md5_mixed_case():
    assert string_to_md5('HeLlO wOrLd') == '3e25960a79dbc69b674cd4ec67a72c62'