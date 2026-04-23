
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
        ("This is a test", "b10a8db164e070918392a31b0d670c8d"),
        ("", None),
        (" ", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"),
        ("a", "d41d8cd98f00b204e9800998ecf8427e"),
        ("12345", "489d3d255014a027700a39459a847a3c"),
        ("你好世界", "e59b329f59985a9d5a62a68c645b99e5"), #Unicode test
        ("This is a longer string to test the function's ability to handle longer inputs", "9060645791193a78574474577303552495674173832399418972891106263459"),
    ],
)
def test_string_to_md5(input_string, expected_md5):
    assert string_to_md5(input_string) == expected_md5

@pytest.mark.parametrize(
    "input_string, expected_none",
    [
        ("", True),
    ],
)
def test_empty_string(input_string, expected_none):
    assert string_to_md5(input_string) is expected_none

@pytest.mark.parametrize(
    "input_string, expected_error",
    [
        None,
    ],
)
def test_none_input(input_string, expected_error):
    with pytest.raises(TypeError):
        string_to_md5(input_string)