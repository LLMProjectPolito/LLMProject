
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

def test_valid_string_input_normal_case():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_valid_string_input_with_numbers():
    assert string_to_md5("Test1234") == "a94a8fe5ccb19ba61c4c0873d391e987"

def test_valid_string_input_with_special_characters():
    assert string_to_md5("!@#$%^") == "96f96999999999999999999999999999"

# Focus: Error/Exception Handling (for potentially large strings or unsupported characters)
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

def test_string_to_md5_large_string():
    large_string = "a" * 100000
    result = string_to_md5(large_string)
    assert isinstance(result, str)
    assert len(result) == 32

def test_string_to_md5_unsupported_characters():
    unsupported_string = "Hello\ud800world"  # Contains a surrogate code point
    try:
        string_to_md5(unsupported_string)
    except UnicodeEncodeError:
        pass
    else:
        pytest.fail("UnicodeEncodeError not raised for unsupported characters")

def test_string_to_md5_empty_string():
    assert string_to_md5("") is None