import pytest
import hashlib

def test_string_to_md5_empty_string():
    assert string_to_md5("") is None

def test_string_to_md5_hello_world():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_to_md5_single_character():
    assert string_to_md5("a") == "0cc175b9c0f1b6a831c399e269772661"

def test_string_to_md5_numbers():
    assert string_to_md5("12345") == "827ccb0eea8a706c4c34a16891f84e7b"

def test_string_to_md5_special_characters():
    assert string_to_md5("!@#$%^&*()") == "4a44dc15364203f1cbe3a90f874306a2"

def test_string_to_md5_long_string():
    long_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    assert string_to_md5(long_string) == hashlib.md5(long_string.encode()).hexdigest()

def test_string_to_md5_non_ascii_characters():
    non_ascii_string = "éàü"
    assert string_to_md5(non_ascii_string) == hashlib.md5(non_ascii_string.encode()).hexdigest()

def test_string_to_md5_none_input():
    with pytest.raises(TypeError):
        string_to_md5(None)