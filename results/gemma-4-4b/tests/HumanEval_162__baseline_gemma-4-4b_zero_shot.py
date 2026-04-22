
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
    return hashlib.md5(text.encode('utf-8')).hexdigest()


@pytest.mark.parametrize(
    "input_string, expected_md5",
    [
        ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
        ("Python", "6f7d7a9822d9d4d9854498e6a6b03a53"),
        ("", None),
        ("a", "ba7816bf8f01410e1849803f323c2b53"),
        ("This is a test", "699942e3f39950224867915148496a5a"),
        ("12345", "489d3d9d2b3dd3157894279095a7c30a"),
        ("你好世界", "e59b9e87520b51be2d83a3a93b29679b"),
    ],
)
def test_string_to_md5(input_string, expected_md5):
    assert string_to_md5(input_string) == expected_md5

def test_empty_string():
    assert string_to_md5("") is None

def test_md5_hash_length():
    assert len(string_to_md5("test")) == 32

def test_unicode_string():
    assert string_to_md5("你好") is not None