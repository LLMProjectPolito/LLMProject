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
        return ""

    max_unique = -1
    max_word = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique:
            max_unique = unique_chars
            max_word = word
        elif unique_chars == max_unique:
            if word < max_word:
                max_word = word

    return max_word

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


def test_find_max_basic():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_all_same_unique():
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"

def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"

def test_find_max_multiple_max_unique():
    assert find_max(["abc", "bca", "cab"]) == "abc"

def test_find_max_with_empty_string():
    assert find_max(["", "abc"]) == "abc"

def test_find_max_with_duplicate_words():
    assert find_max(["abc", "abc", "def"]) == "abc"

def test_find_max_long_strings():
    assert find_max(["abcdefgh", "abcde"]) == "abcdefgh"

def test_find_max_mixed_case():
    assert find_max(["aBc", "AbC"]) == "AbC"

def test_find_max_special_characters():
    assert find_max(["!@#", "abc"]) == "!@"

def test_find_max_numbers_as_strings():
    assert find_max(["123", "12"]) == "123"

def test_find_max_complex_case():
    assert find_max(["abcdef", "abcde", "abcdf", "abc"]) == "abcdef"

def test_find_max_all_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None