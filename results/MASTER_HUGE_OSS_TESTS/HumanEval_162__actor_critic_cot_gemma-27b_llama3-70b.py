import pytest
import hashlib

@pytest.mark.parametrize(
    "input_string, expected_hash",
    [
        ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
        ("  Hello world  ", "b10a8db164e0754105b7a99be72e3fe5"),
        ("!@#$%^&*()_+=-", "5994471abb01112afcc18159f6cc74b4"),
        ("a" * 1000, "d7a8fbb307d7809469ca9abcb0082e4f"),
        ("你好世界", "68494759999999999999999999999999"),
        ("Hello\nworld", "b10a8db164e0754105b7a99be72e3fe5"),
        ("Hello\tworld", "b10a8db164e0754105b7a99be72e3fe5"),
        (b'\x01\x01\x01\x01', "e80544996f199f898999999999999999"),
        ("a" * 5000, "99999999999999999999999999999999"),
    ],
)
def test_string_hashing(input_string, expected_hash):
    if isinstance(input_string, bytes):
        assert string_to_md5(input_string) == expected_hash
    else:
        assert string_to_md5(input_string) == expected_hash

def test_empty_string():
    assert string_to_md5("") is None

def test_non_utf8_string():
    assert string_to_md5("你好世界") == hashlib.md5("你好世界".encode('utf-8')).hexdigest()

def test_none_input():
    with pytest.raises(TypeError):
        string_to_md5(None)

def test_integer_input():
    with pytest.raises(TypeError):
        string_to_md5(123)

def test_float_input():
    with pytest.raises(TypeError):
        string_to_md5(123.45)

def test_list_input():
    with pytest.raises(TypeError):
        string_to_md5([1, 2, 3])

def test_dict_input():
    with pytest.raises(TypeError):
        string_to_md5({"a": 1, "b": 2})