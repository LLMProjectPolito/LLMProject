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

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `string_to_md5` calculates the MD5 hash of a given string.
# It handles the edge case where the input string is empty, returning None in that scenario.
# The function expects a string as input and returns a string representing the MD5 hash.
# We need to test various inputs, including empty strings, normal strings, and strings with special characters.

# STEP 2: PLAN - List test functions names and scenarios.
# test_empty_string: Test with an empty string.
# test_normal_string: Test with a normal string.
# test_special_characters: Test with a string containing special characters.
# test_unicode_string: Test with a Unicode string.
# test_long_string: Test with a long string.
# test_numeric_string: Test with a string containing only numbers.
# test_none_input: Test with None input

# STEP 3: CODE - Write the high-quality pytest suite.
def test_empty_string():
    assert string_to_md5("") is None
    assert string_to_md5("") == None

def test_normal_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_special_characters():
    assert string_to_md5("This is a test!@#$%^&*()") == "b94d27b9934d3e08a52e52d46d1ff81a"

def test_unicode_string():
    assert string_to_md5("你好世界") == "b94d27b9934d3e08a52e52d46d1ff81a"

def test_long_string():
    long_string = "This is a very long string to test the function's performance and correctness."
    assert string_to_md5(long_string) == "8f99999999999999999999999999999999999999"

def test_numeric_string():
    assert string_to_md5("1234567890") == "6b934bca6e6779a7696a98684699699d"

def test_mixed_string():
    assert string_to_md5("Hello123World!") == "6e97839999999999999999999999999999999999"

def test_none_input():
    assert string_to_md5(None) is None