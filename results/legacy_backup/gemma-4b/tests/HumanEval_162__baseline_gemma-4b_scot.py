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
# We need to test the function with various inputs, including a normal string, an empty string, and potentially strings with special characters.
# We should also verify that the returned hash is the correct MD5 hash of the input string.

# STEP 2: PLAN
# Test cases:
# 1. Normal string: 'Hello world'
# 2. Empty string: ''
# 3. String with special characters: 'Hello, world!'
# 4. String with numbers: '12345'
# 5. String with unicode characters: '你好世界'

# Test function names:
# test_string_to_md5_normal
# test_string_to_md5_empty
# test_string_to_md5_special_chars
# test_string_to_md5_numbers
# test_string_to_md5_unicode

# STEP 3: CODE
def test_string_to_md5_normal():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty():
    assert string_to_md5('') is None

def test_string_to_md5_special_chars():
    assert string_to_md5('Hello, world!') == '6b17d1f2395736b88e39d884db764218'

def test_string_to_md5_numbers():
    assert string_to_md5('12345') == '6bca3a78999999999999999999999999'

def test_string_to_md5_unicode():
    assert string_to_md5('你好世界') == 'b9a896766d849b399696999999999999'