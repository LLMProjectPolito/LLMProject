
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import math


# Focus: Boundary Values
import pytest

def test_string_to_md5_empty_string():
    assert string_to_md5("") is None

def test_string_to_md5_single_character():
    # MD5 hash of 'a' is '0cc175b9c0f1b6a831c399e269772661'
    assert string_to_md5("a") == "0cc175b9c0f1b6a831c399e269772661"

def test_string_to_md5_very_long_string():
    long_text = "a" * 10**6
    result = string_to_md5(long_text)
    assert isinstance(result, str)
    assert len(result) == 32

# Focus: Type Scenarios
import pytest

def test_string_to_md5_none_type():
    with pytest.raises(TypeError):
        string_to_md5(None)

def test_string_to_md5_int_type():
    with pytest.raises(TypeError):
        string_to_md5(123)

def test_string_to_md5_list_type():
    with pytest.raises(TypeError):
        string_to_md5(["hello"])

# Focus: Logic Branches
import hashlib

def test_string_to_md5_empty():
    assert string_to_md5("") is None

def test_string_to_md5_non_empty():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"