
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

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
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5_hash

def test_empty_string():
    assert string_to_md5("") is None

def test_valid_string_short():
    assert string_to_md5("test") == "e59ff95a994a324c78591969646935e4"

def test_valid_string_medium():
    assert string_to_md5("This is a medium string") == "8398233342063144823904368187323541297b19662318998854536457435624"

def test_valid_string_long():
    long_string = "This is a very long string to test the function." * 10
    assert string_to_md5(long_string) == "e999299552479423942a978e8b253a854442588347398a797234b63635443496"

def test_valid_string_special_chars():
    assert string_to_md5("!@#$%^&*()") == "5e884898da28047151d0e56f8dc6292773603d0d6aabba0715c2b4a1bb0a22d1f"

def test_valid_string_numbers():
    assert string_to_md5("1234567890") == "a4e3b59595a99999c9b7a99999999999"

def test_valid_string_mixed():
    assert string_to_md5("Hello123World!") == "a9a55568375175048454292573963792981928395662874786499953196b81"

def test_valid_string_unicode():
    assert string_to_md5("你好世界") == "09d43594a8329247966354594999999999999999999999999999999999999999"