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
    return hashlib.md5(text.encode('utf-8')).hexdigest()


### SCoT Steps:

# STEP 1: REASONING
# The function `string_to_md5` calculates the MD5 hash of a given string.
# It handles the edge case of an empty input string by returning None.
# We need to test the function with various inputs, including an empty string,
# a simple string, and potentially longer strings to ensure the hash is calculated correctly.
# We should also consider testing the return type to ensure it's a string.

# STEP 2: PLAN
# Test cases:
# 1. Empty string: Should return None.
# 2. Simple string: Should return the correct MD5 hash.
# 3. Longer string: Should return the correct MD5 hash.
# 4. String with special characters: Should return the correct MD5 hash.

# Test function names:
# test_empty_string
# test_simple_string
# test_long_string
# test_special_characters_string


# STEP 3: CODE
def test_empty_string():
    assert string_to_md5("") is None

def test_simple_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_long_string():
    long_string = "This is a very long string to test the MD5 hash function."
    assert string_to_md5(long_string) == "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"

def test_special_characters_string():
    special_string = "This string contains !@#$%^&*()_+=-`~[]\{}|;':\",./<>?"
    assert string_to_md5(special_string) == "8996999999999999999999999999999999999999999999999999999999999999"

def test_unicode_string():
    unicode_string = "你好世界"
    assert string_to_md5(unicode_string) == "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"

def test_string_with_spaces():
    assert string_to_md5("  leading and trailing spaces  ") == "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"