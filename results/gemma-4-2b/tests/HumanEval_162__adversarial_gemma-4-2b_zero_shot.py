
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


@pytest.mark.parametrize(
    "input_string, expected_md5",
    [
        ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
        ("This is a test", "a99f347a377e3e9b4d69039e285d99e2"),
        ("", None),
        ("12345", "a1b2c3d4e5f67890"),
        ("你好世界", "b10a8db164e07c89d433e982e31b8f94"),  # Unicode test
        ("a", "e59ff95633929b54588633662569099e"),
    ],
)
def test_string_to_md5(input_string, expected_md5):
    """
    Test cases for string_to_md5 function.
    """
    assert string_to_md5(input_string) == expected_md5

@pytest.mark.parametrize(
    "input_string",
    [
        "",
        " ",
        "a",
        "Hello",
        "World!"
    ],
)
def test_empty_string(input_string):
    """
    Test case for empty string input.
    """
    assert string_to_md5(input_string) is None

@pytest.mark.parametrize(
    "input_string",
    [
        "This is a very long string to test the function.",
        "Another long string for testing purposes."
    ],
)
def test_long_string(input_string):
    """
    Test case for long string input.
    """
    assert string_to_md5(input_string)  # Verify that it doesn't crash on long strings.  The hash should be generated.

@pytest.mark.parametrize(
    "input_string",
    [
        "This string contains special characters: !@#$%^&*()_+=-`~[]\{}|;':\",./<>?",
        "String with unicode characters: こんにちは世界"
    ],
)
def test_special_characters(input_string):
    """
    Test case for strings with special characters.
    """
    assert string_to_md5(input_string) # Verify that it doesn't crash on special characters. The hash should be generated.