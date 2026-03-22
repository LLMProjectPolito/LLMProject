import pytest
import hashlib

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

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
    return hashlib.md5(text.encode()).hexdigest()

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True

def test_palindrome_empty():
    assert is_palindrome('') == True
    assert is_palindrome(' ') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([3, 2, 1]) == 3
    assert get_max([-1, 0, 1]) == 1

def test_max_empty():
    assert get_max([]) == None

def test_max_single_element():
    assert get_max([5]) == 5

def test_max_negative_numbers():
    assert get_max([-1, -2, -3]) == -1

def test_string_to_md5_basic():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('madam') == '2f8e19a86443452e'
    assert string_to_md5('') == None

def test_string_to_md5_unicode():
    assert string_to_md5('你好世界') == 'b9a8a9c710088e88e6e167723b79999'
    assert string_to_md5('नमस्ते दुनिया') == '99999999999999999999999999999999'

def test_string_to_md5_mixed():
    assert string_to_md5('Hello World!') == '6a3999d32ee468944d9693b899969999'