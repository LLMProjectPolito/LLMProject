
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib
from your_module import string_to_md5  # Replace your_module

def test_empty_string():
    assert string_to_md5("") is None

def test_simple_string():
    assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_with_spaces():
    assert string_to_md5("This is a test") == 'b10a8db164e0755b79f872d4333355c3'

def test_string_with_special_characters():
    assert string_to_md5("!@#$%^&*()") == 'e233b8681994a816b1b38a800759384f'

def test_string_with_numbers():
    assert string_to_md5("1234567890") == '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'

def test_long_string():
    long_string = "This is a very long string to test the function's performance." * 10
    md5_hash = hashlib.md5(long_string.encode()).hexdigest()
    assert string_to_md5(long_string) == md5_hash

def test_string_with_unicode_characters():
    assert string_to_md5("你好世界") == '5a839775b96993858d30492b98b44549'

def test_string_with_mixed_characters():
    assert string_to_md5("Hello你好世界123") == '6803a85475e2706950b9d538c1d6526c'