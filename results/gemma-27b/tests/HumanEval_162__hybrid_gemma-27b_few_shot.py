
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import hashlib
import pytest

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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


def test_md5_basic():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('pytest') == '5a105e8b9d40e1329780d62ea2265d8a'

def test_md5_empty():
    assert string_to_md5('') == None

def test_md5_single_char():
    assert string_to_md5('a') == '0cc175b9c0f1b6a831c399e269772661'

def test_md5_numbers():
    assert string_to_md5('12345') == '827ccb0eea8a706c4c34a16891f84e7b'

def test_md5_with_spaces():
    assert string_to_md5('  test  ') == '9f86d081884c7d659a2feaa0c55ad015'

def test_md5_special_characters():
    assert string_to_md5('!@#$%^') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_md5_long_string():
    long_string = "This is a very long string to test the MD5 hash function."
    expected_md5 = '9f86d081884c7d659a2feaa0c55ad015'
    assert string_to_md5(long_string) == expected_md5

def test_md5_unicode():
    assert string_to_md5('你好世界') == '6f9d8969191999999999999999999999'

def test_md5_mixed_characters():
    assert string_to_md5('Hello123!@#') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_md5_mixed_case():
    assert string_to_md5('Hello World') == 'b10a8db164e0754105b7a99be72e3fe5' #Case sensitive

def test_md5_with_leading_and_trailing_spaces():
    assert string_to_md5('  hello  ') == '99299929999999999999999999999999'

# Palindrome tests
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Racecar') == False

# Max tests
def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4