import pytest
import hashlib

def test_string_to_md5_empty_string():
    assert string_to_md5("") is None

def test_string_to_md5_hello_world():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_single_character():
    assert string_to_md5('a') == '0cc175b9c0f1b6a831c399e269772661'

def test_string_to_md5_numbers():
    assert string_to_md5('12345') == '827ccb0eea8a706c4c34a16891f84e7b'

def test_string_to_md5_special_characters():
    assert string_to_md5('@#$%') == 'a7d9e0e2c4f6b8d0'

def test_string_to_md5_long_string():
    long_string = 'a' * 1000
    assert len(string_to_md5(long_string)) == 32

def test_string_to_md5_none_input():
    with pytest.raises(TypeError):
        string_to_md5(None)

def test_string_to_md5_non_string_input():
    with pytest.raises(TypeError):
        string_to_md5(12345)