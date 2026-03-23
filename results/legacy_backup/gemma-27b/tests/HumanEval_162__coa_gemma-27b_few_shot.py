import pytest
import math


# Focus: Empty/Null Input
import hashlib

def test_string_to_md5_empty():
    assert string_to_md5('') is None

def test_string_to_md5_none_input():
    assert string_to_md5(None) is None

# Focus: Valid String Input
import hashlib

def test_md5_valid_string():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('test') == '098f6bcd4621d373cade4e832627b4f6'
    assert string_to_md5('a') == '0cc175b9c0f1b6a831c399e269772661'

# Focus: Error/Exception Handling (for potentially large strings or unsupported characters)
import hashlib

def test_string_to_md5_empty_string():
    assert string_to_md5("") is None

def test_string_to_md5_long_string():
    long_string = "a" * 1000
    expected_hash = hashlib.md5(long_string.encode('utf-8')).hexdigest()
    assert string_to_md5(long_string) == expected_hash

def test_string_to_md5_unsupported_characters():
    unsupported_string = "你好世界"  # Contains non-ASCII characters
    expected_hash = hashlib.md5(unsupported_string.encode('utf-8')).hexdigest()
    assert string_to_md5(unsupported_string) == expected_hash