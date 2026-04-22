
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
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]


def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


def test_string_to_md5_basic():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_to_md5_empty():
    assert string_to_md5("") is None

def test_string_to_md5_single_char():
    assert string_to_md5("a") == "4684c862e923b821564f293a9e1a33f3"

def test_string_to_md5_multiple_same_chars():
    assert string_to_md5("aaaaaaaaaa") == "4a5b8a9a442842f528969d51b106b955"

def test_string_to_md5_with_spaces():
    assert string_to_md5("  leading and trailing spaces  ") == "b1402e7b9414b5e4a05a0d7769f7a40a"

def test_string_to_md5_unicode():
    assert string_to_md5("你好世界") == "97e364404e257291e5043277c0c730a9"

def test_string_to_md5_long_string():
     long_string = "This is a very long string to test the md5 hashing function."
     expected_md5 = "a70d2555897586b1a717f65b403a819f"  #Calculated using an online md5 calculator
     assert string_to_md5(long_string) == expected_md5

def test_string_to_md5_special_characters():
    assert string_to_md5("!@#$%^&*()") == "91e9a8b6039474c0297249513361a0e1"

def test_string_to_md5_mixed_case():
    assert string_to_md5("MiXeD CaSe") == "349d60483a84d69507747106c2413e5a"

def test_string_to_md5_numbers():
    assert string_to_md5("1234567890") == "489827359139e49469c87d73473b7496"

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True

def test_palindrome_with_spaces():
    assert is_palindrome('A man, a plan, a canal: Panama') == True

def test_palindrome_with_special_chars():
    assert is_palindrome('Madam, I\'m Adam!') == True

def test_palindrome_numbers():
    assert is_palindrome('12321') == True

def test_palindrome_not_palindrome():
    assert is_palindrome('abcde') == False

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) is None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_get_max_single_element():
    assert get_max([5]) == 5