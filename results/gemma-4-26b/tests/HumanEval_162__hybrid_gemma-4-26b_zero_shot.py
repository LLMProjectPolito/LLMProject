
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
    """
    if not text:
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def test_string_to_md5_empty_and_falsy():
    """Tests that empty strings and other falsy values return None as per requirements."""
    assert string_to_md5("") is None
    assert string_to_md5(None) is None
    assert string_to_md5([]) is None

@pytest.mark.parametrize("input_text, expected_hash", [
    ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
    ("a", "0cc175b9c0f1b6a831c399e269772661"),
    ("12345", "827ccb0eea8a706c4c34a16891f84e7b"),
    (" ", "315f5bdb76d078c43b8ac00c33e48e2a"),
    ("!@#$%^&*()", "69997f82696f3e80184674317096f31c"),
    ("Python", "1102e150963f5359e08442205c41855e"),
    ("Special characters: \n\t\r", "80216779895340579258105574384899"),
])
def test_string_to_md5_standard_cases(input_text, expected_hash):
    """Tests various standard ASCII and control character strings against known MD5 hashes."""
    assert string_to_md5(input_text) == expected_hash

@pytest.mark.parametrize("unicode_text, expected_hash", [
    ("こんにちは", "96e086d464e393e760840082f668322e"),  # Japanese
    ("你好", "e309f510037486526476986f6e826890"),      # Chinese
    ("🐍", "77057687393a990829277f1037966041"),        # Emoji
    ("Café", "72f9439030e65876036695486527028e"),      # Accented
])
def test_string_to_md5_unicode_inputs(unicode_text, expected_hash):
    """Ensures the function handles UTF-8 encoded multi-byte characters correctly."""
    assert string_to_md5(unicode_text) == expected_hash

def test_string_to_md5_case_sensitivity():
    """Tests that the MD5 hash is case-sensitive."""
    lower = string_to_md5("hello")
    upper = string_to_md5("HELLO")
    assert lower != upper
    assert lower == "5d41402abc4b2a76b9719d911017c592"
    assert upper == "8b1a5ee462e65b04e934285544c6455a"

def test_string_to_md5_large_input():
    """Tests with a large payload using dynamic verification to ensure stability."""
    large_text = "abc" * 10000
    expected_hash = hashlib.md5(large_text.encode('utf-8')).hexdigest()
    assert string_to_md5(large_text) == expected_hash

@pytest.mark.parametrize("invalid_input", [12345, 1.1, {"key": "val"}, [1, 2]])
def test_string_to_md5_invalid_types(invalid_input):
    """
    Checks behavior when a truthy non-string type is provided.
    Falsy types (None, empty list) are handled by the 'if not text' check.
    Truthy non-strings should raise AttributeError when .encode() is called.
    """
    with pytest.raises(AttributeError):
        string_to_md5(invalid_input)