
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
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]

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
    result = ""
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            result = word
        elif unique_chars == max_unique_chars and word < result:
            result = word
    return result


# --- Tests for is_palindrome ---
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

def test_palindrome_with_punctuation():
    assert is_palindrome('Madam, I\'m Adam') == True

def test_palindrome_with_numbers():
    assert is_palindrome('121') == True

def test_palindrome_with_numbers_and_letters():
    assert is_palindrome('A1b2c3a') == True

def test_palindrome_non_palindrome_with_spaces():
    assert is_palindrome('hello world') == False

# --- Tests for get_max ---
def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) is None

def test_max_single_element():
    assert get_max([5]) == 5

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 0, 1]) == 1

def test_max_duplicates():
    assert get_max([1, 1, 1]) == 1

# --- Tests for find_max ---
def test_find_max_basic():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_anagram():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_all_same():
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"

def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"

def test_find_max_multiple_words_same_unique_chars():
    assert find_max(["abc", "def", "ghi"]) == "abc"

def test_find_max_with_special_characters():
    assert find_max(["!@#", "$%^", "&*"]) == "!@#"

def test_find_max_with_mixed_characters():
    assert find_max(["a", "aa", "aaa"]) == "aaa"