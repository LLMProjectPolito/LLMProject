
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


def test_string_to_md5_empty():
    assert string_to_md5("") is None

def test_string_to_md5_simple():
    assert string_to_md5("abc") == "d41d8cd98f00b204e9800998ecf8427e"

def test_string_to_md5_with_spaces():
    assert string_to_md5("hello world") == "b10a8db164e3b56d68c7d9009c5b779e"

def test_string_to_md5_with_special_chars():
    assert string_to_md5("!@#$%^&*()") == "c74d5e05e821e75a4b186c8218b591b4"

def test_string_to_md5_unicode():
    assert string_to_md5("你好世界") == "7e275527c367057a43688b02d664764b"

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the md5 hash."
    assert string_to_md5(long_string) == "d28d5d4a17b98256946f656763772c03"

def test_string_to_md5_basic():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"
    assert string_to_md5("Python") == "18d5d5958885307e0b199895187f4d3c"
    assert string_to_md5("Test") == "b3a9945716739525223c7363d0a92402"

def test_string_to_md5_unicode():
    assert string_to_md5("你好世界") == "e935e27440d44a575039389b295b96f9"
    assert string_to_md5("नमस्ते") == "d8c252589ed8862213915a06b265a7b5"

def test_string_to_md5_special_chars():
    assert string_to_md5("!@#$%^&*()") == "f067492904f6f505003a6e9018210352"

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the md5 hash."
    assert string_to_md5(long_string) == "9d0b6535476139c7a997d71809f2d360"

def test_string_to_md5_with_spaces():
    assert string_to_md5("  Leading spaces  ") == "485c6c26690e45b8d8c851f2324965d7"
    assert string_to_md5("Trailing spaces  ") == "e0374159d4946b218322597192579b6a"
    assert string_to_md5("  Spaces only  ") == "c208b056f950d70058431b5394a34361"



def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_with_spaces():
    assert is_palindrome('A man, a plan, a canal: Panama') == False # Case sensitive

def test_palindrome_with_special_chars():
    assert is_palindrome('Racecar!') == False # Case sensitive

def test_palindrome_long_string():
    long_string = "A man, a plan, a canal: Panama"
    assert is_palindrome(long_string) == False

def test_palindrome_mixed_case():
    assert is_palindrome('RaceCar') == False # Case sensitive

def test_palindrome_numbers():
    assert is_palindrome('121') == True
    assert is_palindrome('123') == False

def test_palindrome_no_spaces():
    assert is_palindrome('madam') == True

def test_palindrome_with_unicode():
    assert is_palindrome("你好世界") == False # Case sensitive

def test_palindrome_with_mixed_unicode_and_ascii():
    assert is_palindrome("你好世界你好") == False # Case sensitive