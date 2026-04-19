
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def get_md5(text):
    """Helper to generate expected MD5 hashes for test verification."""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

@pytest.mark.parametrize("input_text, expected", [
    ('Hello world', '3e25960a79dbc69b674cd4ec67a72c62'),
    ('abc', '900150983cd24fb0d6963f7d28e17f72'),
    ('12345', '827ccb0eea8a706c4c34a16891f84e7b'),
    (' ', '77075b46318fa27ea430316bf69d6f5d'),
    ('Special characters !@#$%^&*()', get_md5('Special characters !@#$%^&*()')),
    ('Unicode test: 你好', get_md5('Unicode test: 你好')),
    ('Long string' * 100, get_md5('Long string' * 100)),
])
def test_string_to_md5_valid_inputs(input_text, expected):
    """Test that valid strings return the correct MD5 hash."""
    assert string_to_md5(input_text) == expected

def test_string_to_md5_empty_string():
    """Test that an empty string returns None as per requirements."""
    assert string_to_md5('') is None

def test_string_to_md5_case_sensitivity():
    """Test that MD5 hashes are case sensitive."""
    assert string_to_md5('Hello') != string_to_md5('hello')

def test_string_to_md5_type_error():
    """Test that the function raises an error when non-string input is provided."""
    with pytest.raises(AttributeError):
        string_to_md5(None)
    with pytest.raises(AttributeError):
        string_to_md5(123)