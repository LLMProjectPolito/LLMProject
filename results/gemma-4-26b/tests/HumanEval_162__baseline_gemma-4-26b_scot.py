
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest

# Note: string_to_md5 is assumed to be defined in the environment as per instructions.

@pytest.mark.parametrize("input_text, expected_md5", [
    ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
    ("123", "202cb962ac59075b964b07152d234b70"),
    ("!@#", "6ec80063060307907695099953f0293e"),
    (" ", "356a192b7913b04c54574d18c28d46e6"),
    ("python", "1f3870be274f6c49b3e31a0c6728957f"),
])
def test_string_to_md5_parameterized(input_text, expected_md5):
    """Test multiple standard string inputs against known MD5 hashes."""
    assert string_to_md5(input_text) == expected_md5

def test_string_to_md5_empty_string():
    """Verify that an empty string returns None."""
    assert string_to_md5("") is None

def test_string_to_md5_unicode():
    """Verify that Unicode characters (e.g., emojis) are handled correctly."""
    # MD5 of '🐍' (UTF-8: f0 9f 90 8d)
    expected = "67707763759909946693209818369660"
    assert string_to_md5("🐍") == expected

def test_string_to_md5_long_string():
    """Verify the function handles longer strings correctly."""
    long_str = "a" * 1000
    # MD5 of 1000 'a's
    expected = "70066660638164357095747698745692"
    assert string_to_md5(long_str) == expected

def test_string_to_md5_whitespace_variations():
    """Verify that different whitespace configurations are not treated as empty."""
    # A single space is not an empty string
    assert string_to_md5(" ") is not None
    # A tab is not an empty string
    assert string_to_md5("\t") is not None
    # Newline is not an empty string
    assert string_to_md5("\n") is not None

def test_string_to_md5_case_sensitivity():
    """Verify that MD5 is case sensitive (standard behavior)."""
    lower = string_to_md5("hello")
    upper = string_to_md5("HELLO")
    assert lower != upper