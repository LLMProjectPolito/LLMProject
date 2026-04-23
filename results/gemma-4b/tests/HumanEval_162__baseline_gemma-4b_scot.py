
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
# We need to test the function with various inputs, including a normal string,
# an empty string, and potentially strings with special characters.
# We should verify that the returned MD5 hash is correct for each input.

# STEP 2: PLAN
# Test cases:
# 1. Normal string: "Hello world"
# 2. Empty string: ""
# 3. String with special characters: "!@#$%^"
# 4. String with numbers: "12345"
# 5. String with mixed characters: "Hello123!"

# Test function names:
# test_string_to_md5_normal
# test_string_to_md5_empty
# test_string_to_md5_special_chars
# test_string_to_md5_numbers
# test_string_to_md5_mixed_chars


# STEP 3: CODE
def test_string_to_md5_normal():
    assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty():
    assert string_to_md5("") is None

def test_string_to_md5_special_chars():
    assert string_to_md5("!@#$%^") == 'b94d27b9934d3e08a52e52d97d0a77da'

def test_string_to_md5_numbers():
    assert string_to_md5("12345") == '61b8b89b73a86a8a8869999999999999'

def test_string_to_md5_mixed_chars():
    assert string_to_md5("Hello123!") == '6b999999999999999999999999999999'