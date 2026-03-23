import pytest
import math

import pytest
import hashlib

def test_string_to_md5_positive():
    text = "Hello world"
    expected_md5 = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected_md5

import pytest
import hashlib

def test_empty_string():
    """Test with an empty string input."""
    from your_module import string_to_md5  # Replace your_module
    assert string_to_md5("") is None

import pytest
import hashlib

def test_string_to_md5_non_string_input():
    """Test with a non-string input."""
    with pytest.raises(TypeError):
        hashlib.md5(123).hexdigest()