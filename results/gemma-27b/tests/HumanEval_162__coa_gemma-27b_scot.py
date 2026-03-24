
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import math


# Focus: Empty/Null Input
import pytest
from your_module import string_to_md5  # Replace your_module

def test_string_to_md5_empty_string():
    assert string_to_md5("") is None

def test_string_to_md5_none_input():
    with pytest.raises(TypeError):
        string_to_md5(None)

# Focus: Valid String Input
import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()

def test_valid_string_input_basic():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_valid_string_input_different_string():
    assert string_to_md5("This is a test") == "5994471abb01112afcc18159f6cc74b4"

def test_valid_string_input_with_numbers():
    assert string_to_md5("string123") == "967a9a8f999999999999999999999999"

# Focus: Error Handling/Invalid Input Types
import pytest
from hashlib import md5

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    return md5(text.encode()).hexdigest()

def test_string_to_md5_invalid_input_type_int():
    with pytest.raises(TypeError):
        string_to_md5(123)

def test_string_to_md5_invalid_input_type_list():
    with pytest.raises(TypeError):
        string_to_md5([1, 2, 3])