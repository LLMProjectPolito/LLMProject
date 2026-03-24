import pytest

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return ""

    max_unique = -1
    result = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique:
            max_unique = unique_chars
            result = word
        elif unique_chars == max_unique and word < result:
            result = word

    return result


def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"

def test_find_max_multiple_words_different_unique_chars():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_multiple_words_same_unique_chars_lexicographical_order():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_multiple_words_same_unique_chars_and_lexicographical_order():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_find_max_multiple_words_same_unique_chars_and_lexicographical_order_2():
    assert find_max(["abc", "bca", "cab"]) == "abc"

def test_find_max_words_with_duplicates():
    assert find_max(["aabbcc", "abc"]) == "abc"

def test_find_max_words_with_mixed_case():
    assert find_max(["Hello", "hello"]) == "Hello"

def test_find_max_words_with_special_characters():
    assert find_max(["!@#", "abc"]) == "abc"

def test_find_max_words_with_numbers():
    assert find_max(["123", "abc"]) == "abc"

def test_find_max_words_with_empty_string():
    assert find_max(["", "abc"]) == "abc"

def test_find_max_words_with_empty_string_and_empty_string():
    assert find_max(["", ""]) == ""

def test_find_max_words_with_mixed_empty_and_non_empty():
    assert find_max(["", "abc", ""]) == "abc"