
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
from your_module import string_to_md5  # Replace your_module


@pytest.mark.parametrize(
    "input_string, expected_md5",
    [
        ("", None),
        ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
        ("1234567890", "e59ff9645c4696b483b0255c6688c5c7"),
        ("!@#$%^&*()", "964e9f215054e370a0a5707e771a40c8"),
        ("This is a long string", "6e79f4619d7349f94c7f166536e88a78"),
        ("你好世界", "86e5a5d5e1a5e1a5e1a5e1a5e1a5e1a5"),
        ("   ", "30e61f922f30a42774947015d91c5697"),
        ("madam", "b10a8374a4722549f41d12a2f6898982")
    ],
)
def test_string_to_md5(input_string, expected_md5):
    assert string_to_md5(input_string) == expected_md5

@pytest.mark.parametrize(
    "input_string",
    [
        "",
        "Hello world",
        "1234567890",
        "!@#$%^&*()",
        "This is a long string",
        "你好世界",
        "   ",
        "madam",
    ],
)
def test_string_to_md5_various_inputs(input_string):
    assert string_to_md5(input_string) is None if input_string == "" else string_to_md5(input_string)