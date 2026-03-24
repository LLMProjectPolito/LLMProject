
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

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
    md5_hash = hashlib.md5(text.encode('utf-8'))
    return md5_hash.hexdigest()

# STEP 1: REASONING
# The function `string_to_md5` calculates the MD5 hash of a given string.
# It should return None if the input string is empty.
# The MD5 hash should be consistent for the same input string.
# We need to test the following scenarios:
# 1. Empty string input.
# 2. Non-empty string input.
# 3. String with special characters.
# 4. String with unicode characters.
# 5. Long string input.

# STEP 2: PLAN
# Test functions:
# - test_empty_string: Test with an empty string input.
# - test_non_empty_string: Test with a non-empty string input.
# - test_special_characters: Test with a string containing special characters.
# - test_unicode_characters: Test with a string containing unicode characters.
# - test_long_string: Test with a long string input.
# - test_known_string: Test with a known string and expected MD5 hash.

# STEP 3: CODE
class TestStringtoMD5:
    def test_empty_string(self):
        assert string_to_md5("") is None

    def test_non_empty_string(self):
        assert string_to_md5("test") == "098f6bcd4621d373cade4e832627b4f6"

    def test_special_characters(self):
        assert string_to_md5("!@#$%^&*()") == "99d8310496a399999999999999999999"

    def test_unicode_characters(self):
        assert string_to_md5("你好世界") == "a94a8fe5ccb19ba61c4c0873d391e987"

    def test_long_string(self):
        long_string = "This is a very long string to test the function with a large input."
        assert string_to_md5(long_string) == "91999699999999999999999999999999"

    def test_known_string(self):
        assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"