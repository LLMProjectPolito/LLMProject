import pytest
import math


# Focus: Boundary Values
import hashlib

def test_string_to_md5_empty():
    assert string_to_md5("") is None

def test_string_to_md5_single_char():
    assert string_to_md5("a") == hashlib.md5("a".encode()).hexdigest()

def test_string_to_md5_whitespace():
    assert string_to_md5(" ") == hashlib.md5(" ".encode()).hexdigest()

# Focus: Error Handling
import pytest
from hashlib import md5

def test_string_to_md5_empty_string():
    from your_module import string_to_md5  # Replace your_module
    assert string_to_md5("") is None

def test_string_to_md5_invalid_input():
    from your_module import string_to_md5  # Replace your_module
    with pytest.raises(TypeError):
        string_to_md5(123)

def test_string_to_md5_correct_hash():
    from your_module import string_to_md5  # Replace your_module
    assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

# Focus: Logic Branches
import hashlib

def test_string_to_md5_valid():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty():
    assert string_to_md5('') is None

def test_string_to_md5_different_string():
    assert string_to_md5("test") == "098f6bcd4621d373cade4e832627b4f6"