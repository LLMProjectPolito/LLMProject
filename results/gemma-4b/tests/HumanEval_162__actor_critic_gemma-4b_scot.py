
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

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `string_to_md5` calculates the MD5 hash of a given string.
# It handles the edge case where the input string is empty, returning None in that scenario.
# The function expects a string as input and returns a string representing the MD5 hash.
# We need to test various inputs, including empty strings, normal strings, and strings with special characters.
# We also need to verify that the returned hash is correct.

# STEP 2: PLAN - List test functions names and scenarios.
# test_empty_string: Test with an empty string.
# test_normal_string: Test with a normal string.
# test_special_characters: Test with a string containing special characters.
# test_unicode_string: Test with a Unicode string.
# test_long_string: Test with a long string.
# test_numeric_string: Test with a string containing only numbers.


# STEP 3: CODE - Write the high-quality pytest suite.
def test_empty_string():
    assert string_to_md5("") is None

def test_normal_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_special_characters():
    assert string_to_md5("This is a test!@#$%^&*()") == "6749999999999999999999999999999999999999999999999999999999999999"

def test_unicode_string():
    assert string_to_md5("你好世界") == "b9a8f99969999999999999999999999999999999999999999999999999999999"

def test_long_string():
    long_string = "a" * 1000
    assert string_to_md5(long_string) == "b9a8f99969999999999999999999999999999999999999999999999999999999"

def test_numeric_string():
    assert string_to_md5("1234567890") == "6b934d987b36d4c89d3692693b8999999999999999999999999999999999999"