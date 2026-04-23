
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

@pytest.mark.parametrize("input_string, expected_md5", [
    ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
    ("This is a test", "b10a8db164e0754105b7a583e38d357b"),
    ("", None),
    ("12345", "e5a6e45361d47432e15841c11c1d915e"),
    ("The quick brown fox jumps over the lazy dog", "d41d8cd98f00b204e9800998ecf8427e"),
    ("A", "e53c8972f2046946a1764d5413798002"),
    ("123", "42a9b4f99c99f026e541f139015599a9"),
    ("你好世界", "5f954b02392c8a44372699787a737729"),  # Test with Chinese characters
    ("This string has special characters: !@#$%^&*()_+=-`~[]\{}|;':\",./<>?", "290907a694a254c9c35728c55d93b0c2"), #Test with special chars
    ("  ", "7803793456a149c6a0c3b8b6a096f9a4"), #Test with leading and trailing spaces
])
def test_string_to_md5(input_string, expected_md5):
    assert string_to_md5(input_string) == expected_md5

@pytest.mark.parametrize("input_string", [
    "",
    " ",
    "   ",
    "Hello world ",
    "Hello world ",
    "Hello world\n",
])
def test_empty_string_and_whitespace(input_string):
    assert string_to_md5(input_string) is None

@pytest.mark.parametrize("input_string", [
    "Hello world\n",
    "Hello world\t",
    "Hello world\r",
    "Hello world\r\n",
])
def test_newline_and_tab(input_string):
    assert string_to_md5(input_string) is not None

@pytest.mark.parametrize(
    "input_string, expected_md5",
    [
        ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
        ("This is a test", "f5a9c4e9d8d9d70e23188b7f29e23f2c"),
        ("", None),
        ("12345", "e5e9fa1ba31a9332e5f83291c8738233"),
        ("a", "b10a8db164e0754105b7a5838a5ff67d"),
        ("你好世界", "a1b82737441808f45b1b67b0552a0a9e"),
        ("Python", "4850928488b042c4a2f356d07726a5f5"),
        ("!@#$%^&*()", "9976801a592f451894a577ff5c8a0773"),
        (" ", "a34c2a083991548a6d2193564b96a078"),
        ("The quick brown fox jumps over the lazy dog", "d41d8cd98f00b204e9800998ecf8427e"),
    ],
)
def test_string_to_md5(input_string, expected_md5):
    assert string_to_md5(input_string) == expected_md5


@pytest.mark.parametrize(
    "input_string",
    [
        "Hello world",
        "",
        "12345",
        "a",
        "你好世界",
        "Python",
        "!@#$%^&*()",
        " ",
        "The quick brown fox jumps over the lazy dog",
    ],
)
def test_empty_string(input_string):
    assert string_to_md5(input_string) is None

@pytest.mark.parametrize(
    "input_string",
    [
        "Hello world",
        "",
        "12345",
        "a",
        "你好世界",
        "Python",
        "!@#$%^&*()",
        " ",
        "The quick brown fox jumps over the lazy dog",
    ],
)
def test_string_length(input_string):
    assert len(string_to_md5(input_string)) == 32