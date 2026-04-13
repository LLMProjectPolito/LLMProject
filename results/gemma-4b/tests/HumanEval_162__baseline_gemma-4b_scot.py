
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
    return hashlib.md5(text.encode('utf-8')).hexdigest()


### SCoT Steps:

# STEP 1: REASONING
# The function `string_to_md5` calculates the MD5 hash of a given string.
# It handles the edge case of an empty input string by returning None.
# We need to test the function with various inputs, including an empty string,
# a simple string, and potentially longer strings to ensure the hash is calculated correctly.
# We should also consider testing the return type (string) and the behavior when the input is None.

# STEP 2: PLAN
# Test cases:
# 1. Empty string: Should return None.
# 2. Simple string: "Hello world" - Should return the expected MD5 hash.
# 3. Another simple string: "Test string" - Should return the expected MD5 hash.
# 4. Longer string: "This is a longer string to test the function." - Should return the expected MD5 hash.
# 5. String with special characters: "String with !@#$%^&*()" - Should return the expected MD5 hash.

# Test function names:
# test_empty_string
# test_simple_string
# test_longer_string
# test_special_characters
# test_none_input

# STEP 3: CODE
def test_empty_string():
    assert string_to_md5("") is None

def test_simple_string():
    assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

def test_longer_string():
    assert string_to_md5("This is a longer string to test the function.") == 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'

def test_special_characters():
    assert string_to_md5("String with !@#$%^&*()") == '8999999999999999999999999999999999999999999999999999999999999999'

def test_none_input():
    assert string_to_md5(None) is None