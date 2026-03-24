
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
from your_module import string_to_md5  # Replace your_module

def test_empty_string_boundary():
    assert string_to_md5("") is None

def test_single_character_boundary():
    assert string_to_md5("a") == "0cc175b9c0f1b6a831c399e269772661"

def test_short_string_boundary():
    assert string_to_md5("ab") == "2baa7b9332e6bb5f727d689896bca5e4"

# Focus: Error Handling
def test_string_to_md5_empty_string():
    assert string_to_md5("") is None

def test_string_to_md5_invalid_input_type():
    try:
        string_to_md5(123)
        assert False, "Should have raised a TypeError"
    except TypeError:
        assert True

def test_string_to_md5_none_input():
    try:
        string_to_md5(None)
        assert False, "Should have raised a TypeError"
    except TypeError:
        assert True

# Focus: Logic Branches
def test_empty_string():
    assert string_to_md5("") is None

def test_non_empty_string():
    assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

def test_different_string():
    assert string_to_md5("This is a test") == '9f86d081884c7d659a2feaa0c55ad015'