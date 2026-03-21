import pytest
import string_to_md5
import hashlib

def test_string_to_md5_normal_case():
    # Test with a string that has alphanumeric characters
    assert string_to_md5.string_to_md5('Hello world') == hashlib.md5('Hello world'.encode()).hexdigest()

def test_string_to_md5_special_case():
    # Test with a string that contains special characters
    assert string_to_md5.string_to_md5('@#$%^&*()_+-={}:<>?') == hashlib.md5('@#$%^&*()_+-={}:<>?'.encode()).hexdigest()

def test_string_to_md5_empty_string():
    # Test with an empty string
    assert string_to_md5.string_to_md5('') is None

def test_string_to_md5_none():
    # Test with a None string
    assert string_to_md5.string_to_md5(None) is None

def test_string_to_md5_number():
    # Test with a string that is a number
    assert string_to_md5.string_to_md5('123') == hashlib.md5('123'.encode()).hexdigest()

def test_string_to_md5_float():
    # Test with a string that is a float
    assert string_to_md5.string_to_md5('123.456') == hashlib.md5('123.456'.encode()).hexdigest()

def test_string_to_md5_single_character():
    # Test with a string that has a length of 1 (a single character)
    assert string_to_md5.string_to_md5('a') == hashlib.md5('a'.encode()).hexdigest()

def test_string_to_md5_max_length():
    # Test with a string that has a length of 255 (the maximum length of a string in Python)
    max_length_string = 'a' * 255
    assert string_to_md5.string_to_md5(max_length_string) == hashlib.md5(max_length_string.encode()).hexdigest()

def test_string_to_md5_excess_length():
    # Test with a string that has a length of 256 (beyond the maximum length of a string in Python)
    excess_length_string = 'a' * 256
    with pytest.raises(TypeError):
        string_to_md5.string_to_md5(excess_length_string)

def test_string_to_md5_non_string_input():
    # Test with a non-string input
    with pytest.raises(TypeError):
        string_to_md5.string_to_md5(123)

def test_string_to_md5_bytes_input():
    # Test with a bytes input
    assert string_to_md5.string_to_md5('Hello world'.encode()) == hashlib.md5('Hello world'.encode()).hexdigest()

def test_empty_string():
    # Test with an empty string
    assert string_to_md5.string_to_md5('') is None

def test_single_character_string():
    # Test with a single character string
    assert string_to_md5.string_to_md5('a') != None

def test_longer_string():
    # Test with a longer string
    assert string_to_md5.string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_non_ascii_string():
    # Test with a non-ASCII string
    assert string_to_md5.string_to_md5('ñóáéíúü') != None

def test_none_input():
    # Test with a None input
    assert string_to_md5.string_to_md5(None) is None

def test_non_string_input():
    # Test with a non-string input
    with pytest.raises(TypeError):
        string_to_md5.string_to_md5(123)

def test_non_hashable_input():
    # Test with a non-hashable input
    with pytest.raises(TypeError):
        string_to_md5.string_to_md5({'a': 1})

def test_large_input():
    # Test with a large input
    assert len(string_to_md5.string_to_md5('a' * 1000)) == 32

def test_duplicate_input():
    # Test with a duplicate input
    assert string_to_md5.string_to_md5('Hello') == string_to_md5.string_to_md5('Hello')

def test_case_sensitivity():
    # Test with a case-sensitive input
    assert string_to_md5.string_to_md5('Hello') != string_to_md5.string_to_md5('hello')

def test_whitespace_input():
    # Test with a whitespace input
    assert string_to_md5.string_to_md5('   Hello world   ') == string_to_md5.string_to_md5('Hello world')

def test_string_to_md5_max_hash_length():
    # Test with a string that has a length of 32 (the maximum length of a hash in Python)
    max_hash_length_string = 'a' * 32
    assert string_to_md5.string_to_md5(max_hash_length_string) == hashlib.md5(max_hash_length_string.encode()).hexdigest()

def test_string_to_md5_excess_hash_length():
    # Test with a string that has a length of 33 (beyond the maximum length of a hash in Python)
    excess_hash_length_string = 'a' * 33
    with pytest.raises(TypeError):
        string_to_md5.string_to_md5(excess_hash_length_string)

def test_string_to_md5_invalid_input():
    # Test with an invalid input (e.g., a list or a dictionary)
    with pytest.raises(TypeError):
        string_to_md5.string_to_md5([1, 2, 3])

def test_string_to_md5_invalid_type():
    # Test with an invalid type (e.g., a complex number)
    with pytest.raises(TypeError):
        string_to_md5.string_to_md5(1 + 2j)

def test_string_to_md5_invalid_encoding():
    # Test with an invalid encoding (e.g., a string with a non-ASCII encoding)
    with pytest.raises(TypeError):
        string_to_md5.string_to_md5('Hello world'.encode('latin1'))