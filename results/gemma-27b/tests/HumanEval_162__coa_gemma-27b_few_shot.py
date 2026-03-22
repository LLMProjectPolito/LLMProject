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

# Focus: Error Handling/Invalid Input Types
import pytest
import hashlib

def test_string_to_md5_invalid_input():
    with pytest.raises(TypeError):
        string_to_md5(123)
    with pytest.raises(TypeError):
        string_to_md5([1, 2, 3])
    with pytest.raises(TypeError):
        string_to_md5(None)

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None