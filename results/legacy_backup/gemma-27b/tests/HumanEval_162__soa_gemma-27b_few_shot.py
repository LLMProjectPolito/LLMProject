import hashlib
import pytest

def test_string_to_md5_basic():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty():
    assert string_to_md5('') is None

def test_string_to_md5_single_char():
    assert string_to_md5('a') == '0cc175b9c0f1b6a831c399e269772661'

def test_string_to_md5_with_spaces():
    assert string_to_md5('  test  ') == '69814199999999999999999999999999'

def test_string_to_md5_with_numbers():
    assert string_to_md5('12345') == '827ccb0eea8a706c4c34a16891f84e7b'

def test_string_to_md5_with_special_chars():
    assert string_to_md5('!@#$%^') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the md5 hash function."
    assert string_to_md5(long_string) == '9f86d081884c7d659a2feaa0c55ad015'