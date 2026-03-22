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
# The tests should cover:
#   - A normal string input.
#   - An empty string input.
#   - A string with special characters.
#   - A string with unicode characters.

# STEP 2: PLAN
# Test cases:
#   - test_empty_string: Checks the empty string case.
#   - test_normal_string: Checks a normal string.
#   - test_special_characters: Checks a string with special characters.
#   - test_unicode_string: Checks a string with unicode characters.


# STEP 3: CODE
def test_empty_string():
    assert string_to_md5("") is None

def test_normal_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_special_characters():
    assert string_to_md5("!@#$%^&*()") == "6899999999999999999999999999999999999999"

def test_unicode_string():
    assert string_to_md5("你好世界") == "b94d27b9934d031642a378a8778a9879"

def test_mixed_string():
    assert string_to_md5("Hello world 123!") == "6966666666666666666666666666666666666666"

def test_long_string():
    long_string = "This is a very long string to test the function's performance and correctness."
    expected_md5 = "8966939999999999999999999999999999999999"
    assert string_to_md5(long_string) == expected_md5

def test_numeric_string():
    assert string_to_md5("12345") == "6b934236163a82699663d364939e36a9"

def test_whitespace_string():
    assert string_to_md5("   ") == "02a39b8b888e4667999999999999999999999999"