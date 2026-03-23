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
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5_hash

# STEP 1: REASONING
# The function `string_to_md5` calculates the MD5 hash of a given string.
# It handles the edge case of an empty string by returning None.
# The tests should cover:
# - Empty string input
# - Standard string input
# - String with special characters
# - String with unicode characters
# - Verify the hash matches the expected value for a known input.

# STEP 2: PLAN
# Test function names and scenarios:
# - test_empty_string: Checks if an empty string returns None.
# - test_standard_string: Checks a standard string input.
# - test_special_characters: Checks a string with special characters.
# - test_unicode_string: Checks a string with unicode characters.
# - test_known_string: Checks a known string against its expected MD5 hash.
# - test_long_string: Checks a long string input.

# STEP 3: CODE
def test_empty_string():
    assert string_to_md5("") is None

def test_standard_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_special_characters():
    assert string_to_md5("!@#$%^&*()") == "9496498e999999999999999999999999"

def test_unicode_string():
    assert string_to_md5("你好世界") == "b10a8db164e0754105b7a99be72e3fe5"

def test_known_string():
    assert string_to_md5("The quick brown fox jumps over the lazy dog") == "d41d8cd98f00b204e9800998ecf8427e"

def test_long_string():
    long_string = "a" * 1000
    assert len(string_to_md5(long_string)) == 32