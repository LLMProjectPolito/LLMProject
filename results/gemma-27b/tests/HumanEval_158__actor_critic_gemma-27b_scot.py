
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

    >>> find_max(["name", "of", "string"])
    'string'
    >>> find_max(["name", "enam", "game"])
    'enam'
    >>> find_max(["aaaaaaa", "bb" ,"cc"])
    'aaaaaaa'
    """
    max_unique = 0
    max_word = ""

    for word in words:
        unique_count = len(set(word))
        if unique_count > max_unique:
            max_unique = unique_count
            max_word = word
        elif unique_count == max_unique and word < max_word:
            max_word = word

    return max_word

def test_empty_list():
    """Test with an empty list. Should return an empty string."""
    assert find_max([]) == ""

def test_single_word():
    """Test with a list containing a single word. Should return that word."""
    assert find_max(["hello"]) == "hello"

def test_multiple_words_different_unique_counts():
    """Test with multiple words having different numbers of unique characters."""
    assert find_max(["name", "of", "string"]) == "string"

def test_same_unique_lexicographical():
    """Tests that when multiple words have the same number of unique characters, the lexicographically smaller word is returned."""
    assert find_max(["name", "enam", "game"]) == "enam"

def test_words_with_empty_strings():
    """Test with a list containing empty strings and other words."""
    assert find_max(["", "hello", "world"]) == "world"

def test_all_empty_strings():
    """Test with a list containing only empty strings. Should return an empty string."""
    assert find_max(["", "", ""]) == ""

def test_words_with_special_characters():
    """Test with words containing special characters."""
    assert find_max(["abc!", "def@", "ghi#"]) == "abc!"

def test_long_words():
    """Test with long words to ensure correct handling of longer strings."""
    assert find_max(["abcdefghijklmnopqrstuvwxyz", "abcdefghijklm"]) == "abcdefghijklmnopqrstuvwxyz"

def test_numbers_as_strings():
    """Test with a list of strings that represent numbers."""
    assert find_max(["123", "45", "6789"]) == "6789"

def test_large_list_similar_counts():
    """Test with a larger list of words with similar unique character counts to check performance."""
    words = ["word" + str(i) for i in range(1000)]
    words = [w + "a" for w in words] # make unique counts similar
    assert find_max(words) == "word999a"

def test_mixed_case():
    """Test with words containing mixed case characters."""
    assert find_max(["aBc", "AbC"]) == "AbC"

def test_same_unique_lexicographical_equal():
    """Test when multiple words have the same max unique chars and are lexicographically equal."""
    assert find_max(["abc", "abc", "def"]) == "abc"

def test_unicode_characters():
    """Test with words containing unicode characters."""
    assert find_max(["你好", "世界", "abc"]) == "世界"