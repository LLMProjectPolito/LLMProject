
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

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

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('') == True

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Madam') == True

def test_string_to_md5_empty():
    assert string_to_md5('') is None

def test_string_to_md5_basic():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_numbers():
    assert string_to_md5('12345') == 'e5e9fa1ba31c399e29f86537a1f380a3'

def test_string_to_md5_special_chars():
    assert string_to_md5('!@#$%^&*()') == 'e5e9fa1ba31c399e29f86537a1f380a3'

def test_string_to_md5_unicode():
    assert string_to_md5('你好世界') == 'a97959c065a93535098739766894a94a'