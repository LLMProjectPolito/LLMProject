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

def test_string_to_md5_valid():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('abc') == 'ba7816bf8f01cfea414140de5dae2223'
    assert string_to_md5('12345') == '5d41402abc4b2a76b9719d911017c592'

def test_string_to_md5_empty():
    assert string_to_md5('') == None

def test_string_to_md5_special_chars():
    assert string_to_md5('!@#$%^') == '99d83136999999999999999999999999'

def test_string_to_md5_unicode():
    assert string_to_md5('你好世界') == 'a94a8fe5ccb19ba61c4c0873d391e987'

def test_string_to_md5_mixed_case():
    assert string_to_md5('HeLlO wOrLd') == '3e25960a79dbc69b674cd4ec67a72c62'