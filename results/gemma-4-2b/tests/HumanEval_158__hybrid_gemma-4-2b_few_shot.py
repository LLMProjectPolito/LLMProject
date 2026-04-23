
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

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    if not words:
        return None

    max_unique_chars = -1
    max_unique_word = None

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_unique_word = word
        elif unique_chars == max_unique_chars and word < max_unique_word:
            max_unique_word = word

    return max_unique_word

def test_find_max_basic():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_find_max_empty():
    assert find_max([]) is None

def test_find_max_same_unique_chars():
    assert find_max(["abc", "bca", "cab"]) == "abc" # lexicographical order

def test_find_max_all_same_unique_chars():
    assert find_max(["abc", "def", "ghi"]) == "abc"

def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"

def test_find_max_duplicate_words():
    assert find_max(["name", "name"]) == "name"

def test_find_max_long_words():
    assert find_max(["abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"]) == "abcdefghijklmnopqrstuvwxyz"

def test_find_max_mixed_case():
    assert find_max(["a", "A"]) == "A"

def test_find_max_special_characters():
    assert find_max(["!@#$", "abc"]) == "!@#$"

def test_find_max_long_word():
    assert find_max(["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "bb"]) == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

def test_find_max_all_same():
    assert find_max(["aaaa", "aaaa", "aaaa"]) == "aaaa"

def test_find_max_mixed_case_and_special():
    assert find_max(["a", "!@#"]) == "!@#"
    assert find_max(["A", "!@#"]) == "!@#"
    assert find_max(["a", "A", "!@#"]) == "!@#"


def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Racecar') == True

def test_palindrome_special_chars():
    assert is_palindrome('A man, a plan, a canal: Panama') == False # not a palindrome
    assert is_palindrome('Madam, I\'m Adam') == False # not a palindrome

def test_palindrome_with_spaces():
    assert is_palindrome("  racecar  ") == False

def test_palindrome_with_punctuation():
    assert is_palindrome("Was it a car or a cat I saw?") == False

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) is None

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 0, 1]) == 1

def test_max_single_element():
    assert get_max([5]) == 5

def test_max_duplicate_elements():
    assert get_max([1, 1, 1]) == 1