
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

import pytest

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    max_unique_chars = -1
    max_unique_char_word = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_unique_char_word = word
        elif unique_chars == max_unique_chars and word < max_unique_char_word:
            max_unique_char_word = word

    return max_unique_char_word


def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_find_max_basic():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_anagram():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_all_same():
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"

def test_find_max_mixed():
    assert find_max(["abc", "def", "ghi"]) == "abc"

def test_find_max_duplicates():
    assert find_max(["abc", "abc", "def"]) == "abc"

def test_find_max_empty_list():
    assert find_max([]) == ""