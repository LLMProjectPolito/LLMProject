
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

# STEP 1: REASONING
# The function `string_to_md5` takes a string as input and returns its MD5 hash as a string.
# If the input string is empty, it returns None.
# We need to create a pytest suite to test the following:
# 1. Test with a valid string (e.g., "Hello world") and verify the returned MD5 hash.
# 2. Test with an empty string and verify the returned None.
# 3. Test with a string containing special characters (e.g., "!@#$%^&*()") and verify the returned MD5 hash.
# 4. Test with a very long string to check for potential performance issues (though MD5 is not designed for very long strings, it's good to have a basic check).

# STEP 2: PLAN
# test_string_to_md5_valid_string
# test_string_to_md5_empty_string
# test_string_to_md5_special_characters
# test_string_to_md5_long_string

# STEP 3: CODE
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
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5_hash

def test_string_to_md5_valid_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_to_md5_empty_string():
    assert string_to_md5("") is None

def test_string_to_md5_special_characters():
    assert string_to_md5("!@#$%^&*()") == "e5a9f934a4521423793584559874587"

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the function." * 100
    assert string_to_md5(long_string) == hashlib.md5(long_string.encode('utf-8')).hexdigest()