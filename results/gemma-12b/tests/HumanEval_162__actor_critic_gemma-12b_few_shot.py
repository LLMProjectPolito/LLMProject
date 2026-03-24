
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

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8'))
    return md5_hash.hexdigest()

def test_string_to_md5_basic():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty():
    assert string_to_md5('') is None

def test_string_to_md5_single_char():
    assert string_to_md5('a') == '0cc175b9c0f1b6a831c399e269772661'

def test_string_to_md5_with_spaces():
    assert string_to_md5('  ') == 'd14a028c2a3a2bc9476102bb288234c4'

def test_string_to_md5_numbers():
    assert string_to_md5('12345') == '5d414c7b5fdc8661509d3fbe5a386a83'

def test_string_to_md5_special_characters():
    assert string_to_md5('!@#$%^&*()_+=-`~[]\{}|;\':",./<>?') == '99d8310496a939999999999999999999' # Combined special chars

def test_string_to_md5_mixed_case():
    assert string_to_md5('HeLlO') == '15339413a99019999999999999999999'

def test_string_to_md5_unicode():
    assert string_to_md5('你好世界') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_string_to_md5_non_ascii():
    assert string_to_md5('éàçüö') == '99999999999999999999999999999999' # Example non-ASCII characters

def test_string_to_md5_long_string():
    long_string = "a" * 1000  # Create a long string
    assert len(string_to_md5(long_string)) == 32 # Check the length of the hash

def test_string_to_md5_non_string_input():
    with pytest.raises(TypeError):
        string_to_md5(123)  # Pass an integer
    with pytest.raises(TypeError):
        string_to_md5([1, 2, 3]) # Pass a list