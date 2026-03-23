import pytest
import math


# Focus: Empty/Null Input
def test_string_to_md5_empty_string():
    assert string_to_md5("") is None

def test_string_to_md5_none_input():
    assert string_to_md5(None) is None

# Focus: Valid String Input
def test_valid_string_input_normal_case():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_valid_string_input_with_spaces():
    assert string_to_md5("  test string  ") == "5a105e8b9d40e1329780d62ea2265d8a"

def test_valid_string_input_special_characters():
    assert string_to_md5("!@#$%^&*()") == "8a1b9699999999999999999999999999"

# Focus: Error/Exception Handling (for potentially very large strings)
def test_string_to_md5_empty_string():
    assert string_to_md5("") is None

def test_string_to_md5_large_string():
    large_string = "a" * 1000000
    assert isinstance(string_to_md5(large_string), str)

def test_string_to_md5_non_string_input():
    with pytest.raises(TypeError):
        string_to_md5(123)