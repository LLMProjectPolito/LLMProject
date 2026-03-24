
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

# Test functions:
# 1. test_empty_string
# 2. test_normal_string
# 3. test_special_characters
# 4. test_numbers
# 5. test_mixed_characters


# STEP 3: CODE
def test_empty_string():
    assert string_to_md5("") is None

def test_normal_string():
    assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

def test_special_characters():
    assert string_to_md5("!@#$%^") == 'b94d27b9934d3e08a52e52d97d0a763d'

def test_numbers():
    assert string_to_md5("12345") == '6ed35e09c8a999999999999999999999'

def test_mixed_characters():
    assert string_to_md5("Hello123!") == '6b889999999999999999999999999999'