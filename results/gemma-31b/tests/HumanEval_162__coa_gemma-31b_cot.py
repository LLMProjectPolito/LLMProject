
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import math


# Focus: Boundary Values
import hashlib

def test_string_to_md5_empty_string():
    assert string_to_md5("") is None

def test_string_to_md5_single_character():
    expected = hashlib.md5("a".encode()).hexdigest()
    assert string_to_md5("a") == expected

# Focus: Type Scenarios
import pytest

def test_string_to_md5_type_int():
    with pytest.raises(TypeError):
        string_to_md5(123)

def test_string_to_md5_type_none():
    with pytest.raises(TypeError):
        string_to_md5(None)

def test_string_to_md5_type_list():
    with pytest.raises(TypeError):
        string_to_md5(["hello"])

# Focus: Logic Branches
import pytest

def test_string_to_md5_empty_string():
    assert string_to_md5("") is None

def test_string_to_md5_non_empty_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"